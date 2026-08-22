# Testing

## Cómo correr los tests

```bash
pytest
```

`pytest.ini` ya tiene `pythonpath = .` configurado — correr siempre desde la raíz del repo con el venv activado.

## Qué cubrir

- **Tests unitarios** (`tests/unit/`): `TicketRepository` contra SQLite en memoria (`:memory:`); `TicketService` contra un repositorio fake — no tocan la API HTTP.
- **Tests de integración** (`tests/integration/`): endpoints completos vía `TestClient`, con `X-API-Key` real y una base de datos temporal por test.

## Criterio de aceptación

- Ningún cambio se da por terminado si `pytest` no queda en verde.
- `main` siempre debe estar en verde — un change abierto con un bug conocido (ej. `tk-102-stats-bug`) no lleva un test rojo commiteado; el test que prueba el fix se agrega junto con el fix, en la rama o change que lo resuelve.
- Para un change de OpenSpec: además de `pytest` en verde, correr `openspec validate <ID> --strict` antes de considerarlo terminado.
