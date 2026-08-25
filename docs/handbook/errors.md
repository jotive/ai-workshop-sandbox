# Catálogo de Errores Conocidos y Troubleshooting

> Base de conocimiento de errores comunes, síntomas, causa raíz y soluciones probadas. Consolidado en `docs/handbook/` junto con el resto de la documentación del proyecto.

## 1. `401 Unauthorized` en cualquier endpoint de tickets/stats

- **Síntoma**: `{"detail":"Invalid API key"}` al llamar `/tickets` o `/stats`.
- **Causa raíz**: falta el header `X-API-Key`, o no coincide con la variable de entorno `API_KEY` (default `dev-local-key` en `.env.example`).
- **Solución**: agregar el header `X-API-Key: <valor de API_KEY>` en la request, o cargar el valor correcto en el input de API key del front.

## 2. `sqlite3.OperationalError: unable to open database file`

- **Síntoma**: la API no arranca o falla en el primer request a `/tickets`.
- **Causa raíz**: `DATABASE_PATH` apunta a un directorio que no existe (típico al correr con Docker si el volumen no está montado).
- **Solución**: verificar que el directorio de `DATABASE_PATH` exista, o correr con la ruta relativa default (`tickets.db` en la raíz del proyecto).

## 3. `ModuleNotFoundError: No module named 'api'`

- **Síntoma**: falla al correr `pytest` o `uvicorn api.main:app` desde otra carpeta.
- **Causa raíz**: el comando se corrió fuera de la raíz del repo, o el venv no está activado.
- **Solución**: correr siempre desde la raíz del repo con el venv activado. `pytest` ya tiene `pythonpath = .` configurado en `pytest.ini`.

## 4. `/stats` muestra `open` igual a `total` aunque haya tickets cerrados

- **Síntoma**: el conteo de tickets abiertos en `/stats` no baja después de cerrar tickets.
- **Causa raíz**: bug conocido y sin arreglar en `main` — ver `openspec/changes/tk-102-stats-bug/`. No es un problema de entorno, es el bug a resolver en el ejercicio.
- **Solución**: resolverlo como change de OpenSpec (research → plan → fix + test, siguiendo `openspec/changes/tk-102-stats-bug/tasks.md`). La solución de referencia vive en la rama `reference/tk-102`.
