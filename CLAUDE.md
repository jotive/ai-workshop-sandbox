# ai-workshop-sandbox

> Contexto para agentes de IA. Este archivo describe el proyecto REAL — no es una plantilla con placeholders. Léelo antes de tocar código.

## 1. Qué es este proyecto

Mini sistema de tickets internos (crear, listar, filtrar, cerrar) con API en FastAPI, front vanilla y persistencia en SQLite. Es el sandbox de una jornada de capacitación de desarrollo agéntico: se usa para practicar el ciclo research → plan → implementa → revisa diff sobre código real, no sobre un tutorial.

## 2. Estructura de Memoria Persistente (`docs/`)

- **Handbook** (`docs/handbook/`): toda la documentación consolidada, se carga bajo demanda — `architecture.md`, `conventions.md`, `decisions.md`, `glossary.md`, `workflow.md`, `development.md`, `git-workflow.md`, `testing.md`, `releases.md`, `errors.md`, `ai-agents.md`. Índice en `docs/HANDBOOK.md`.
- **Decisions** (`docs/adr/`): ADRs con decisiones aceptadas, razones, opciones descartadas y estado (detalle largo; `docs/handbook/decisions.md` es el índice rápido).
- **Onboarding** (`docs/onboarding.md`): cómo arranca alguien nuevo (humano o agente) en este repo.
- **Roadmap** (`docs/ROADMAP.md`): ahora · siguiente · después (con bloqueador) · hecho.

## 3. Reglas Duras de Ejecución

1. **Spec Antes del Código**: cada change vive en `openspec/changes/<ID>/{proposal.md, design.md, tasks.md, specs/}` — se revisan ANTES de modificar código (convención `tickets/TK-XXX/` reemplazada, ver `tickets/README.md`). Ver `openspec/changes/archive/2026-08-22-tk-101-priority-filter/` como ejemplo de ciclo completo ya recorrido.
2. **Cero Comentarios de WHAT**: solo comentar el WHY cuando la razón técnica no sea obvia.
3. **No relitigar ADRs**: respetar las decisiones en `docs/adr/` (ej. SQLite en vez de Postgres, repository pattern sin ORM; índice rápido en `docs/handbook/decisions.md`).
4. **Verificación Empírica**: todo cambio debe pasar `pytest` en verde antes de dar la tarea por completada.
5. **No sobre-construir**: este proyecto es MVP a propósito. No agregar multi-tenant, roles, rate limiting real, CI/CD ni deploy — está fuera de scope salvo que un change lo pida explícitamente.

## 4. Changes abiertos para practicar

- `openspec/changes/archive/2026-08-22-tk-101-priority-filter/` — filtro por prioridad. Ciclo completo (proposal → design → tasks → notas) ya recorrido e implementado. Referencia de cómo se ve un change bien documentado.
- `openspec/changes/tk-102-stats-bug/` — bug real y sin arreglar: `/stats` no descuenta los tickets cerrados del conteo de abiertos. Plan completo, `notas.md` vacío para completar en vivo.
- `openspec/changes/tk-103-assignee/` — feature media sin implementar: agregar campo `assignee` al ticket (modelo, servicio, front). Plan completo, `notas.md` vacío para completar en vivo.

Las soluciones de referencia de TK-102 y TK-103 existen en las ramas `reference/tk-102` y `reference/tk-103` (cada una con su propio `openspec/changes/archive/` reflejando el estado resuelto) — no mirarlas antes de intentar el ejercicio.
