# openspec/changes/

Acá vive la traza real de trabajo de este repo — reemplaza lo que antes era `tickets/<ID>/` (ver `tickets/README.md`, que ahora solo apunta acá).

## Cómo usar

1. `openspec new change <ID>-<descripción-corta>` (usa el ID que ya existe en el sistema de tickets del equipo — Jira, Linear, GitHub Issues — igual que antes; no se inventa uno nuevo). Esto crea `openspec/changes/<ID>-<descripción-corta>/` con `.openspec.yaml` — nunca crear la carpeta a mano, el CLI genera metadata que los demás comandos necesitan.
2. Dentro de Claude Code: `/opsx:explore` (Research, opcional) y `/opsx:propose "<descripción>"` (Plan) generan los 4 artefactos reales de OpenSpec:
   - `proposal.md` — qué y por qué.
   - `design.md` — cómo (decisiones técnicas, alternativas descartadas, riesgos).
   - `tasks.md` — checklist de implementación, trackeable con checkboxes.
   - `specs/<capability-path>/spec.md` — contrato de comportamiento (requirements + scenarios WHEN/THEN), no plan de implementación.
3. `notas.md` — **quinto archivo, extensión propia de este repo, NO es parte de OpenSpec**. Documenta decisiones tomadas en el camino y qué cambió respecto al plan original, para el relevo que llegue después. OpenSpec no tiene equivalente a esto.
4. Implement corre en la terminal de Codex (`$openspec-apply-change`) o el agente que corresponda — mismo patrón de 3 terminales descrito en `docs/handbook/ai-agents.md` (este repo no tiene un `docs/router-protocol.md` propio; es el mismo protocolo que documenta `ai-workspace-template`).
5. `openspec archive <ID>` mueve el change completo a `openspec/changes/archive/<fecha>-<ID>/` cuando termina, sincronizando `specs/` con `openspec/specs/` (las specs base del proyecto).

## Por qué se migró desde `tickets/`

La convención anterior (`tickets/_TEMPLATE/{research.md,plan.md,notas.md}`) era una convención propia de este repo sin conexión a ninguna herramienta real de spec-driven development. Ahora hay una sola: la real, la que genera y valida el CLI de `@fission-ai/openspec`, más `notas.md` como la única pieza que valía la pena conservar de la convención anterior.

## Changes de este repo

- `archive/2026-08-22-tk-101-priority-filter/` — filtro por prioridad, ya implementado y mergeado en `main`. Migrado desde `tickets/TK-101/`.
- `tk-102-stats-bug/` — bug real y sin arreglar: `/stats` no descuenta los tickets cerrados del conteo de abiertos. Abierto, para practicar en vivo. Solución de referencia en la rama `reference/tk-102` (ver `openspec/changes/archive/` en esa rama).
- `tk-103-assignee/` — feature media sin implementar: agregar campo `assignee` al ticket. Abierto, para practicar en vivo. Solución de referencia en la rama `reference/tk-103` (ver `openspec/changes/archive/` en esa rama).
