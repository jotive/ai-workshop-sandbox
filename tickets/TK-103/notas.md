# Notas — TK-103

> Decisiones tomadas en el camino. Qué cambió respecto al plan original y por qué — para el relevo que llegue después.

- 2026-08-20 — Se agregó un endpoint dedicado `POST /tickets/{id}/assign` en vez de permitir `assignee` en un `PATCH /tickets/{id}` genérico. Razón: el proyecto no tiene ningún endpoint de actualización parcial genérica todavía (solo acciones puntuales como `close`), y agregar un `PATCH` genérico hoy sería sobre-construir para una sola necesidad. Si en el futuro aparecen más campos editables, ahí sí se justifica reconsiderar un `PATCH` genérico — no antes.
- 2026-08-20 — `TicketAssignRequest.assignee` es obligatorio y no vacío (`min_length=1`) a propósito: "reasignar a nadie" no se pidió, y si se necesitara "desasignar" sería un caso de uso distinto y explícito, no un efecto secundario de mandar un string vacío.
