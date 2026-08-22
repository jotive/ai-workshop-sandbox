# Research — TK-101

> Volcado del agente en modo solo-lectura. Qué existe hoy, qué toca, qué no se sabe todavía.

## Qué se pidió

"En el listado de tickets quiero poder filtrar por prioridad, para no tener que scrollear todo cuando solo me importan los `high`."

## Qué existe hoy (relevante a este cambio)

- `GET /tickets` en `api/routes/tickets.py` lista todos los tickets sin ningún query param — llama a `TicketController.list()` sin argumentos.
- `TicketController.list()` en `api/controllers/ticket_controller.py` delega a `TicketService.list_tickets()`.
- `TicketService.list_tickets()` en `api/services/ticket_service.py` delega a `TicketRepository.find_all()`.
- `TicketRepository.find_all()` en `api/repositories/ticket_repository.py` ya soporta un parámetro opcional `priority: TicketPriority | None` (se implementó pensando en este filtro desde el schema de la tabla) — hace `SELECT * FROM tickets WHERE priority = ?` cuando se pasa, o `SELECT * FROM tickets` cuando es `None`. Solo falta exponerlo en las capas de arriba.
- `TicketPriority` (`low`/`medium`/`high`) ya existe como enum en `api/schemas/ticket.py`.
- El front (`front/index.html`) tiene un `<select>` de prioridad en el formulario de creación, pero no hay ningún control de filtro en la sección de listado.

## Preguntas abiertas / [unknown]

- Ninguna — el cambio es acotado: la capa de datos ya soporta el filtro, falta conectar router → controller → service y agregar el `<select>` de filtro en el front.
