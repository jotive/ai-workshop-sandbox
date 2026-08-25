# Workflow

> Índice denso del ciclo de trabajo día a día en `ai-workshop-sandbox`. Detalle completo de cada sección en su propio archivo del handbook.

## Preparación de entorno

Vía principal: Python + venv.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api.main:app --reload
```

`GET http://localhost:8000/health` debe responder `{"status": "ok"}`. Alternativa opcional (no es la vía principal): `docker compose up -d`. Comandos comunes y detalle completo → `docs/handbook/development.md`.

## Checklist antes de mergear

- `pytest` en verde. Ningún cambio se da por terminado si la suite no pasa — `main` siempre debe estar en verde.
- Para un change de OpenSpec: además de `pytest`, correr `openspec validate <ID> --strict`.
- Revisar el diff línea a línea (fase Verify) — no basta con que los tests pasen. Detalle completo → `docs/handbook/testing.md`.

## Convención de ramas

Este repo no tiene remoto ni flujo de PR real. `main` es la rama base + TK-101 ya implementado; `reference/tk-102` y `reference/tk-103` son soluciones de referencia sin mergear; `bench-claude`/`bench-codex` son ramas vacías para comparar agentes en vivo. Un commit por change completo (o por tarea de `tasks.md` si el change es grande). Detalle completo → `docs/handbook/git-workflow.md`.

## Deploy

No hay deploy real en este proyecto — es un sandbox de práctica, sin versionado semántico, changelog ni pipeline de release. "Deploy" acá significa correr `uvicorn` (o `docker compose up -d`) local y validar contra `/health` y `/stats`. Detalle completo → `docs/handbook/releases.md`.

## Ciclo con agentes IA

Research → Plan → Implement → Verify sobre OpenSpec real (`openspec/changes/<ID>/`), con reglas duras de capas y cuándo saltarse fases. Detalle completo → `docs/handbook/ai-agents.md`.
