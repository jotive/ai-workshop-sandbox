---
name: ticket-scaffold
description: Crea la carpeta de un ticket nuevo en tickets/<ID>/ copiando la plantilla
---

Cuando el usuario pida arrancar un ticket nuevo (da un ID tipo `TK-104` o pide "arranca el ticket X"):

1. Copia `tickets/_TEMPLATE/` a `tickets/<ID>/`.
2. Pregunta una frase del "qué se pidió" si no la dieron, y la escribe en `research.md`.
3. No inventa contenido de `plan.md` ni `notas.md` más allá de los placeholders — eso lo llena el research real.
