import sqlite3
from datetime import datetime, timezone

from api.schemas.ticket import TicketPriority, TicketStatus


class TicketRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

    def create(self, title: str, description: str, priority: TicketPriority) -> sqlite3.Row:
        created_at = datetime.now(timezone.utc).isoformat()
        cursor = self._connection.execute(
            """
            INSERT INTO tickets (title, description, priority, status, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, description, priority.value, TicketStatus.OPEN.value, created_at),
        )
        return self.find_by_id(cursor.lastrowid)

    def find_all(self, priority: TicketPriority | None = None) -> list[sqlite3.Row]:
        if priority is None:
            return self._connection.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
        return self._connection.execute(
            "SELECT * FROM tickets WHERE priority = ? ORDER BY id DESC",
            (priority.value,),
        ).fetchall()

    def find_by_id(self, ticket_id: int) -> sqlite3.Row | None:
        return self._connection.execute(
            "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
        ).fetchone()

    def close(self, ticket_id: int) -> sqlite3.Row | None:
        self._connection.execute(
            "UPDATE tickets SET status = ? WHERE id = ?",
            (TicketStatus.CLOSED.value, ticket_id),
        )
        return self.find_by_id(ticket_id)

    def count_total(self) -> int:
        row = self._connection.execute("SELECT COUNT(*) AS count FROM tickets").fetchone()
        return row["count"]

    def count_open(self) -> int:
        row = self._connection.execute(
            "SELECT COUNT(*) AS count FROM tickets WHERE status = ?",
            (TicketStatus.OPEN.value,),
        ).fetchone()
        return row["count"]

    def count_closed(self) -> int:
        row = self._connection.execute(
            "SELECT COUNT(*) AS count FROM tickets WHERE status = ?",
            (TicketStatus.CLOSED.value,),
        ).fetchone()
        return row["count"]
