from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from .database import engine
from .routers.portfolio import router as portfolio_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(title="Portfolio Tracker", lifespan=lifespan)

app.include_router(portfolio_router, prefix="/assets", tags=["assets"])
