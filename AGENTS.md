# Contexto Universal de IA del Proyecto (AGENTS.md)

> Fuente de verdad de arquitectura e instrucciones para asistentes de código (Claude Code, Codex CLI, Cursor, Gemini, Copilot, Windsurf) sobre `ai-workshop-sandbox`: mini sistema de tickets internos (FastAPI + SQLite + front vanilla).

## 0. Índice rápido

- `ROADMAP.md` — ahora · siguiente · después (con bloqueador) · hecho.
- `HANDBOOK.md` — índice a `docs/handbook/*` (contenido operativo bajo demanda).
- `docs/onboarding.md` — cómo arranca alguien nuevo (humano o agente) en este repo.

## 1. Memoria Operacional Persistente (`docs/`)

Toda la especificación técnica y de negocio vive en `docs/` en Markdown:

- **Arquitectura (`docs/architecture.md`)**: Stack, estructura de carpetas, flujos de datos y lo que NO existe.
- **Convenciones (`docs/conventions.md`)**: Reglas de estilo, naming semántico, patrones aceptados y estrategia de tests.
- **Decisiones / ADRs (`docs/adr/`)**: Decisiones de arquitectura aceptadas, razones, opciones descartadas y estado.
- **Glosario (`docs/glossary.md`)**: Términos del dominio de tickets usados en este repo.
- **Handbook (`docs/handbook/`)**: contenido operativo que se carga bajo demanda — `development.md`, `git-workflow.md`, `testing.md`, `releases.md`, `errors.md`, `ai-agents.md`. Índice en `HANDBOOK.md` (raíz). `docs/workflow.md` y `docs/errors.md` quedaron como stubs de deprecación apuntando acá.

## 2. Protocolo de Trabajo por Change (RPI + SDD, con OpenSpec real)

Este repo usa `@fission-ai/openspec` real — la convención vieja en `tickets/<ID>/{research.md,plan.md,notas.md}` fue reemplazada (ver `tickets/README.md`). Detalle completo en `docs/handbook/ai-agents.md`; resumen:

1. **Research**: explorar el problema antes de escribir código — qué existe hoy, qué toca, qué queda como `[unknown]`.
2. **Plan (Spec)**: `openspec/changes/<ID>/{proposal.md, design.md, tasks.md, specs/}` — se revisan ANTES de implementar.
3. **Implement**: implementar contra `tasks.md`, verificar diff línea a línea y ejecutar `pytest` en verde.
4. **Notas**: registrar en `openspec/changes/<ID>/notas.md` (quinto archivo, extensión propia de este repo, NO es parte de OpenSpec) cualquier decisión que se haya desviado del plan original, y por qué.
5. **Verify**: `openspec validate <ID> --strict` antes de dar el change por terminado. `openspec archive <ID>` al completarlo.

## 3. Reglas duras de este repo

- API en `api/`, capas separadas: `routes` → `controllers` → `services` → `repositories`. No saltarse capas.
- DTOs de entrada/salida con Pydantic en `api/schemas/`. Nada de dicts sueltos cruzando capas.
- Persistencia: SQLite vía `sqlite3` estándar, sin ORM (ver `docs/adr/0002-sqlite-sin-orm.md`). No agregar SQLAlchemy/Postgres sin discutirlo primero.
- Auth simple por header `X-API-Key` contra `docs/architecture.md` — no hay usuarios ni roles.
- Tests con `pytest`: unitarios para `services`/`repositories`, integración para endpoints con `TestClient`.
- Front en `front/index.html`: HTML+JS vanilla sin build step. No introducir React/Vite/npm para esto.
