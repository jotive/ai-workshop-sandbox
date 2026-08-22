# Desarrollo día a día

## Preparación del entorno local (vía Python — vía principal)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api.main:app --reload
```

`GET http://localhost:8000/health` debe responder `{"status": "ok"}`. El front se puede abrir directo como archivo (`front/index.html`) o servirlo con:

```bash
python -m http.server 8080 --directory front
```

La API key de desarrollo por default es `dev-local-key` (ver `.env.example`) — el front la pide en un input y la guarda en `localStorage`.

## Alternativa: Docker Compose (opcional, no es la vía principal)

```bash
docker compose up -d
docker compose logs -f api
docker compose down
```

Levanta la API en `:8000` y el front (servido por nginx) en `:8080`.

## Comandos comunes

| Qué | Comando |
|---|---|
| Correr la API en modo dev | `uvicorn api.main:app --reload` |
| Servir el front | `python -m http.server 8080 --directory front` |
| Correr toda la suite de tests | `pytest` |
| Ver status de un change de OpenSpec | `openspec status --change <ID>` |
| Validar un change antes de darlo por terminado | `openspec validate <ID> --strict` |

Ver `docs/architecture.md` para el detalle de stack y estructura de carpetas.
