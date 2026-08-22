# ai-workshop-sandbox

> Contexto para agentes de IA. Este archivo describe el proyecto REAL — no es una plantilla con placeholders. Léelo antes de tocar código.

## 1. Qué es este proyecto

Mini sistema de tickets internos (crear, listar, filtrar, cerrar) con API en FastAPI, front vanilla y persistencia en SQLite. Es el sandbox de una jornada de capacitación de desarrollo agéntico: se usa para practicar el ciclo research → plan → implementa → revisa diff sobre código real, no sobre un tutorial.

## 2. Estructura de Memoria Persistente (`docs/`)

- **Architecture** (`docs/architecture.md`): Stack real, estructura de carpetas, flujos de datos y lo que NO existe.
- **Conventions** (`docs/conventions.md`): Reglas de estilo, naming semántico, patrones aceptados y estrategia de tests.
- **Decisions** (`docs/adr/`): ADRs con decisiones aceptadas, razones, opciones descartadas y estado.
- **Glossary** (`docs/glossary.md`): Términos de dominio de tickets usados en este repo.
- **Workflow** (`docs/workflow.md`): Preparación de entorno, checklist pre-merge (Definition of Done) y deploy.
- **Errors** (`docs/errors.md`): Catálogo de errores conocidos, síntomas, causa raíz y soluciones probadas.

## 3. Reglas Duras de Ejecución

1. **Spec Antes del Código**: escribir `tickets/TK-XXX/research.md` y `plan.md` antes de modificar código. Ver `tickets/TK-101/` como ejemplo de ciclo completo ya recorrido.
2. **Cero Comentarios de WHAT**: solo comentar el WHY cuando la razón técnica no sea obvia.
3. **No relitigar ADRs**: respetar las decisiones en `docs/adr/` (ej. SQLite en vez de Postgres, repository pattern sin ORM).
4. **Verificación Empírica**: todo cambio debe pasar `pytest` en verde antes de dar la tarea por completada.
5. **No sobre-construir**: este proyecto es MVP a propósito. No agregar multi-tenant, roles, rate limiting real, CI/CD ni deploy — está fuera de scope salvo que un ticket lo pida explícitamente.

## 4. Tickets abiertos para practicar

- `tickets/TK-101/` — filtro por prioridad. Ciclo completo (research → plan → implementado → notas). Referencia de cómo se ve un ticket bien documentado.
- `tickets/TK-102/` — bug real y sin arreglar: `/stats` no descuenta los tickets cerrados del conteo de abiertos. Investigar antes de tocar código.
- `tickets/TK-103/` — feature media sin implementar: agregar campo `assignee` al ticket (modelo, servicio, front).

Las soluciones de referencia de TK-102 y TK-103 existen en las ramas `reference/tk-102` y `reference/tk-103` — no mirarlas antes de intentar el ejercicio.
