import sqlite3

from api.repositories.ticket_repository import TicketRepository
from api.schemas.ticket import StatsResponse, TicketCreateRequest, TicketPriority


class TicketNotFoundError(Exception):
    pass


class TicketService:
    def __init__(self, repository: TicketRepository) -> None:
        self._repository = repository

    def create_ticket(self, request: TicketCreateRequest) -> sqlite3.Row:
        return self._repository.create(
            request.title, request.description, request.priority, request.assignee
        )

    def list_tickets(self, priority: TicketPriority | None = None) -> list[sqlite3.Row]:
        return self._repository.find_all(priority)

    def close_ticket(self, ticket_id: int) -> sqlite3.Row:
        ticket = self._repository.find_by_id(ticket_id)
        if ticket is None:
            raise TicketNotFoundError(f"Ticket {ticket_id} not found")
        return self._repository.close(ticket_id)

    def assign_ticket(self, ticket_id: int, assignee: str) -> sqlite3.Row:
        ticket = self._repository.find_by_id(ticket_id)
        if ticket is None:
            raise TicketNotFoundError(f"Ticket {ticket_id} not found")
        return self._repository.assign(ticket_id, assignee)

    def get_stats(self) -> StatsResponse:
        return StatsResponse(
            total=self._repository.count_total(),
            open=self._repository.count_open(),
            closed=self._repository.count_closed(),
        )
