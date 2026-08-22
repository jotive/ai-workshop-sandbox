## Context

Ver `proposal.md` - Why. Estado actual (`main`):

- Tabla `tickets` (`api/db.py::SCHEMA`): `id, title, description, priority, status, created_at`. No hay columna `assignee`.
- `TicketCreateRequest` / `TicketResponse` (`api/schemas/ticket.py`) no tienen campo `assignee`.
- `TicketRepository.create()` inserta con un `INSERT` fijo de 5 columnas — hay que agregar la sexta.
- No existe ningún endpoint para actualizar campos de un ticket ya creado más allá de `POST /tickets/{id}/close` — el patrón de "acción sobre un ticket existente" (buscar por id, 404 si no existe, delegar al repositorio) ya está resuelto en `TicketService.close_ticket()` / `TicketController.close()` / `api/routes/tickets.py::close_ticket`, así que `assign` puede seguir exactamente ese mismo patrón.
- `front/index.html` no tiene ningún campo ni control relacionado a asignación.

## Goals / Non-Goals

**Goals:**
- `assignee` opcional al crear, editable después vía un endpoint dedicado.
- Reusar el patrón ya existente de "acción sobre ticket existente con 404 si no existe" (`close_ticket`), no inventar uno nuevo.

**Non-Goals:**
- Entidad "usuario" o autenticación por persona — `assignee` sigue siendo texto libre, no una referencia a una tabla de usuarios.
- Notificar al assignee (email, webhook, etc.) — no se pidió.
- Filtrar el listado por assignee (como TK-101 hizo con prioridad) — es un change aparte si se necesita.

## Decisions

- **Endpoint dedicado `POST /tickets/{id}/assign` en vez de `PATCH /tickets/{id}` genérico**: el proyecto no tiene ningún endpoint de actualización parcial genérica todavía (solo acciones puntuales como `close`), y agregar un `PATCH` genérico hoy sería sobre-construir para una sola necesidad. Si en el futuro aparecen más campos editables, ahí sí se justifica reconsiderar un `PATCH` genérico — no antes.
- **`TicketAssignRequest.assignee` es obligatorio y no vacío (`min_length=1`) a propósito**: "reasignar a nadie" no se pidió, y si se necesitara "desasignar" sería un caso de uso distinto y explícito, no un efecto secundario de mandar un string vacío.
- **`assignee` no se valida contra una lista cerrada de personas del equipo**: el dominio no tiene entidad "usuario" (ver `docs/architecture.md`, "NO hay autenticación de usuarios ni roles"). Si esto se pidiera más adelante, ameritaría un ADR nuevo — no se resuelve de forma implícita en este change.
- **Reasignar un ticket cerrado está permitido**: reasignar no cambia el `status`, y no se pidió lo contrario. Bloquearlo sería una regla de negocio inventada sin fuente.

## Risks / Trade-offs

- [Riesgo] Migración de esquema en una tabla ya poblada — mitigado porque `assignee` es `NULL`able y `api/db.py::init_db()` usa `CREATE TABLE IF NOT EXISTS` (no hay filas existentes en el sandbox de práctica que necesiten backfill real; si las hubiera, todas quedarían con `assignee = NULL`, que es el valor por default esperado).
