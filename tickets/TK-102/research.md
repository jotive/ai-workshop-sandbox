# Research — TK-102

> Volcado del agente en modo solo-lectura. Qué existe hoy, qué toca, qué no se sabe todavía.

## Qué se pidió

"El dashboard de `/stats` dice que tengo 8 tickets abiertos pero en el listado solo veo 3 sin cerrar — algo está mal en el conteo."

## Qué existe hoy (relevante a este cambio)

- `GET /stats` (`api/routes/stats.py`) devuelve `TicketController.stats()` → `TicketService.get_stats()` (`api/services/ticket_service.py`), que arma un `StatsResponse(total=..., open=..., closed=...)`.
- `TicketRepository.count_total()` (`api/repositories/ticket_repository.py`): `SELECT COUNT(*) FROM tickets` — correcto, cuenta todo.
- `TicketRepository.count_closed()`: `SELECT COUNT(*) FROM tickets WHERE status = 'closed'` — correcto.
- `TicketRepository.count_open()`: **`SELECT COUNT(*) FROM tickets`** — la misma query que `count_total()`, sin filtrar por `status = 'open'`. Este es el bug: nunca descuenta los tickets cerrados, así que `open` siempre es igual a `total`.
- No hay ningún test que cubra `count_open()` — ni en `tests/unit/test_ticket_repository.py` ni en `tests/integration/test_tickets_api.py` — por eso el bug pasó a `main` sin que la suite lo agarrara.

## Preguntas abiertas / [unknown]

- Ninguna — el bug es reproducible leyendo el código, no depende de datos externos ni de configuración.
