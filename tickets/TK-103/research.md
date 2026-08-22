# Research — TK-103

> Volcado del agente en modo solo-lectura. Qué existe hoy, qué toca, qué no se sabe todavía.

## Qué se pidió

"Necesito poder asignarle un responsable a cada ticket, tanto al crearlo como después si cambia de dueño."

## Qué existe hoy (relevante a este cambio)

- Tabla `tickets` (`api/db.py::SCHEMA`): `id, title, description, priority, status, created_at`. No hay columna `assignee`.
- `TicketCreateRequest` / `TicketResponse` (`api/schemas/ticket.py`) no tienen campo `assignee`.
- `TicketRepository.create()` (`api/repositories/ticket_repository.py`) inserta con un `INSERT` fijo de 5 columnas — hay que agregar la sexta.
- No existe ningún endpoint para actualizar campos de un ticket ya creado más allá de `POST /tickets/{id}/close` — el patrón de "acción sobre un ticket existente" (buscar por id, 404 si no existe, delegar al repositorio) ya está resuelto en `TicketService.close_ticket()` / `TicketController.close()` / `api/routes/tickets.py::close_ticket`, así que agregar `assign` puede seguir exactamente ese mismo patrón.
- `front/index.html` no tiene ningún campo ni control relacionado a asignación.

## Preguntas abiertas / [unknown]

- Si `assignee` debería validarse contra una lista cerrada de personas del equipo — se asume que no: el dominio no tiene entidad "usuario", es texto libre. Si esto se pidiera más adelante, ameritaría un ADR nuevo (ya que hoy `docs/architecture.md` dice explícitamente "NO hay autenticación de usuarios ni roles").
- Si reasignar un ticket ya cerrado debería estar permitido — se asume que sí (reasignar no cambia el `status`), porque no se pidió lo contrario y bloquearlo sería una regla de negocio inventada sin fuente.
