# Notas — TK-101

> Decisiones tomadas en el camino. Qué cambió respecto al plan original y por qué — para el relevo que llegue después.

- 2026-08-20 — El plan original asumía que había que agregar el filtro a `TicketRepository.find_all()` desde cero. En research se encontró que el parámetro `priority` ya estaba soportado en esa capa (se había dejado preparado al escribir el repositorio inicial), así que el trabajo real quedó limitado a conectar router → controller y agregar el control en el front. Se documenta acá para que quede claro que no fue un cambio de scope, fue research que evitó reescribir algo que ya existía.
- 2026-08-20 — Se decidió que el valor `all` del `<select>` del front no viaje como query param (en vez de mandar `priority=all` y que la API lo ignore) — mantiene el contrato de la API limpio: o se manda una prioridad válida, o no se manda nada.
