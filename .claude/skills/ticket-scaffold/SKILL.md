---
name: ticket-scaffold
description: Crea un change nuevo de OpenSpec en openspec/changes/<ID>-<descripción>/ (proposal.md, design.md, tasks.md, specs/) más el notas.md propio de este repo
---

> Esta skill reemplaza la convención vieja de `tickets/<ID>/{research.md,plan.md,notas.md}` — ver `tickets/README.md`.

Cuando el usuario pida arrancar un ticket/change nuevo (da un ID tipo `TK-104` o pide "arranca el ticket X"):

1. Deriva `<ID>-<descripción-corta-kebab-case>` (ej. `TK-104-add-comments`). El ID es el que ya existe en el sistema de tickets del equipo — no se inventa uno nuevo.
2. Corre `openspec new change <ID>-<descripción-corta>` — **nunca crear la carpeta a mano bajo `openspec/changes/`**, el CLI genera `.openspec.yaml` con metadata que los demás comandos (`status`, `instructions`, `validate`, `archive`) necesitan.
3. Escribe `openspec/changes/<ID>-<descripción-corta>/notas.md` con el encabezado:
   ```
   # Notas — <ID>-<descripción-corta>

   > Extensión propia de este repo (NO es parte de OpenSpec). Decisiones tomadas en el camino, qué cambió del plan original y por qué.

   - <fecha> — <primera entrada, si ya hay algo que registrar>
   ```
   Si no hay nada que registrar todavía, deja solo el encabezado — no inventes decisiones que no se tomaron.
4. Sugiere `/opsx:explore` (si hace falta pensar el problema primero) y `/opsx:propose "<descripción>"` como siguiente paso para generar `proposal.md`, `design.md`, `tasks.md` y `specs/<capability-path>/spec.md` — no los ejecuta solo, es decisión del usuario cuándo pasar de scaffolding a planning real.
5. No inventa contenido de `proposal.md`, `design.md`, `tasks.md` ni `specs/` — esos los genera `/opsx:propose` siguiendo las instrucciones reales del CLI (`openspec instructions <artefacto> --change <ID> --json`), no este skill.

Ver `openspec/changes/README.md` para la convención completa y `openspec/changes/tk-102-stats-bug/` o `tk-103-assignee/` para ejemplos reales de changes abiertos con los 5 archivos (4 de OpenSpec + `notas.md`).
