import asyncio

async def genrate_response(question:str) -> str:
    await asyncio.sleep(2)
    return f"Ai response :{question}"