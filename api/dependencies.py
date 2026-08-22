from typing import Iterator

from fastapi import Header, HTTPException, status

from api.config import settings
from api.controllers.ticket_controller import TicketController
from api.db import get_connection
from api.repositories.ticket_repository import TicketRepository
from api.services.ticket_service import TicketService


def require_api_key(x_api_key: str = Header(default="")) -> None:
    if x_api_key == settings.api_key:
        return
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")


def get_ticket_controller() -> Iterator[TicketController]:
    with get_connection() as connection:
        repository = TicketRepository(connection)
        service = TicketService(repository)
        yield TicketController(service)
