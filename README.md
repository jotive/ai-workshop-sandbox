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

Ver `docs/architecture.md` para el detalle completo del stack y las capas (`routes` → `controllers` → `services` → `repositories`). Ver `CLAUDE.md` / `AGENTS.md` para el contexto que consumen los agentes de IA, `docs/onboarding.md` para arrancar de cero, y `openspec/changes/` para los changes de práctica de la jornada (`tk-101-priority-filter` archivado, `tk-102-stats-bug` y `tk-103-assignee` abiertos) — reemplaza la vieja carpeta `tickets/` (ver `tickets/README.md`).

## Documentación

- `ROADMAP.md` — ahora · siguiente · después (con bloqueador) · hecho.
- `HANDBOOK.md` — índice a `docs/handbook/` (desarrollo, git, testing, releases, errores, agentes de IA — contenido bajo demanda).
- `docs/onboarding.md` — cómo arranca alguien nuevo, humano o agente.
- `docs/adr/` — decisiones de arquitectura aceptadas.

## Ramas de este repo

- `main` — proyecto base + TK-101 (filtro por prioridad) ya implementado, archivado en `openspec/changes/archive/2026-08-22-tk-101-priority-filter/`. TK-102 (bug de `/stats`) y TK-103 (campo `assignee`) quedan abiertos en `openspec/changes/` para practicar en vivo.
- `reference/tk-102`, `reference/tk-103` — soluciones de referencia de esos dos changes, ya implementadas pero sin mergear a `main` (cada una con su propio `openspec/changes/archive/` reflejando el estado resuelto). No mirar antes de intentar el ejercicio.
- `bench-claude`, `bench-codex` — ramas vacías para comparar Claude Code vs Codex CLI resolviendo el mismo ticket en vivo.
