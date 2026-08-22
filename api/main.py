import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.config import settings
from api.db import init_db
from api.logging_config import configure_logging
from api.routes import health, stats, tickets
from api.services.ticket_service import TicketNotFoundError

configure_logging(settings.log_level)
logger = logging.getLogger("tickets-api")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    init_db()
    logger.info("startup complete")
    yield


app = FastAPI(title="Tickets API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(TicketNotFoundError)
def handle_ticket_not_found(request: Request, exc: TicketNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": str(exc)})


app.include_router(health.router)
app.include_router(stats.router)
app.include_router(tickets.router)
