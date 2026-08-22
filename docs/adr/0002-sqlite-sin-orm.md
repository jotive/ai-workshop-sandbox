# 0002. SQLite sin ORM para el sistema de tickets

- **Fecha**: 2026-08-20
- **Estado**: Aceptado
- **Autor**: Josse

## Contexto y Problema

El sistema de tickets necesita persistencia local, simple de levantar en una jornada de capacitación en vivo, sin depender de un servicio de base de datos externo ni de credenciales de infra real.

## Decisión Tomada

Usar SQLite con el módulo estándar `sqlite3`, acceso encapsulado exclusivamente en `api/repositories/ticket_repository.py` (repository pattern manual, sin ORM). El schema se crea con `CREATE TABLE IF NOT EXISTS` en `api/db.py::init_db()` al arrancar la app — no hay migraciones versionadas porque el dominio es chico y el proyecto es un sandbox de práctica, no un sistema en producción.

## Opciones Descartadas

- **PostgreSQL + SQLAlchemy**: exige levantar un contenedor de base de datos aparte y agrega una capa de ORM/migraciones (Alembic) que no aporta nada al objetivo pedagógico del proyecto — la meta dura es instalar y correr en menos de 5 minutos.
- **SQLAlchemy Core sobre SQLite**: se descartó igual para mantener cero dependencias de ORM y que el repository pattern quede explícito y fácil de leer en una sesión de research de 10-15 minutos.

## Consecuencias y Trade-offs

- **Positivas**: cero servicios externos, arranque instantáneo, el SQL queda explícito y auditable en una sola capa.
- **Negativas / Riesgos**: sin pool de conexiones ni migraciones versionadas — aceptable para el alcance de este proyecto. Si este dominio creciera a un proyecto real, esta decisión debería reabrirse explícitamente con un nuevo ADR.
