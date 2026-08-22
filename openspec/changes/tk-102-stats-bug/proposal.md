## Why

Reporte real: "El dashboard de `/stats` dice que tengo 8 tickets abiertos pero en el listado solo veo 3 sin cerrar — algo está mal en el conteo." El endpoint `GET /stats` nunca descuenta los tickets cerrados del conteo de `open`, así que `open` siempre queda igual a `total`.

## What Changes

- `TicketRepository.count_open()` (`api/repositories/ticket_repository.py`) deja de contar todos los tickets y empieza a filtrar por `status = 'open'`, siguiendo el mismo patrón que `count_closed()`.
- Se agregan tests unitario y de integración que cubren el fix — hoy no existe ningún test que ejercite `count_open()` aislado del resto, por eso el bug llegó a `main` sin que la suite lo agarrara.

## Capabilities

### Modified Capabilities
- `ticket-stats`: `GET /stats` debe reportar `open` como los tickets con `status == "open"`, no como el total de tickets.

## Impact

- Archivo tocado: `api/repositories/ticket_repository.py` (una función, `count_open()`).
- Tests nuevos en `tests/unit/test_ticket_repository.py` y `tests/integration/test_tickets_api.py`.
- Sin impacto en `count_total()` ni `count_closed()` — ya funcionan bien, el bug es solo en `count_open()`.

## Estado

**Sin implementar en `main`** — bug real, abierto, para practicar el ciclo research → plan → implementa → revisa diff en la jornada de capacitación. La solución de referencia existe en la rama `reference/tk-102` (no mirar antes de intentar el ejercicio). Este `proposal.md`/`design.md`/`tasks.md` documentan el plan completo (investigado contra la rama de referencia para que el ejemplo sea real, no inventado) — `notas.md` queda vacío para completarse en vivo durante la jornada.
