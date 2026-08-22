from typing import Annotated

from fastapi import APIRouter, Depends

from api.controllers.ticket_controller import TicketController
from api.dependencies import get_ticket_controller, require_api_key
from api.schemas.ticket import StatsResponse

router = APIRouter(dependencies=[Depends(require_api_key)])


@router.get("/stats", response_model=StatsResponse)
def get_stats(
    controller: Annotated[TicketController, Depends(get_ticket_controller)],
) -> StatsResponse:
    return controller.stats()
