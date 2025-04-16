from fastapi import FastAPI
from app.routers import user_router, post_router

app = FastAPI(title="Simple social network")

app.include_router(user_router.router)
app.include_router(post_router.router)

@app.get("/")
async def root():
    return {"mensaje": "Hola, FastAPI en windsurf!"}