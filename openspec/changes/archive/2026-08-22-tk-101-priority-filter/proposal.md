## Why

En el listado de tickets, el usuario tiene que scrollear todo el listado cuando solo le importan los tickets `high`. Se pidió: "En el listado de tickets quiero poder filtrar por prioridad, para no tener que scrollear todo cuando solo me importan los `high`."

## What Changes

- `GET /tickets` acepta un query param opcional `priority` (`low`/`medium`/`high`). Sin el param, devuelve todos los tickets (comportamiento actual sin cambios).
- El front (`front/index.html`) agrega un `<select>` de filtro por prioridad sobre el listado, que dispara un nuevo fetch a `/tickets?priority=<valor>` al cambiar, sin recargar la página.
- Sin cambios de esquema de datos: `TicketRepository.find_all()` ya soportaba el parámetro `priority` desde que se escribió el repositorio inicial — solo faltaba conectar router → controller → front.

## Capabilities

### New Capabilities
- `priority-filter`: filtrar el listado de tickets por prioridad vía query param en `GET /tickets`, con control equivalente en el front.

### Modified Capabilities
<!-- ninguna: no se toca el contrato de otros endpoints -->

## Impact

- Archivos tocados: `api/routes/tickets.py`, `api/controllers/ticket_controller.py`, `front/index.html`, `tests/integration/test_tickets_api.py`.
- Sin cambios en `api/repositories/ticket_repository.py` (ya soportaba el filtro) ni en el esquema de la tabla `tickets`.
- Sin impacto en `POST /tickets`, `POST /tickets/{id}/close` ni `GET /stats`.

## Estado

Ya implementado y mergeado en `main` (era `tickets/TK-101/`, convención reemplazada por este change de OpenSpec — ver `openspec/changes/README.md`). Este change se archiva inmediatamente después de crearse, como traza retroactiva del trabajo ya hecho.
