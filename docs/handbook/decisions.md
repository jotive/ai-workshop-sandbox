# Decisiones — Índice Rápido

> Log corto de decisiones tomadas en este proyecto. Detalle largo (contexto, opciones descartadas, consecuencias) vive en `docs/adr/`, un archivo por decisión. Esta tabla es el resumen de una fila por ADR, no lo reemplaza.

| Decisión | Por qué | Descartado | Estado |
|---|---|---|---|
| SQLite sin ORM (`sqlite3` estándar, repository pattern manual) — [ADR 0002](../adr/0002-sqlite-sin-orm.md) | Persistencia local simple de levantar en una jornada de capacitación en vivo, sin infra externa ni credenciales reales; meta dura de instalar y correr en menos de 5 minutos. | PostgreSQL + SQLAlchemy (exige contenedor aparte + Alembic); SQLAlchemy Core sobre SQLite (agrega ORM sin necesidad, rompe el repository pattern explícito). | Aceptado |
