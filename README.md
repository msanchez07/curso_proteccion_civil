# Curs de Protecció Civil en el centre educatiu

**Autor:** Manuel Sánchez Gomis · Professor de FP d’Informàtica · me.sanchezgomis@edu.gva.es

Curs **autònom** de 4 sessions de **55 minuts** sobre prevenció, autoprotecció i resposta inicial davant d’emergències, per a **alumnat de Batxillerat i Cicles Formatius**.

Web bilingüe: **valencià per defecte** i **castellà** en `/es/`.

---

## Estructura

```
.
├── index.html                     ← curs en valencià (portada)
├── aules/index.html               ← guia d’Aules
├── descargas/examen-moodle.xml    ← examen (Moodle XML)
├── es/
│   ├── index.html                 ← curs en castellà
│   ├── aules/index.html           ← guia en castellà
│   └── descargas/examen-moodle.xml
├── README.md
├── .gitignore
└── .nojekyll
```

- **`/`** → curs en valencià.
- **`/es/`** → curs en castellà (complet).
- **`/aules/`** → guia per a importar el XML i publicar el qüestionari.
- **`/descargas/examen-moodle.xml`** → examen de 20 preguntes.

## Estat de la traducció

| Part | Valencià | Castellà |
|---|---|---|
| Interfície, menú i planificació | ✅ | ✅ |
| 12 lliçons i tests de sessió | ✅ | ✅ |
| Glossari (21 termes) | ✅ | ✅ |
| Casos pràctics i exercicis | ⏳ | ✅ |
| Diagrames i captures oficials | ⏳ | ✅ |
| Guia d’Aules | ⏳ (enllaça a la castellana) | ✅ |
| Examen Moodle | ⏳ (enllaça al castellà) | ✅ |

Mentres el valencià no estiga complet, la portada mostra un avís i un enllaç a la versió castellana completa.

## Publicar en GitHub Pages

**Settings › Pages › Deploy from a branch › main · / (root)**.

- `https://TU-USUARIO.github.io/TU-REPO/` → valencià
- `https://TU-USUARIO.github.io/TU-REPO/es/` → castellà
- `https://TU-USUARIO.github.io/TU-REPO/aules/` → guia
- `https://TU-USUARIO.github.io/TU-REPO/descargas/examen-moodle.xml` → descàrrega

## El curs

| Sessió | Títol | Lliçons |
|---|---|---|
| 1 | Entendre el risc i saber a qui escoltar | 3 |
| 2 | Aigua i foc | 3 |
| 3 | Dins de l’edifici i a casa | 3 |
| 4 | Quan el sòl o l’aire són el perill | 3 |

Cada sessió són 55 minuts de treball autònom: tres lliçons, un test i repàs. Cada lliçó inclou «En una frase», explicació completa, casos, pràctica, repàs ràpid, «L’essencial» i fonts.

### Avaluació

| Instrument | Moment | Criteri |
|---|---|---|
| Tests de sessió (4) | Final de cada sessió | 60 % d’encerts; repetició il·limitada |
| Examen final en Aules | En acabar la sessió 4 | 14/20 encerts (70 %) |

## Fonts

Materials públics de **112 Comunitat Valenciana** (Generalitat Valenciana): *Guia tècnica de suport i consulta ràpida* (2026), infografies N1, N2 i N3, textos de suport, díptic i cartell d’inundacions, vídeo i audiollibre de la DANA, i normativa (BOE-A-2025-21354, RD 524/2023, RD 393/2007, resolució autonòmica de 2026).

## Llicència i ús

- El **contingut original** (textos, diagrames, guia, examen) és de Manuel Sánchez Gomis i es compartix per a ús educatiu.
- Les **infografies oficials** pertanyen a la Generalitat Valenciana i es reproduïxen sense modificacions, amb autoria i enllaç a l’original.
- Si vols publicar el repositori amb una llicència explícita, una opció habitual per a materials educatius és **CC BY-NC-SA 4.0**.

## Avís

Material formatiu. **No substitueix** el pla d’autoprotecció del centre, la formació oficial ni les instruccions de l’autoritat competent. En una emergència real: **112**.
