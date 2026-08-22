## 1. Esquema y DTOs

- [ ] 1.1 `api/db.py`: agregar columna `assignee TEXT` (nullable) al `SCHEMA` de `tickets`.
- [ ] 1.2 `api/schemas/ticket.py`: agregar `assignee: str | None = None` a `TicketCreateRequest` y a `TicketResponse`; agregar un DTO nuevo `TicketAssignRequest { assignee: str }` (requerido, `min_length=1`, no puede reasignarse a vacío).

## 2. Capas

- [ ] 2.1 `api/repositories/ticket_repository.py`: `create()` acepta `assignee` opcional y lo inserta; agregar `assign(ticket_id, assignee) -> Row` que hace `UPDATE tickets SET assignee = ? WHERE id = ?`.
- [ ] 2.2 `api/services/ticket_service.py`: `create_ticket()` pasa `request.assignee` al repositorio; agregar `assign_ticket(ticket_id, assignee)` que reusa el mismo chequeo de "no existe" que `close_ticket()` (levanta `TicketNotFoundError`).
- [ ] 2.3 `api/controllers/ticket_controller.py`: incluir `assignee` en `_to_ticket_response`; agregar método `assign()`.
- [ ] 2.4 `api/routes/tickets.py`: agregar `POST /tickets/{ticket_id}/assign` con body `TicketAssignRequest`.

## 3. Front

- [ ] 3.1 `front/index.html`: agregar input de "Asignado a" (opcional) en el formulario de creación; mostrar el assignee (o "sin asignar") en cada card de ticket; agregar un botón "Reasignar" que pida el nuevo assignee y llame al endpoint nuevo.

## 4. Tests

- [ ] 4.1 Unitarios en `tests/unit/test_ticket_repository.py`: crear con/sin assignee, `assign()` actualiza.
- [ ] 4.2 Unitarios en `tests/unit/test_ticket_service.py`: `assign_ticket` actualiza y levanta `TicketNotFoundError` si no existe.
- [ ] 4.3 Integración en `tests/integration/test_tickets_api.py`: crear con assignee, reasignar, reasignar ticket inexistente devuelve 404.

## 5. Docs

- [ ] 5.1 Actualizar `docs/architecture.md` (sección "Dominio: Ticket" y "Lo que NO existe") y `docs/glossary.md` (entrada "Assignee") para reflejar que el campo ya existe, una vez implementado.

## Criterio de éxito

- `pytest` en verde, incluyendo todos los tests nuevos de `assignee`.
- `POST /tickets` con `assignee` en el body lo persiste y lo devuelve en la respuesta; sin `assignee` devuelve `null`.
- `POST /tickets/{id}/assign` actualiza el campo y lo refleja en `GET /tickets` inmediatamente después.
- El front permite crear un ticket con assignee y reasignarlo sin recargar la página.

## Qué NO entra en este change

- Entidad "usuario"/autenticación por persona — `assignee` sigue siendo texto libre, no una referencia a una tabla de usuarios.
- Notificar al assignee (email, webhook, etc.) — no se pidió.
- Filtrar el listado por assignee (como TK-101 hizo con prioridad) — es un change aparte si se necesita.
