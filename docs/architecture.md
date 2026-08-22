# Arquitectura del Sistema

> Definición del stack, estructura de carpetas, flujos de datos y límites del sistema.

## 1. Stack Tecnológico

- **Lenguaje / Runtime**: Python 3.12
- **Framework Principal**: FastAPI
- **Base de Datos**: SQLite (archivo local, vía `sqlite3` estándar — sin ORM, ver `docs/adr/0002-sqlite-sin-orm.md`)
- **Front**: HTML + JS vanilla, sin build step (`front/index.html`)
- **Tests**: pytest + `fastapi.testclient.TestClient`
- **Infraestructura**: Docker opcional (`Dockerfile` + `docker-compose.yml`). La vía principal es correr con `uvicorn` directo.

## 2. Estructura de Carpetas

```
api/
├── main.py               # Punto de entrada FastAPI, wiring de routers, logging, startup
├── config.py             # Settings (API_KEY, DATABASE_PATH, LOG_LEVEL) desde variables de entorno
├── logging_config.py     # Logging estructurado JSON a stdout
├── db.py                 # Conexión SQLite + schema + init_db()
├── dependencies.py       # DI: require_api_key, get_ticket_controller
├── schemas/               # DTOs Pydantic de entrada/salida (TicketCreateRequest, TicketResponse, StatsResponse)
├── repositories/          # Acceso a SQLite (TicketRepository) — única capa que ejecuta SQL
├── services/              # Lógica de negocio pura (TicketService)
├── controllers/           # Traduce entre DTOs de API y servicios (TicketController)
└── routes/                # Routers FastAPI (tickets, health, stats) — sin lógica de negocio
front/
└── index.html             # UI única: listar, filtrar por prioridad, crear, cerrar tickets
tests/
├── unit/                  # TicketRepository (SQLite en memoria) y TicketService (repo fake)
└── integration/           # Endpoints vía TestClient
```

## 3. Flujos de Datos Principales

1. **Cliente → Router**: FastAPI valida el DTO de entrada (Pydantic) y exige header `X-API-Key`.
2. **Router → Controller**: el router solo resuelve dependencias e invoca al controller.
3. **Controller → Service**: el controller traduce entre DTO/HTTP y llamadas al servicio, y convierte filas de SQLite a `TicketResponse`.
4. **Service → Repository**: el servicio aplica reglas de negocio (ej. no cerrar un ticket inexistente) y delega el acceso a datos al repositorio.
5. **Repository → SQLite**: única capa que conoce SQL. Devuelve `sqlite3.Row`, nunca DTOs.

## 4. Dominio: Ticket

Campos (rama `reference/tk-103`, con TK-103 ya resuelto): `id`, `title`, `description`, `priority` (`low`/`medium`/`high`), `status` (`open`/`closed`), `assignee` (`str | None`), `created_at`.

`assignee` se puede fijar al crear el ticket (`POST /tickets`) o cambiar después vía `POST /tickets/{id}/assign`. En `main` este campo todavía no existe — este es precisamente el alcance de TK-103.

## 5. Lo que NO existe (Límites Duros contra Alucinaciones)

- NO hay ORM (SQLAlchemy, Prisma, etc.) — SQL crudo vía `sqlite3` en `api/repositories/`.
- NO hay Postgres, Redis, ni ninguna otra base de datos — solo SQLite local.
- NO hay autenticación de usuarios ni roles — solo `X-API-Key` fijo por variable de entorno. `assignee` es un texto libre, no una referencia a un usuario real.
- NO hay multi-tenant.
- NO hay CI/CD, IaC ni deploy a la nube — el proyecto corre local (Python directo o Docker Compose).
- NO hay build step en el front (nada de React/Vite/webpack).
