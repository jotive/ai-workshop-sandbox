# ai-workshop-sandbox

Mini sistema de tickets internos (crear, listar, filtrar por prioridad, cerrar) con API en FastAPI + SQLite y un front vanilla de una sola página. Es el proyecto de práctica de una jornada de capacitación de desarrollo agéntico con IA: sirve para recorrer el ciclo **research → plan → implementa → revisa diff** sobre código real.

## Instalación en menos de 5 minutos (Python directo — vía principal)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api.main:app --reload
```

Verificar que levantó:

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

Abrir el front directamente como archivo (`front/index.html`) o servirlo:

```bash
python -m http.server 8080 --directory front
```

La API key de desarrollo por default es `dev-local-key` (ver `.env.example`) — el front la pide en un input y la guarda en `localStorage`.

## Alternativa: Docker Compose (opcional, no es la vía principal)

```bash
docker compose up -d
curl http://localhost:8000/health
docker compose down
```

Levanta la API en `:8000` y el front (servido por nginx) en `:8080`.

## Correr los tests

```bash
pytest
```

## Estructura

Ver `docs/architecture.md` para el detalle completo del stack y las capas (`routes` → `controllers` → `services` → `repositories`). Ver `CLAUDE.md` / `AGENTS.md` para el contexto que consumen los agentes de IA, y `tickets/` para los tickets de práctica de la jornada (`TK-101`, `TK-102`, `TK-103`).

## Ramas de este repo

- `main` — proyecto base + TK-101 (filtro por prioridad) ya implementado. TK-102 (bug de `/stats`) y TK-103 (campo `assignee`) quedan abiertos para practicar en vivo.
- `reference/tk-102`, `reference/tk-103` — soluciones de referencia de esos dos tickets, ya implementadas pero sin mergear a `main`. No mirar antes de intentar el ejercicio.
- `bench-claude`, `bench-codex` — ramas vacías para comparar Claude Code vs Codex CLI resolviendo el mismo ticket en vivo.
