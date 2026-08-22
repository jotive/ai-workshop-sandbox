## Context

`GET /stats` (`api/routes/stats.py`) devuelve `TicketController.stats()` → `TicketService.get_stats()` (`api/services/ticket_service.py`), que arma un `StatsResponse(total=..., open=..., closed=...)` a partir de tres métodos del repositorio:

- `TicketRepository.count_total()`: `SELECT COUNT(*) FROM tickets` — correcto, cuenta todo.
- `TicketRepository.count_closed()`: `SELECT COUNT(*) FROM tickets WHERE status = 'closed'` — correcto.
- `TicketRepository.count_open()` (antes del fix): `SELECT COUNT(*) FROM tickets` — la misma query que `count_total()`, sin filtrar por `status = 'open'`. Ese era el bug.

No había ningún test que cubriera `count_open()` — por eso el bug pasó a `main` sin que la suite lo agarrara.

## Goals / Non-Goals

**Goals:**
- Corregir `count_open()` para que filtre por `status = 'open'`, siguiendo exactamente el mismo patrón que `count_closed()`.
- Cubrir el fix con un test unitario (capa de datos aislada) y uno de integración (contrato HTTP de `/stats`).

**Non-Goals:**
- Agregar más desgloses a `/stats` (por prioridad, por fecha, etc.).
- Tocar `count_total()` o `count_closed()`.

## Decisions

- **Fix de una sola query, sin refactor mayor**: `count_open()` ahora hace `SELECT COUNT(*) AS count FROM tickets WHERE status = ?` con `TicketStatus.OPEN.value`, igual que `count_closed()`. Alternativa descartada: calcular `open` como `total - closed` en la capa de servicio — se descartó porque rompe la simetría con `count_closed()` y mueve lógica de conteo fuera del repositorio.
- **Dos tests, no uno**: unitario en `tests/unit/test_ticket_repository.py` + integración en `tests/integration/test_tickets_api.py`. El fix fue de una sola línea de intención, pero se agregaron dos tests porque el síntoma original lo reportó alguien mirando el endpoint, no el código — no alcanzaba con cubrirlo solo a nivel unitario.

## Risks / Trade-offs

- [Riesgo] Ninguno significativo — fix acotado a una función pura de conteo, sin cambios de esquema ni de contrato de API.
