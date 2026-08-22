# tickets/

Una carpeta por ticket del sistema que ya usa el equipo (Jira, Linear, GitHub Issues — el ID es el que ya existe, no se inventa uno nuevo). Deja traza de lo trabajado sin depender de reconstruir una conversación de chat.

## Cómo usar

1. Copia `_TEMPLATE/` → `tickets/<ID>/` (ej. `tickets/TK-104/`).
2. `research.md` — lo que el agente encontró en modo solo-lectura, antes de tocar código.
3. `plan.md` — el plan troceado en pasos verificables, revisado ANTES de implementar (esto es la spec).
4. `notas.md` — decisiones tomadas en el camino, cosas que cambiaron respecto al plan original y por qué.

## Tickets de este repo

- `TK-101/` — filtro por prioridad en el listado. Ciclo completo ya recorrido y mergeado en `main`.
- `TK-102/` — bug: `/stats` no descuenta los tickets cerrados del conteo de abiertos. Abierto en `main`, solución de referencia en `reference/tk-102`.
- `TK-103/` — feature: agregar campo `assignee` al ticket. Abierto en `main`, solución de referencia en `reference/tk-103`.

## Por qué

Cualquiera en el equipo abre `tickets/<ID>/` y entiende qué se pidió, qué se decidió y qué se hizo — sin preguntarle a quien lo hizo ni desenterrar el chat.
