# Git workflow

> Este repo no tiene remoto (`git remote -v` vacío) — todo el trabajo queda local. No hay flujo de PR real; esta convención describe cómo se usan las ramas para la jornada de capacitación.

## Ramas de este repo

- `main` — proyecto base + TK-101 (filtro por prioridad) ya implementado y archivado en `openspec/changes/archive/`. TK-102 (bug de `/stats`) y TK-103 (campo `assignee`) quedan abiertos en `openspec/changes/` para practicar en vivo.
- `reference/tk-102`, `reference/tk-103` — soluciones de referencia de esos dos changes, ya implementadas pero sin mergear a `main`. Cada una tiene su propio `openspec/changes/archive/<fecha>-<ID>/` reflejando el estado ya resuelto, para mostrar el before/after real. No mirar antes de intentar el ejercicio.
- `bench-claude`, `bench-codex` — ramas vacías para comparar Claude Code vs Codex CLI resolviendo el mismo ticket en vivo.

## Cuándo hacer commit

- Un commit por change completo (o por tarea de `tasks.md` si el change es grande) — no un commit gigante al final.
- Mensaje de commit describe el *qué* del cambio en un renglón (ej. `TK-102: fix /stats not discounting closed tickets from open count`), siguiendo el patrón ya usado en el historial de este repo.

## Cuándo hacer PR

No aplica — este repo no tiene remoto ni flujo de revisión por PR. La "revisión" es la fase Verify del ciclo (diff línea a línea + `pytest` en verde + `openspec validate <ID> --strict`), documentada en `docs/handbook/ai-agents.md`.
