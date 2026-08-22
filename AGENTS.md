# Contexto Universal de IA del Proyecto (AGENTS.md)

> Fuente de verdad de arquitectura e instrucciones para asistentes de código (Claude Code, Codex CLI, Cursor, Gemini, Copilot, Windsurf) sobre `ai-workshop-sandbox`: mini sistema de tickets internos (FastAPI + SQLite + front vanilla).

## 1. Memoria Operacional Persistente (`docs/`)

Toda la especificación técnica y de negocio vive en `docs/` en Markdown:

- **Arquitectura (`docs/architecture.md`)**: Stack, estructura de carpetas, flujos de datos y lo que NO existe.
- **Convenciones (`docs/conventions.md`)**: Reglas de estilo, naming semántico, patrones aceptados y estrategia de tests.
- **Decisiones / ADRs (`docs/adr/`)**: Decisiones de arquitectura aceptadas, razones, opciones descartadas y estado.
- **Glosario (`docs/glossary.md`)**: Términos del dominio de tickets usados en este repo.
- **Workflow (`docs/workflow.md`)**: Preparación de entorno, checklist pre-merge (Definition of Done) y deploy.
- **Errores (`docs/errors.md`)**: Catálogo de errores conocidos, síntomas, causa raíz y soluciones probadas.

## 2. Protocolo de Trabajo por Ticket (RPI + SDD)

1. **Research**: extraer hallazgos a `tickets/TK-XXX/research.md` antes de escribir código — qué existe hoy, qué toca, qué queda como `[unknown]`.
2. **Plan (Spec)**: escribir o revisar la spec en `tickets/TK-XXX/plan.md`. Se revisa ANTES de implementar.
3. **Implement**: implementar contra la spec, verificar diff línea a línea y ejecutar `pytest` en verde.
4. **Notas**: registrar en `tickets/TK-XXX/notas.md` cualquier decisión que se haya desviado del plan original, y por qué.

## 3. Reglas duras de este repo

- API en `api/`, capas separadas: `routes` → `controllers` → `services` → `repositories`. No saltarse capas.
- DTOs de entrada/salida con Pydantic en `api/schemas/`. Nada de dicts sueltos cruzando capas.
- Persistencia: SQLite vía `sqlite3` estándar, sin ORM (ver `docs/adr/0002-sqlite-sin-orm.md`). No agregar SQLAlchemy/Postgres sin discutirlo primero.
- Auth simple por header `X-API-Key` contra `docs/architecture.md` — no hay usuarios ni roles.
- Tests con `pytest`: unitarios para `services`/`repositories`, integración para endpoints con `TestClient`.
- Front en `front/index.html`: HTML+JS vanilla sin build step. No introducir React/Vite/npm para esto.
