## Context

Ver `proposal.md` - Why. `GET /stats` (`api/routes/stats.py`) devuelve `TicketController.stats()` → `TicketService.get_stats()` (`api/services/ticket_service.py`), que arma un `StatsResponse(total=..., open=..., closed=...)` a partir de tres métodos del repositorio:

- `TicketRepository.count_total()`: `SELECT COUNT(*) FROM tickets` — correcto, cuenta todo.
- `TicketRepository.count_closed()`: `SELECT COUNT(*) FROM tickets WHERE status = 'closed'` — correcto.
- `TicketRepository.count_open()`: **`SELECT COUNT(*) FROM tickets`** — la misma query que `count_total()`, sin filtrar por `status = 'open'`. Este es el bug: nunca descuenta los tickets cerrados, así que `open` siempre es igual a `total`.

No hay ningún test que cubra `count_open()` — ni en `tests/unit/test_ticket_repository.py` ni en `tests/integration/test_tickets_api.py` — por eso el bug pasó a `main` sin que la suite lo agarrara.

## Goals / Non-Goals

**Goals:**
- Corregir `count_open()` para que filtre por `status = 'open'`, siguiendo exactamente el mismo patrón que `count_closed()`.
- Cubrir el fix con un test unitario (capa de datos aislada) y uno de integración (contrato HTTP de `/stats`), no solo uno de los dos — el síntoma original lo reportó alguien mirando el endpoint, no el código.

**Non-Goals:**
- Agregar más desgloses a `/stats` (por prioridad, por fecha, etc.) — no se pidió, es scope de un change aparte.
- Tocar `count_total()` o `count_closed()` — ya funcionan bien, el bug es solo en `count_open()`.

## Decisions

- **Fix de una sola query, sin refactor mayor**: cambiar `count_open()` a `SELECT COUNT(*) AS count FROM tickets WHERE status = ?` con `TicketStatus.OPEN.value`, igual que `count_closed()`. Alternativa descartada: calcular `open` como `total - closed` en la capa de servicio en vez de una query dedicada — se descartó porque rompe la simetría con `count_closed()` y mueve lógica de conteo fuera del repositorio, que es la única capa que debe conocer SQL (ver `docs/conventions.md`).
- **Dos tests, no uno**: unitario en `tests/unit/test_ticket_repository.py` (crea un ticket abierto y uno cerrado, verifica que `count_open()` devuelve 1) + integración en `tests/integration/test_tickets_api.py` (crea dos tickets, cierra uno, verifica `GET /stats` completo). El unitario prueba la capa de datos aislada; el de integración prueba que el contrato HTTP también refleja el fix.

## Risks / Trade-offs

- [Riesgo] Ninguno significativo — es un fix acotado a una función pura de conteo, sin cambios de esquema ni de contrato de API (el shape de `StatsResponse` no cambia, solo el valor calculado).
