from app.services.ai_service import genrate_response
import asyncio

async def main():
    response = await genrate_response("What is redis?")

    print(response)

asyncio.run(main())