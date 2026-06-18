import os
from dotenv import load_dotenv
from app.config.redis import redis_client

CACHE_TTL = int(os.getenv("CACHE_TTL",3600))

async def get_cached_response(question:str):
    return await redis_client.get(question)

async def cache_response(question:str,response:str):
    await redis_client.setex(question,CACHE_TTL,response)