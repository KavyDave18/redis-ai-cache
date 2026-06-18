from app.services.cache_service import (get_cached_response,cache_response)
import asyncio

async def main():
    await cache_response("what is redis?","Redis is awsome")

    result = await get_cached_response("what is redis?")

    print(result)

asyncio.run(main())