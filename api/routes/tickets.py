from typing import Annotated

from fastapi import APIRouter, Depends

from api.controllers.ticket_controller import TicketController
from api.dependencies import get_ticket_controller, require_api_key
from api.schemas.ticket import TicketCreateRequest, TicketPriority, TicketResponse

router = APIRouter(prefix="/tickets", tags=["tickets"], dependencies=[Depends(require_api_key)])


@router.get("", response_model=list[TicketResponse])
def list_tickets(
    controller: Annotated[TicketController, Depends(get_ticket_controller)],
    priority: TicketPriority | None = None,
) -> list[TicketResponse]:
    return controller.list(priority)


@router.post("", response_model=TicketResponse, status_code=201)
def create_ticket(
    request: TicketCreateRequest,
    controller: Annotated[TicketController, Depends(get_ticket_controller)],
) -> TicketResponse:
    return controller.create(request)


@router.post("/{ticket_id}/close", response_model=TicketResponse)
def close_ticket(
    ticket_id: int,
    controller: Annotated[TicketController, Depends(get_ticket_controller)],
) -> TicketResponse:
    return controller.close(ticket_id)
