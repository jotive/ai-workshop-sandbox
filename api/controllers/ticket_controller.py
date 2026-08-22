import sqlite3

from api.schemas.ticket import (
    StatsResponse,
    TicketCreateRequest,
    TicketPriority,
    TicketResponse,
)
from api.services.ticket_service import TicketService


def _to_ticket_response(row: sqlite3.Row) -> TicketResponse:
    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        priority=row["priority"],
        status=row["status"],
        created_at=row["created_at"],
    )


class TicketController:
    def __init__(self, service: TicketService) -> None:
        self._service = service

    def create(self, request: TicketCreateRequest) -> TicketResponse:
        ticket = self._service.create_ticket(request)
        return _to_ticket_response(ticket)

    def list(self, priority: TicketPriority | None = None) -> list[TicketResponse]:
        tickets = self._service.list_tickets(priority)
        return [_to_ticket_response(ticket) for ticket in tickets]

    def close(self, ticket_id: int) -> TicketResponse:
        ticket = self._service.close_ticket(ticket_id)
        return _to_ticket_response(ticket)

    def stats(self) -> StatsResponse:
        return self._service.get_stats()
