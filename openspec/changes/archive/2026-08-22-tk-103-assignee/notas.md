# Notas — tk-103-assignee

> Extensión propia de este repo (NO es parte de OpenSpec). Decisiones tomadas en el camino, qué cambió del plan original y por qué — para el relevo que llegue después.

- 2026-08-20 — Se agregó un endpoint dedicado `POST /tickets/{id}/assign` en vez de permitir `assignee` en un `PATCH /tickets/{id}` genérico. Razón: el proyecto no tiene ningún endpoint de actualización parcial genérica todavía (solo acciones puntuales como `close`), y agregar un `PATCH` genérico hoy sería sobre-construir para una sola necesidad. Si en el futuro aparecen más campos editables, ahí sí se justifica reconsiderar un `PATCH` genérico — no antes.
- 2026-08-20 — `TicketAssignRequest.assignee` es obligatorio y no vacío (`min_length=1`) a propósito: "reasignar a nadie" no se pidió, y si se necesitara "desasignar" sería un caso de uso distinto y explícito, no un efecto secundario de mandar un string vacío.
- 2026-08-22 — Migrado desde `tickets/TK-103/{research.md,plan.md,notas.md}` (convención propia, reemplazada) a este change real de OpenSpec en la rama `reference/tk-103`, generado con la CLI (`openspec new change tk-103-assignee`). La feature ya estaba implementada en esta rama antes de esta migración; este change documenta retroactivamente el ciclo research → plan → implementa → verifica, y se archiva inmediatamente para reflejar el estado resuelto.
