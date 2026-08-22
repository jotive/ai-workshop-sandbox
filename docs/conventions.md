# Convenciones de Código y Estándares

> Guía de estilo, naming semántico, patrones aceptados y estrategia de pruebas para `ai-workshop-sandbox`.

## 1. Estilo de Código

- Código **limpio, declarativo**, en inglés (identificadores, mensajes de error, docstrings si las hubiera).
- **Cero comentarios de WHAT** (ej. `# increment counter`). Solo comentarios de WHY cuando la razón de negocio o técnica no sea obvia.
- Control de flujo plano: *early returns* en vez de `if/else` anidados.
- Naming semántico: `ticket_repository.find_by_id`, no `repo.get(x)`.

## 2. Naming Semántico

- **Variables y funciones**: nombres expresivos (`close_ticket`, `count_open`, no `do_stuff`).
- **DTOs (Pydantic)**: nombres centrados en el dominio (`TicketCreateRequest`, `TicketResponse`, `StatsResponse`).
- **Archivos**: `snake_case.py`.

## 3. Patrones Aceptados

- **Repository Pattern**: toda interacción con SQLite pasa por `api/repositories/ticket_repository.py`. Ninguna otra capa ejecuta SQL.
- **Dependency Injection**: `api/dependencies.py` construye `TicketService`/`TicketController` por request vía `Depends`. No instanciar servicios a mano dentro de un route handler.
- **DTO Validation**: toda entrada de la API se valida con Pydantic (`api/schemas/ticket.py`) antes de llegar al controller.

## 4. Estrategia de Testing

- **Tests unitarios** (`tests/unit/`): `TicketRepository` contra SQLite en memoria (`:memory:`); `TicketService` contra un repositorio fake — no tocan la API HTTP.
- **Tests de integración** (`tests/integration/`): endpoints completos vía `TestClient`, con `X-API-Key` real y una base de datos temporal por test.
- **Criterio de aceptación**: ningún cambio se da por terminado si `pytest` no queda en verde. `main` siempre debe estar en verde — un ticket abierto con un bug conocido (ej. TK-102) no lleva un test rojo commiteado; el test que prueba el fix se agrega junto con el fix, en la rama que lo resuelve.
