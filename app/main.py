from fastapi import FastAPI
from app.routes.ai_routes import router

app = FastAPI(
    title = "Redis AI Cache",
    version="1.0.0"
    )

app.include_router(router)