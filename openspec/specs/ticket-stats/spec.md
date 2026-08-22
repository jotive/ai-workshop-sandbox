# ticket-stats Specification

## Purpose
Reporta el conteo de tickets por estado (`total`, `open`, `closed`) en `GET /stats`, para tener una vista agregada sin tener que contar el listado a mano.

## Requirements

### Requirement: El conteo de tickets abiertos excluye los tickets cerrados
El sistema SHALL reportar en `GET /stats` un valor `open` igual a la cantidad de tickets con `status == "open"`, excluyendo explícitamente los tickets con `status == "closed"`.

#### Scenario: Hay tickets abiertos y cerrados
- **WHEN** existen 2 tickets, uno con `status == "open"` y otro con `status == "closed"`
- **THEN** `GET /stats` devuelve `total: 2`, `open: 1`, `closed: 1`

#### Scenario: Todos los tickets están abiertos
- **WHEN** no se cerró ningún ticket
- **THEN** `GET /stats` devuelve `open` igual a `total`

#### Scenario: Todos los tickets están cerrados
- **WHEN** se cerraron todos los tickets existentes
- **THEN** `GET /stats` devuelve `open: 0`

### Requirement: El total cuenta todos los tickets sin filtrar
El sistema SHALL reportar en `GET /stats` un valor `total` igual a la cantidad total de tickets, sin filtrar por `status`.

#### Scenario: Total incluye abiertos y cerrados
- **WHEN** existen tickets abiertos y cerrados
- **THEN** `GET /stats` devuelve `total` igual a la suma de `open` + `closed`
