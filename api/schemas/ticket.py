from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TicketStatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


class TicketCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=2000)
    priority: TicketPriority = TicketPriority.MEDIUM
    assignee: str | None = Field(default=None, max_length=200)


class TicketAssignRequest(BaseModel):
    assignee: str = Field(min_length=1, max_length=200)


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: TicketPriority
    status: TicketStatus
    assignee: str | None
    created_at: datetime


class StatsResponse(BaseModel):
    total: int
    open: int
    closed: int
