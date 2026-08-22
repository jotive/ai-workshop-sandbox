## Context

Ver `proposal.md` - Why. `TicketRepository.find_all()` (`api/repositories/ticket_repository.py`) ya soportaba un parámetro opcional `priority: TicketPriority | None` desde que se escribió el repositorio inicial (se dejó preparado a propósito). El trabajo real fue research, no reescritura: conectar router → controller y agregar el control en el front.

## Goals / Non-Goals

**Goals:**
- Filtrar por una sola prioridad a la vez, vía query param en `GET /tickets`.
- Contrato de API limpio: o se manda una prioridad válida, o no se manda nada — nunca un valor "vacío" o "todas" como string.

**Non-Goals:**
- Filtrar por múltiples prioridades a la vez (ej. `high,medium`) — no se pidió.
- Filtrar por estado (`open`/`closed`) — eso ya funciona indirectamente cerrando tickets, no es parte de este change.
- Ordenar el listado por prioridad — el orden sigue siendo por `id DESC`.

## Decisions

- **El valor "todas" del `<select>` del front no viaja como query param**: en vez de mandar `priority=all` y que la API lo ignore, el front omite el query param completo cuando el usuario elige "todas". Mantiene el contrato de la API limpio. Alternativa descartada: aceptar `all` como valor válido en el backend — hubiera significado tratar un valor no perteneciente al enum `TicketPriority` como caso especial en la capa de datos, sin necesidad real.
- **No se tocó `TicketRepository.find_all()`**: ya aceptaba `priority: TicketPriority | None` y hacía `SELECT * FROM tickets WHERE priority = ?` (o sin filtro si es `None`). Reescribirlo hubiera sido trabajo innecesario — research evitó ese error antes de tocar código.

## Risks / Trade-offs

- [Riesgo] Ninguno significativo — el cambio es acotado y la capa de datos ya estaba probada indirectamente por los tests existentes de `find_all()`. Mitigación: se agregó un test de integración específico para el filtro end-to-end (`GET /tickets?priority=high`).
