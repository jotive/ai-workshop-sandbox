## Purpose

Permite asignar un responsable (texto libre, sin entidad "usuario") a un ticket, tanto al crearlo como después, para saber quién es dueño de cada ticket sin salir del sistema.

## ADDED Requirements

### Requirement: Un ticket puede crearse con un assignee opcional
El sistema SHALL aceptar un campo opcional `assignee` (texto, 1-200 caracteres) en `POST /tickets`. Cuando no se envía, el ticket SHALL quedar creado con `assignee` igual a `null`.

#### Scenario: Crear ticket sin assignee
- **WHEN** se hace `POST /tickets` sin el campo `assignee`
- **THEN** la respuesta tiene `assignee: null`

#### Scenario: Crear ticket con assignee
- **WHEN** se hace `POST /tickets` con `assignee: "Ana"`
- **THEN** la respuesta tiene `assignee: "Ana"`

### Requirement: Un ticket existente puede reasignarse
El sistema SHALL exponer `POST /tickets/{id}/assign` con un `assignee` obligatorio (no vacío) en el body, que actualiza el `assignee` del ticket indicado sin modificar su `status`.

#### Scenario: Reasignar un ticket existente
- **WHEN** se hace `POST /tickets/{id}/assign` con `assignee: "Bruno"` sobre un ticket existente
- **THEN** la respuesta tiene `assignee: "Bruno"` y el `status` del ticket no cambia

#### Scenario: Reasignar un ticket cerrado
- **WHEN** se hace `POST /tickets/{id}/assign` sobre un ticket con `status == "closed"`
- **THEN** la reasignación se aplica igual (reasignar no está bloqueado por el estado del ticket)

#### Scenario: Reasignar un ticket inexistente
- **WHEN** se hace `POST /tickets/{id}/assign` con un `id` que no existe
- **THEN** el sistema responde `404`

### Requirement: El assignee es texto libre, no una referencia a un usuario
El sistema SHALL tratar `assignee` como texto libre sin validarlo contra ninguna lista de personas del equipo, dado que el dominio no tiene entidad "usuario" ni autenticación por persona.

#### Scenario: Cualquier texto no vacío es válido
- **WHEN** se envía cualquier string de 1 a 200 caracteres como `assignee`
- **THEN** el sistema lo acepta sin validarlo contra una lista cerrada
