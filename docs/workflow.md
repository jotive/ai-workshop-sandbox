# Workflow de Desarrollo y Deploy

> Proceso operativo: preparación de entorno, checklist pre-merge y deploy.

## 1. Preparación del Entorno Local (vía Python — vía principal)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api.main:app --reload
```

`GET http://localhost:8000/health` debe responder `{"status": "ok"}`. El front se puede abrir directo como archivo (`front/index.html`) o servirlo con `python -m http.server 8080 --directory front`.

## 2. Alternativa: Docker Compose (opcional, no es la vía principal)

```bash
docker compose up -d
docker compose logs -f api
docker compose down
```

## 3. Checklist Pre-Merge (Definition of Done)

- [ ] Spec previa escrita en `tickets/TK-XXX/research.md` y `plan.md`.
- [ ] Diff revisado línea a línea por el desarrollador.
- [ ] Suite de tests ejecutada en verde (`pytest`).
- [ ] `tickets/TK-XXX/notas.md` actualizado si algo cambió respecto al plan.
- [ ] Cero credenciales reales expuestas en código (el `API_KEY` de ejemplo es solo para desarrollo local).

## 4. Proceso de "Deploy"

Este proyecto es un sandbox de práctica — no tiene pipeline de deploy real. "Deploy" acá significa: correr `uvicorn` (o `docker compose up -d`) localmente y validar contra `/health` y `/stats`.
