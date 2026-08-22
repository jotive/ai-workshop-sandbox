# Reglas para agentes de código en este repo

## Ciclo de trabajo: Research → Plan → Implement → Verify, con OpenSpec real

Este repo usa `@fission-ai/openspec` de verdad (no una convención de carpetas propia — la convención vieja en `tickets/` fue reemplazada, ver `tickets/README.md`). Cada ticket/feature es un change en `openspec/changes/<ID>-<descripción>/`:

1. **Research** (opcional): explorar el problema — qué existe hoy, qué toca, qué queda como `[unknown]` — antes de escribir código.
2. **Plan**: `proposal.md` (qué y por qué), `design.md` (cómo, decisiones y alternativas descartadas), `tasks.md` (checklist verificable), `specs/<capability-path>/spec.md` (contrato de comportamiento, requirements + scenarios WHEN/THEN) — los 4 artefactos reales de OpenSpec. Se revisan ANTES de implementar.
3. **Implement**: implementar contra `tasks.md`, marcando checkboxes a medida que avanza. Verificar el diff línea a línea.
4. **Verify**: `pytest` en verde + `openspec validate <ID> --strict` antes de dar el change por terminado.

`notas.md` es un **quinto archivo, extensión propia de este repo, NO es parte de OpenSpec**: decisiones tomadas en el camino, qué cambió del plan original y por qué, para el relevo que llegue después.

Al terminar: `openspec archive <ID>` mueve el change a `openspec/changes/archive/` y sincroniza `openspec/specs/` (las specs base del proyecto).

## Protocolo multi-agente (Claude Code + Codex)

Si trabajás con más de un agente en paralelo (Claude Code para Research/Plan/Verify, Codex para Implement), este repo sigue el mismo protocolo de 3 terminales documentado en `ai-workspace-template/docs/router-protocol.md` — no se duplica acá porque es contenido específico del router, no de este proyecto. Resumen mínimo:

```
Terminal 1: claude   → Research (/opsx:explore) + Plan (/opsx:propose)
Terminal 2: codex    → Implement ($openspec-apply-change)
Terminal 1: claude   → Verify (revisión de diff + openspec validate --strict + pytest)
```

Regla dura: durante Implement, el agente NO debe modificar `proposal.md`, `design.md` ni `specs/` del change en curso — solo `tasks.md` (checkboxes) y código real. Ante ambigüedad, no asume: documenta el bloqueo y espera resolución humana (o de Claude en fase Plan) antes de seguir.

## Reglas duras específicas de este repo

- API en `api/`, capas separadas: `routes` → `controllers` → `services` → `repositories`. No saltarse capas.
- DTOs de entrada/salida con Pydantic en `api/schemas/`. Nada de dicts sueltos cruzando capas.
- Persistencia: SQLite vía `sqlite3` estándar, sin ORM (ver `docs/adr/0002-sqlite-sin-orm.md`). No agregar SQLAlchemy/Postgres sin discutirlo primero.
- Front en `front/index.html`: HTML+JS vanilla sin build step. No introducir React/Vite/npm.
- No relitigar ADRs: respetar las decisiones en `docs/adr/`.
- No sobre-construir: este proyecto es MVP a propósito (ver `docs/handbook/releases.md`).
