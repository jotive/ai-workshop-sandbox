## Why

Se pidió: "Necesito poder asignarle un responsable a cada ticket, tanto al crearlo como después si cambia de dueño." Hoy el dominio de ticket no tiene ningún campo de responsable — no hay forma de saber quién es dueño de un ticket sin salir del sistema.

## What Changes

- Se agrega la columna `assignee TEXT` (nullable) a la tabla `tickets`.
- `POST /tickets` acepta un `assignee` opcional en el body; sin él, el ticket queda sin asignar (`null`).
- Se agrega un endpoint dedicado `POST /tickets/{id}/assign` para (re)asignar un ticket ya creado, en vez de un `PATCH /tickets/{id}` genérico (el proyecto no tiene ningún endpoint de actualización parcial genérica todavía, solo acciones puntuales como `close`).
- El front agrega un input de "Asignado a" (opcional) en el formulario de creación, muestra el assignee en cada card de ticket, y agrega un botón "Reasignar".

## Capabilities

### New Capabilities
- `ticket-assignment`: asignar y reasignar un responsable (`assignee`, texto libre) a un ticket, al crearlo o después.

## Impact

- Esquema: nueva columna `assignee` en `tickets` (`api/db.py`).
- DTOs: `assignee` opcional en `TicketCreateRequest`/`TicketResponse`; nuevo DTO `TicketAssignRequest` (`api/schemas/ticket.py`).
- Capas: `api/repositories/ticket_repository.py` (`create()` acepta `assignee`, nuevo método `assign()`), `api/services/ticket_service.py` (nuevo `assign_ticket()`), `api/controllers/ticket_controller.py` (incluir `assignee` en la respuesta, nuevo método `assign()`), `api/routes/tickets.py` (nueva ruta `POST /tickets/{id}/assign`).
- Front: `front/index.html` (input de assignee al crear, badge/texto de assignee en cada card, botón "Reasignar").
- Docs: `docs/architecture.md` y `docs/glossary.md` deben actualizarse para reflejar el campo `assignee` una vez implementado.

## Estado

**Sin implementar en `main`** — feature media, abierta, para practicar el ciclo research → plan → implementa → revisa diff en la jornada de capacitación. La solución de referencia existe en la rama `reference/tk-103` (no mirar antes de intentar el ejercicio). Este `proposal.md`/`design.md`/`tasks.md` documentan el plan completo (investigado contra la rama de referencia para que el ejemplo sea real, no inventado) — `notas.md` queda vacío para completarse en vivo durante la jornada.
