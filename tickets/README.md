# tickets/ (reemplazado por `openspec/changes/`)

> **Esta convención fue reemplazada.** La traza real de trabajo por ticket/change ahora vive en `openspec/changes/<ID>-<descripción>/` — ver `openspec/changes/README.md`.

## Por qué

Antes de este cambio, `tickets/<ID>/{research.md,plan.md,notas.md}` era una convención propia de este repo, sin conexión a ninguna herramienta real de spec-driven development. Se resolvió instalando OpenSpec real (`@fission-ai/openspec`) y migrando la traza de trabajo a `openspec/changes/`.

## Qué se conservó

- `notas.md` — lo único de esta convención que OpenSpec no tiene equivalente. Ahora es el quinto archivo de cada change en `openspec/changes/<ID>/notas.md` (extensión propia de este repo, documentada en `openspec/changes/README.md`).
- `research.md` y `plan.md` se cubren ahora con los artefactos reales de OpenSpec (`proposal.md`, `design.md`, `specs/`, `tasks.md`), generados con `/opsx:explore` + `/opsx:propose` en vez de copiarse a mano desde `_TEMPLATE/`.

## Dónde quedó cada ticket

- `TK-101/` (filtro por prioridad, ya implementado en `main`) → `openspec/changes/archive/2026-08-22-tk-101-priority-filter/`.
- `TK-102/` (bug de `/stats`, abierto) → `openspec/changes/tk-102-stats-bug/`.
- `TK-103/` (campo `assignee`, abierto) → `openspec/changes/tk-103-assignee/`.

## `TK-101/`, `TK-102/`, `TK-103/` y `_TEMPLATE/` se dejan intactas

No se borró nada de esta carpeta — queda como referencia histórica de cómo se veía la convención anterior. Para tickets/changes nuevos, arrancar directamente en `openspec/changes/` (ver `.claude/skills/ticket-scaffold/SKILL.md`, actualizado para generar la estructura nueva).
