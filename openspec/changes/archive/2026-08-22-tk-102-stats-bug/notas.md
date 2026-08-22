# Notas — tk-102-stats-bug

> Extensión propia de este repo (NO es parte de OpenSpec). Decisiones tomadas en el camino, qué cambió del plan original y por qué — para el relevo que llegue después.

- 2026-08-20 — El fix fue de una sola línea de intención (agregar el `WHERE status = ?` que faltaba), pero se agregaron dos tests (unitario + integración) en vez de uno solo: el unitario prueba la capa de datos aislada, el de integración prueba que el contrato HTTP de `/stats` también refleja el fix. Se decidió no dejar el bug cubierto solo a nivel unitario porque el síntoma original lo reportó alguien mirando el endpoint, no el código.
- 2026-08-22 — Migrado desde `tickets/TK-102/{research.md,plan.md,notas.md}` (convención propia, reemplazada) a este change real de OpenSpec en la rama `reference/tk-102`, generado con la CLI (`openspec new change tk-102-stats-bug`). El fix ya estaba implementado en esta rama antes de esta migración; este change documenta retroactivamente el ciclo research → plan → implementa → verifica, y se archiva inmediatamente para reflejar el estado resuelto.
