from fastapi import APIRouter

from app.models.schemas import QuestionRequest
from app.services.ai_service import genrate_response
from app.services.cache_service import (
    get_cached_response,
    cache_response
)
from app.utils.stats import cache_stats

router = APIRouter()


@router.post("/ask")
async def ask_question(request: QuestionRequest):

    cache_stats.increment_request()

    cached_response = await get_cached_response(
        request.question
    )

    print("QUESTION:", request.question)
    print("CACHED:", cached_response)

    if cached_response is not None:

        cache_stats.increment_hit()

        return {
            "cached": True,
            "answer": cached_response
        }

    cache_stats.increment_miss()

    ai_response = await genrate_response(
        request.question
    )

    await cache_response(
        request.question,
        ai_response
    )

    return {
        "cached": False,
        "answer": ai_response
    }


@router.get("/stats")
async def get_stats():
    return cache_stats.get_stats()