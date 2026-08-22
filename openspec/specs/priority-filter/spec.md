# priority-filter Specification

## Purpose
Permite filtrar el listado de tickets por prioridad (`low`/`medium`/`high`) desde la API y desde el front, para no tener que revisar el listado completo cuando solo interesa una prioridad.

## Requirements

### Requirement: El listado de tickets acepta un filtro opcional por prioridad
El sistema SHALL aceptar un query param opcional `priority` en `GET /tickets` con valor `low`, `medium` o `high`, y SHALL devolver únicamente los tickets con esa prioridad cuando se envía.

#### Scenario: Filtro por prioridad enviado
- **WHEN** se hace `GET /tickets?priority=high`
- **THEN** la respuesta contiene únicamente tickets con `priority == "high"`

#### Scenario: Sin filtro
- **WHEN** se hace `GET /tickets` sin query param `priority`
- **THEN** la respuesta contiene todos los tickets, sin filtrar por prioridad

### Requirement: El front permite filtrar el listado por prioridad sin recargar la página
El sistema SHALL ofrecer un control de selección de prioridad sobre el listado que, al cambiar de valor, vuelve a pedir el listado con el filtro aplicado (o sin filtro si se elige "todas"), sin recargar la página completa.

#### Scenario: Usuario cambia el filtro a "high"
- **WHEN** el usuario selecciona `high` en el control de filtro
- **THEN** el front pide `GET /tickets?priority=high` y actualiza la lista visible con la respuesta, sin recargar la página

#### Scenario: Usuario selecciona "todas"
- **WHEN** el usuario selecciona la opción "todas" en el control de filtro
- **THEN** el front pide `GET /tickets` sin el query param `priority`
