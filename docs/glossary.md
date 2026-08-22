# Glosario del Dominio

> Diccionario de términos y entidades del dominio de tickets usados en este repo.

## Términos

| Término | Definición | Contexto de Uso |
|---|---|---|
| **Ticket** | Unidad de trabajo interna: título, descripción, prioridad y estado. | Entidad central del sistema. |
| **Priority (prioridad)** | `low` \| `medium` \| `high`. Fijada al crear el ticket, filtrable en el listado (`GET /tickets?priority=`). | `api/schemas/ticket.py::TicketPriority` |
| **Status (estado)** | `open` \| `closed`. Un ticket nace `open`, se cierra vía `POST /tickets/{id}/close`. No hay estados intermedios en el MVP. | `api/schemas/ticket.py::TicketStatus` |
| **Assignee** | Persona responsable del ticket (texto libre, no referencia a un usuario). Se fija al crear o vía `POST /tickets/{id}/assign`. Resuelto en esta rama (TK-103); no existe todavía en `main`. | `tickets/TK-103/` |
| **Stats** | Conteo de tickets por estado, expuesto en `GET /stats` (`total`, `open`, `closed`). | `api/routes/stats.py` |
| **X-API-Key** | Header de autenticación simple; se valida contra la variable de entorno `API_KEY`. No hay usuarios ni sesiones. | `api/dependencies.py::require_api_key` |
| **DTO** | Data Transfer Object — modelo Pydantic que valida entrada/salida de la API. | `api/schemas/` |
| **SDD** | Spec-Driven Development — escribir el plan antes del código. | `tickets/TK-XXX/plan.md` |
| **RPI** | Research → Plan → Implement — ciclo de vida de trabajo por ticket usado en esta jornada. | `AGENTS.md` |
