# Curso de Protección Civil en el centro educativo

**Autor:** Manuel Sánchez Gomis · Profesor de FP de Informática · me.sanchezgomis@edu.gva.es

Curso **autónomo** de 4 sesiones de **55 minutos** sobre prevención, autoprotección y respuesta inicial ante emergencias, para **alumnado de Bachillerato y Ciclos Formativos**.

Incluye el curso completo en una web autocontenida, la **guía para publicarlo en Aules** y el **examen en formato Moodle XML** listo para importar.

---

## Estructura del repositorio

```
.
├── index.html                     ← el curso (portada del repo)
├── aules/
│   └── index.html                 ← guía paso a paso para Aules
├── descargas/
│   └── examen-moodle.xml          ← examen de 20 preguntas (Moodle XML)
├── README.md
├── .gitignore
└── .nojekyll
```

- **`/`** → curso completo. Se abre con doble clic: no necesita servidor, internet ni dependencias externas.
- **`/aules/`** → guía para importar el XML, crear el cuestionario y publicarlo, con capturas de la interfaz actual de Aules (Moodle 5.2) y enlace a un vídeo de referencia.
- **`/descargas/examen-moodle.xml`** → examen final listo para el banco de preguntas.

---

## Verlo en local

1. Descarga o clona el repositorio.
2. Abre `index.html` en cualquier navegador actual.
3. La guía está en `aules/index.html` y el examen en `descargas/examen-moodle.xml`.

> El progreso del curso se guarda en el almacenamiento local del navegador. En modo privado funciona igual, pero no recuerda el avance.

---

## Publicarlo en GitHub Pages

1. Sube el repositorio a GitHub.
2. Ve a **Settings › Pages**.
3. En *Build and deployment*, elige **Deploy from a branch**.
4. Rama: **main** · Carpeta: **/ (root)**. Guarda.
5. En uno o dos minutos tendrás:
   - `https://TU-USUARIO.github.io/TU-REPO/` → el curso.
   - `https://TU-USUARIO.github.io/TU-REPO/aules/` → la guía.
   - `https://TU-USUARIO.github.io/TU-REPO/descargas/examen-moodle.xml` → descarga directa del examen.

El archivo `.nojekyll` evita que GitHub procese el sitio con Jekyll y sirve el HTML tal cual.

---

## El curso

| Sesión | Título | Lecciones |
|---|---|---|
| 1 | Entender el riesgo y saber a quién escuchar | 3 |
| 2 | Agua y fuego | 3 |
| 3 | Dentro del edificio y en casa | 3 |
| 4 | Cuando el suelo o el aire son el peligro | 3 |

Cada sesión son 55 minutos de trabajo autónomo. Cada lección incluye:

- **En una frase** y explicación completa del fenómeno.
- **Diagrama propio** del mecanismo.
- **Casos frecuentes**: situación, qué hacer y por qué.
- **Practica**: decidir, ordenar y verdadero/falso, con corrección razonada.
- **Repaso rápido**: tres preguntas de comprobación.
- **Lo esencial** y **fuentes** de la lección.

Además: 10 capturas de infografías oficiales del 112CV intercaladas en las explicaciones y un glosario de 21 términos.

### Evaluación

| Instrumento | Momento | Criterio |
|---|---|---|
| Tests de sesión (4) | Final de cada sesión | 60 % de aciertos; repetición ilimitada |
| Examen final en Aules | Al terminar la sesión 4 | 14/20 aciertos (70 %) |

El examen final **no** está dentro del curso: se hace en Aules con `descargas/examen-moodle.xml` (20 preguntas, 19 tipo test y 1 verdadero/falso).

---

## Fuentes

Todo el contenido se elabora a partir de materiales públicos de **112 Comunitat Valenciana** (Generalitat Valenciana), y cada lección enlaza la sección exacta que utiliza:

- *Guia tècnica de suport i consulta ràpida per al professorat de centres docents no universitaris* (2026).
- Infografías N1, N2 y N3, textos de apoyo, díptico y cartel de inundaciones.
- Vídeo y audiolibro sobre la DANA del 112CV.
- Normativa: Plan de formación (BOE-A-2025-21354), RD 524/2023, RD 393/2007 y resolución autonómica de 2026.

---

## Licencia y uso

- El **contenido original** (textos, diagramas, guía, examen) es de Manuel Sánchez Gomis y se comparte para uso educativo.
- Las **infografías oficiales** incrustadas pertenecen a la Generalitat Valenciana y se reproducen sin modificaciones, con autoría y enlace al original.
- Si quieres publicar el repositorio con una licencia explícita, una opción habitual para materiales educativos es **CC BY-NC-SA 4.0**: permite reutilizar y adaptar citando la autoría, sin uso comercial y compartiendo igual.

---

## Aviso

Este curso es material formativo. **No sustituye** al plan de autoprotección del centro, a la formación oficial ni a las instrucciones de la autoridad competente. Las decisiones de evacuación, confinamiento, comunicación con familias, suspensión de actividad o reapertura se rigen por el plan del centro y por la autoridad.

En una emergencia real: **112**.

---

*Versión 4.0 · Curso autónomo · 4 sesiones de 55 min · 12 lecciones · Examen final en Aules.*
