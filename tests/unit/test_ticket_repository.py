import sqlite3

import pytest

from api.db import SCHEMA
from api.repositories.ticket_repository import TicketRepository
from api.schemas.ticket import TicketPriority, TicketStatus


@pytest.fixture
def repository() -> TicketRepository:
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    connection.execute(SCHEMA)
    return TicketRepository(connection)


def test_create_ticket_starts_open(repository: TicketRepository) -> None:
    ticket = repository.create("Broken login", "Users can't log in", TicketPriority.HIGH)

    assert ticket["status"] == TicketStatus.OPEN.value
    assert ticket["priority"] == TicketPriority.HIGH.value


def test_find_all_returns_every_ticket_without_filter(repository: TicketRepository) -> None:
    repository.create("First", "", TicketPriority.LOW)
    repository.create("Second", "", TicketPriority.HIGH)

    assert len(repository.find_all()) == 2


def test_find_all_filters_by_priority(repository: TicketRepository) -> None:
    repository.create("Low prio", "", TicketPriority.LOW)
    repository.create("High prio", "", TicketPriority.HIGH)

    results = repository.find_all(priority=TicketPriority.HIGH)

    assert len(results) == 1
    assert results[0]["priority"] == TicketPriority.HIGH.value


def test_close_updates_status(repository: TicketRepository) -> None:
    ticket = repository.create("Fix bug", "", TicketPriority.MEDIUM)

    closed = repository.close(ticket["id"])

    assert closed["status"] == TicketStatus.CLOSED.value


def test_count_closed_only_counts_closed_tickets(repository: TicketRepository) -> None:
    repository.create("Stays open", "", TicketPriority.LOW)
    to_close = repository.create("Gets closed", "", TicketPriority.LOW)
    repository.close(to_close["id"])

    assert repository.count_closed() == 1
    assert repository.count_total() == 2


def test_count_open_excludes_closed_tickets(repository: TicketRepository) -> None:
    repository.create("Stays open", "", TicketPriority.LOW)
    to_close = repository.create("Gets closed", "", TicketPriority.LOW)
    repository.close(to_close["id"])

    assert repository.count_open() == 1
