import pytest

from api.schemas.ticket import TicketCreateRequest, TicketPriority
from api.services.ticket_service import TicketNotFoundError, TicketService


class FakeTicketRepository:
    def __init__(self) -> None:
        self._tickets: dict[int, dict] = {}
        self._next_id = 1

    def create(self, title: str, description: str, priority: TicketPriority) -> dict:
        ticket = {
            "id": self._next_id,
            "title": title,
            "description": description,
            "priority": priority.value,
            "status": "open",
            "created_at": "2026-08-20T00:00:00+00:00",
        }
        self._tickets[ticket["id"]] = ticket
        self._next_id += 1
        return ticket

    def find_all(self, priority: TicketPriority | None = None) -> list[dict]:
        tickets = list(self._tickets.values())
        if priority is None:
            return tickets
        return [ticket for ticket in tickets if ticket["priority"] == priority.value]

    def find_by_id(self, ticket_id: int) -> dict | None:
        return self._tickets.get(ticket_id)

    def close(self, ticket_id: int) -> dict:
        self._tickets[ticket_id]["status"] = "closed"
        return self._tickets[ticket_id]

    def count_total(self) -> int:
        return len(self._tickets)

    def count_open(self) -> int:
        return sum(1 for ticket in self._tickets.values() if ticket["status"] == "open")

    def count_closed(self) -> int:
        return sum(1 for ticket in self._tickets.values() if ticket["status"] == "closed")


def test_create_ticket_delegates_to_repository() -> None:
    service = TicketService(FakeTicketRepository())

    ticket = service.create_ticket(TicketCreateRequest(title="New bug", priority=TicketPriority.HIGH))

    assert ticket["title"] == "New bug"
    assert ticket["priority"] == TicketPriority.HIGH.value


def test_close_ticket_raises_when_missing() -> None:
    service = TicketService(FakeTicketRepository())

    with pytest.raises(TicketNotFoundError):
        service.close_ticket(999)


def test_close_ticket_marks_it_closed() -> None:
    service = TicketService(FakeTicketRepository())
    ticket = service.create_ticket(TicketCreateRequest(title="Fix it"))

    closed = service.close_ticket(ticket["id"])

    assert closed["status"] == "closed"


def test_list_tickets_filters_by_priority() -> None:
    service = TicketService(FakeTicketRepository())
    service.create_ticket(TicketCreateRequest(title="A", priority=TicketPriority.LOW))
    service.create_ticket(TicketCreateRequest(title="B", priority=TicketPriority.HIGH))

    results = service.list_tickets(priority=TicketPriority.HIGH)

    assert len(results) == 1
    assert results[0]["title"] == "B"
