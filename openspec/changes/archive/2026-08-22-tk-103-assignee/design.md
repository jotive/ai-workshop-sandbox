## Context

Estado antes de este change: tabla `tickets` sin columna `assignee`; `TicketCreateRequest`/`TicketResponse` sin el campo; no existía ningún endpoint para actualizar campos de un ticket ya creado más allá de `POST /tickets/{id}/close` — el patrón de "acción sobre un ticket existente" (buscar por id, 404 si no existe, delegar al repositorio) ya estaba resuelto en `TicketService.close_ticket()` / `TicketController.close()` / `api/routes/tickets.py::close_ticket`, así que `assign` siguió exactamente ese mismo patrón.

## Goals / Non-Goals

**Goals:**
- `assignee` opcional al crear, editable después vía un endpoint dedicado.
- Reusar el patrón ya existente de "acción sobre ticket existente con 404 si no existe" (`close_ticket`).

**Non-Goals:**
- Entidad "usuario" o autenticación por persona.
- Notificar al assignee (email, webhook, etc.).
- Filtrar el listado por assignee (como TK-101 hizo con prioridad).

## Decisions

- **Endpoint dedicado `POST /tickets/{id}/assign` en vez de `PATCH /tickets/{id}` genérico**: el proyecto no tenía ningún endpoint de actualización parcial genérica todavía (solo acciones puntuales como `close`), y agregar un `PATCH` genérico hubiera sido sobre-construir para una sola necesidad.
- **`TicketAssignRequest.assignee` es obligatorio y no vacío (`min_length=1`) a propósito**: "reasignar a nadie" no se pidió; si se necesitara "desasignar" sería un caso de uso distinto y explícito.
- **`assignee` no se valida contra una lista cerrada de personas del equipo**: el dominio no tiene entidad "usuario". Si esto se pidiera más adelante, ameritaría un ADR nuevo.
- **Reasignar un ticket cerrado está permitido**: reasignar no cambia el `status`, y no se pidió lo contrario.

## Risks / Trade-offs

- [Riesgo] Migración de esquema en una tabla ya poblada — mitigado porque `assignee` es `NULL`able y `api/db.py::init_db()` usa `CREATE TABLE IF NOT EXISTS`.
