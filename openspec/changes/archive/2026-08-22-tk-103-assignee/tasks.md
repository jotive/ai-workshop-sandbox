## 1. Esquema y DTOs

- [x] 1.1 `api/db.py`: agregar columna `assignee TEXT` (nullable) al `SCHEMA` de `tickets`.
- [x] 1.2 `api/schemas/ticket.py`: agregar `assignee: str | None = None` a `TicketCreateRequest` y a `TicketResponse`; agregar `TicketAssignRequest { assignee: str }` (requerido, `min_length=1`).

## 2. Capas

- [x] 2.1 `api/repositories/ticket_repository.py`: `create()` acepta `assignee` opcional y lo inserta; agregar `assign(ticket_id, assignee) -> Row`.
- [x] 2.2 `api/services/ticket_service.py`: `create_ticket()` pasa `request.assignee`; agregar `assign_ticket(ticket_id, assignee)` (levanta `TicketNotFoundError` si no existe).
- [x] 2.3 `api/controllers/ticket_controller.py`: incluir `assignee` en `_to_ticket_response`; agregar método `assign()`.
- [x] 2.4 `api/routes/tickets.py`: agregar `POST /tickets/{ticket_id}/assign` con body `TicketAssignRequest`.

## 3. Front

- [x] 3.1 `front/index.html`: input de "Asignado a" (opcional) en el formulario de creación; mostrar el assignee (o "sin asignar") en cada card; botón "Reasignar".

## 4. Tests

- [x] 4.1 Unitarios en `tests/unit/test_ticket_repository.py`: crear con/sin assignee, `assign()` actualiza.
- [x] 4.2 Unitarios en `tests/unit/test_ticket_service.py`: `assign_ticket` actualiza y levanta `TicketNotFoundError` si no existe.
- [x] 4.3 Integración en `tests/integration/test_tickets_api.py`: crear con assignee, reasignar, reasignar ticket inexistente devuelve 404.

## 5. Docs

- [x] 5.1 Actualizar `docs/architecture.md` y `docs/glossary.md` para reflejar el campo `assignee`.

## Criterio de éxito (verificado)

- `pytest` en verde, incluyendo todos los tests de `assignee`.
- `POST /tickets` con `assignee` en el body lo persiste y lo devuelve; sin `assignee` devuelve `null`.
- `POST /tickets/{id}/assign` actualiza el campo y lo refleja en `GET /tickets` inmediatamente después.
- El front permite crear un ticket con assignee y reasignarlo sin recargar la página.
