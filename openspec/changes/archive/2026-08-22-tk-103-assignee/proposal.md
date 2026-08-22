## Why

Se pidió: "Necesito poder asignarle un responsable a cada ticket, tanto al crearlo como después si cambia de dueño." El dominio de ticket no tenía ningún campo de responsable.

## What Changes

- Se agrega la columna `assignee TEXT` (nullable) a la tabla `tickets`.
- `POST /tickets` acepta un `assignee` opcional en el body; sin él, el ticket queda sin asignar (`null`).
- Se agrega un endpoint dedicado `POST /tickets/{id}/assign` para (re)asignar un ticket ya creado.
- El front agrega un input de "Asignado a" (opcional) en el formulario de creación, muestra el assignee en cada card de ticket, y agrega un botón "Reasignar".

## Capabilities

### New Capabilities
- `ticket-assignment`: asignar y reasignar un responsable (`assignee`, texto libre) a un ticket, al crearlo o después. Primera vez que esta capability se documenta como spec en esta rama.

## Impact

- Esquema: nueva columna `assignee` en `tickets` (`api/db.py`).
- DTOs: `assignee` opcional en `TicketCreateRequest`/`TicketResponse`; nuevo DTO `TicketAssignRequest` (`api/schemas/ticket.py`).
- Capas: `api/repositories/ticket_repository.py` (`create()` acepta `assignee`, nuevo método `assign()`), `api/services/ticket_service.py` (nuevo `assign_ticket()`), `api/controllers/ticket_controller.py` (incluir `assignee` en la respuesta, nuevo método `assign()`), `api/routes/tickets.py` (nueva ruta `POST /tickets/{id}/assign`).
- Front: `front/index.html` (input de assignee al crear, texto de assignee en cada card, botón "Reasignar").
- Docs: `docs/architecture.md` y `docs/glossary.md` actualizados para reflejar el campo `assignee`.

## Estado

**Implementado en esta rama** (`reference/tk-103`) — solución de referencia para el ejercicio de la jornada de capacitación. `main` sigue sin el campo `assignee` (ver `openspec/changes/tk-103-assignee/` en `main`, abierto). Este change se archiva inmediatamente después de escribirse, como traza retroactiva de la feature ya implementada en esta rama.
