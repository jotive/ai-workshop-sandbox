# Notas — TK-102

> Decisiones tomadas en el camino. Qué cambió respecto al plan original y por qué — para el relevo que llegue después.

- 2026-08-20 — El fix fue de una sola línea de intención (agregar el `WHERE status = ?` que faltaba), pero se agregaron dos tests (unitario + integración) en vez de uno solo: el unitario prueba la capa de datos aislada, el de integración prueba que el contrato HTTP de `/stats` también refleja el fix. Se decidió no dejar el bug cubierto solo a nivel unitario porque el síntoma original lo reportó alguien mirando el endpoint, no el código.
