# Roadmap — ai-workshop-sandbox

> Estado real del proyecto de práctica. No es un roadmap de producto — es el estado de los tickets/changes de la jornada de capacitación.

## Ahora

- Mantener `main` en verde (`pytest` sin romperse) mientras se usa como base de la jornada de capacitación.

## Siguiente

- `openspec/changes/tk-102-stats-bug/` — bug real de `/stats` (no descuenta tickets cerrados del conteo de abiertos). Plan completo y validado, sin implementar en `main`. Para practicar en vivo.
- `openspec/changes/tk-103-assignee/` — agregar campo `assignee` al ticket (modelo, servicio, front). Plan completo y validado, sin implementar en `main`. Para practicar en vivo.

## Después (con bloqueador)

- Filtrar el listado por `assignee` (análogo a TK-101 con `priority`) — bloqueado por: depende de que TK-103 esté implementado en `main` primero.
- Endpoint de actualización parcial genérico (`PATCH /tickets/{id}`) — bloqueado por: solo se justifica si aparecen más campos editables además de `assignee` (ver `openspec/changes/tk-103-assignee/design.md`, decisión de no construirlo todavía).

## Hecho

- TK-101 (filtro por prioridad en el listado) — implementado, mergeado en `main`, archivado en `openspec/changes/archive/2026-08-22-tk-101-priority-filter/`.
- Migración de `tickets/<ID>/` a OpenSpec real (`@fission-ai/openspec`) — ver `openspec/changes/README.md` y `tickets/README.md`.
- Reestructuración de `docs/` al estándar de handbook (`docs/handbook/`, `docs/onboarding.md`, `docs/HANDBOOK.md`, `docs/ROADMAP.md`).
