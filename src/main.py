from fastapi import FastAPI
from src.routers import rifa_router, numeros_router

app = FastAPI()
app.include_router(rifa_router)
app.include_router(numeros_router)
