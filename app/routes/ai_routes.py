import time

from fastapi import APIRouter

from app.models.schemas import QuestionRequest
from app.services.ai_service import genrate_response
from app.services.cache_service import (
    get_cached_response,
    cache_response,
    delete_cache_response
)
from app.utils.stats import cache_stats

router = APIRouter()


@router.post("/ask")
async def ask_question(request: QuestionRequest):

    cache_stats.increment_request()

    start_time = time.perf_counter()

    cached_response = await get_cached_response(
        request.question
    )

    if cached_response is not None:

        cache_stats.increment_hit()

        end_time = time.perf_counter()

        response_time_ms = round(
            (end_time - start_time) * 1000,
            2
        )

        return {
            "cached": True,
            "answer": cached_response,
            "response_time_ms": response_time_ms
        }

    cache_stats.increment_miss()

    ai_response = await genrate_response(
        request.question
    )

    await cache_response(
        request.question,
        ai_response
    )

    end_time = time.perf_counter()

    response_time_ms = round(
        (end_time - start_time) * 1000,
        2
    )

    return {
        "cached": False,
        "answer": ai_response,
        "response_time_ms": response_time_ms
    }


@router.get("/stats")
async def get_stats():

    return cache_stats.get_stats()

@router.delete("/cache/{question}")
async def delete_cache(question:str):
    deleted = await delete_cache_response(question)

    if deleted:
        return{
            "success":True,
            "messege":"Cache deleted"
            }

    return{
        "success":False,
        "messege":"Cache not found"
        }
