# Onboarding

> Cómo arranca alguien nuevo (humano o agente) en `ai-workshop-sandbox`.

## 1. Leé esto primero

1. `README.md` — qué es el proyecto y cómo levantarlo.
2. `AGENTS.md` / `CLAUDE.md` — reglas duras de este repo (capas, sin ORM, sin build step en el front).
3. `docs/architecture.md` — stack real y lo que NO existe (para no alucinar dependencias).

## 2. Primeros comandos

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api.main:app --reload
```

Verificar: `curl http://localhost:8000/health` debe responder `{"status":"ok"}`. Correr `pytest` y confirmar que los 16 tests existentes pasan antes de tocar nada.

## 3. Tu primer change de OpenSpec

Este repo usa OpenSpec real (`@fission-ai/openspec`), no una convención de carpetas inventada — ver `openspec/changes/README.md`. Para practicar el ciclo completo sin inventar un ticket nuevo, usá uno de los dos changes ya abiertos:

- `openspec/changes/tk-102-stats-bug/` — bug real, plan completo ya escrito (`proposal.md`/`design.md`/`tasks.md`), `notas.md` vacío para llenar en vivo.
- `openspec/changes/tk-103-assignee/` — feature media, mismo estado.

Pasos:

1. `openspec status --change tk-102-stats-bug` (o `tk-103-assignee`) para confirmar que los 4 artefactos están completos.
2. Leé `proposal.md` → `design.md` → `tasks.md` en ese orden.
3. Implementá contra `tasks.md`, marcando checkboxes a medida que avanzás.
4. Corré `pytest` en verde antes de dar la tarea por terminada.
5. Registrá en `notas.md` cualquier decisión que se haya desviado del plan — es el quinto archivo, extensión propia de este repo (no es parte de OpenSpec).
6. `openspec validate <ID> --strict` antes de considerar el change terminado.

No mires las ramas `reference/tk-102` / `reference/tk-103` antes de intentarlo — tienen la solución de referencia ya implementada, para comparar tu resultado después, no para copiar antes.

## 4. Dónde mirar primero según lo que necesites

| Necesito... | Mirar |
|---|---|
| Entender una capa (routes/controllers/services/repositories) | `docs/architecture.md` |
| Saber si algo ya se decidió (SQLite sin ORM, etc.) | `docs/adr/` |
| Un término de dominio (`assignee`, `stats`, etc.) | `docs/glossary.md` |
| Cómo correr tests / qué cubrir | `docs/handbook/testing.md` |
| Un error conocido | `docs/handbook/errors.md` |
| Reglas para agentes de código en este repo | `docs/handbook/ai-agents.md` |
