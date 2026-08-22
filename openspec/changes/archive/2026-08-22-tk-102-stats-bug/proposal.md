## Why

Reporte real: "El dashboard de `/stats` dice que tengo 8 tickets abiertos pero en el listado solo veo 3 sin cerrar — algo está mal en el conteo." El endpoint `GET /stats` nunca descontaba los tickets cerrados del conteo de `open`, así que `open` siempre quedaba igual a `total`.

## What Changes

- `TicketRepository.count_open()` (`api/repositories/ticket_repository.py`) deja de contar todos los tickets y empieza a filtrar por `status = 'open'`, siguiendo el mismo patrón que `count_closed()`.
- Se agregan tests unitario y de integración que cubren el fix.

## Capabilities

### New Capabilities
- `ticket-stats`: `GET /stats` reporta el conteo de tickets por estado (`total`, `open`, `closed`), con `open` calculado como los tickets con `status == "open"`, no como el total de tickets. Primera vez que esta capability se documenta como spec en esta rama (no existía `openspec/specs/ticket-stats/` antes de este change).

## Impact

- Archivo tocado: `api/repositories/ticket_repository.py` (una función, `count_open()`).
- Tests nuevos en `tests/unit/test_ticket_repository.py`, `tests/unit/test_ticket_service.py` (fake repo actualizado) y `tests/integration/test_tickets_api.py`.
- Sin impacto en `count_total()` ni `count_closed()`.

## Estado

**Implementado en esta rama** (`reference/tk-102`) — solución de referencia para el ejercicio de la jornada de capacitación. `main` sigue con el bug sin arreglar (ver `openspec/changes/tk-102-stats-bug/` en `main`, abierto). Este change se archiva inmediatamente después de escribirse, como traza retroactiva del fix ya aplicado en esta rama.
