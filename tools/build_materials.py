#!/usr/bin/env python3
"""Genera materials/index.html y es/materials/index.html a partir de las fuentes."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUENTES = {x["id"]: x for x in json.loads((ROOT / "materiales/fuentes.json").read_text(encoding="utf-8"))}

N3 = [
    ("n3_1", "Inundació i DANA", "L'aigua enganya. Davant d'una inundació, busca altura.",
     "Inundación y DANA", "El agua engaña. Ante una inundación, busca altura."),
    ("n3_2", "Preses i embassaments", "Segueix la ruta segura prevista i mantín el grup unit.",
     "Presas y embalses", "Sigue la ruta segura prevista y mantén el grupo unido."),
    ("n3_3", "Tempesta, vent fort i temporal marítim", "Busca un lloc interior segur i allunya't del que puga caure.",
     "Tormenta, viento fuerte y temporal marítimo", "Busca un lugar interior seguro y aléjate de lo que pueda caer."),
    ("n3_4", "Incendi forestal", "Si veus fum, avisa i segueix la indicació oficial.",
     "Incendio forestal", "Si ves humo, avisa y sigue la indicación oficial."),
    ("n3_5", "Onada de fred, nevades i CO", "Abrida't, evita caigudes i usa la calefacció de forma segura.",
     "Ola de frío, nevadas y CO", "Abrígate, evita caídas y usa la calefacción de forma segura."),
    ("n3_6", "Onada de calor", "Reconeix els senyals, baixa el ritme i busca un lloc fresc.",
     "Ola de calor", "Reconoce las señales, baja el ritmo y busca un lugar fresco."),
    ("n3_7", "Terratrèmol", "Protegeix-te durant el tremolor; després, segueix la indicació del centre.",
     "Terremoto", "Protégete durante el temblor; después, sigue la indicación del centro."),
    ("n3_8", "Risc tecnològic · Evacuació", "Si la instrucció és eixir, segueix la ruta segura indicada.",
     "Riesgo tecnológico · Evacuación", "Si la instrucción es salir, sigue la ruta segura indicada."),
    ("n3_9", "Risc tecnològic · Confinament", "Estar dins és més segur: entra, tanca i informa't.",
     "Riesgo tecnológico · Confinamiento", "Estar dentro es más seguro: entra, cierra e infórmate."),
    ("n3_10", "Pirotècnia", "Disfruta amb distància i respecte.",
     "Pirotécnia", "Disfruta con distancia y respeto."),
    ("n3_11", "Riscos en la llar", "A casa: para, protegeix-te i avisa.",
     "Riesgos en el hogar", "En casa: para, protégete y avisa."),
    ("n3_12", "Esdeveniments multitudinaris", "Grup unit, punt de trobada i eixides clares.",
     "Eventos multitudinarios", "Grupo unido, punto de encuentro y salidas claras."),
    ("n3_13", "Alertes i notícies falses", "Verifica la informació abans de compartir-la.",
     "Alertas y noticias falsas", "Verifica la información antes de compartirla."),
    ("n3_14", "Després de l'emergència", "Seguretat, cura i aprenentatge.",
     "Después de la emergencia", "Seguridad, cuidado y aprendizaje."),
    ("n3_15", "Telefonada a l'1·1·2", "Què dir i qui ajuda.",
     "Llamada al 1·1·2", "Qué decir y quién ayuda."),
]

N1_TITLES = {1: "Em prepare amb Emer! Dins o fora?"}
N2_TITLES = {1: "Missió emergència!"}

TOC = [
    ("Marc d'ús, abast i llenguatge comú", 1, "Marco de uso, alcance y lenguaje común"),
    ("Sistema Nacional de Protecció Civil, alertes i fonts oficials", 3, "Sistema Nacional de Protección Civil, alertas y fuentes oficiales"),
    ("Comunicació accessible i conducció bàsica del grup", 5, "Comunicación accesible y conducción básica del grupo"),
    ("Incendi en interior", 6, "Incendio en interior"),
    ("Inundació i DANA", 8, "Inundación y DANA"),
    ("Preses i embassaments", 10, "Presas y embalses"),
    ("Tempesta, vent fort i temporal marítim", 13, "Tormenta, viento fuerte y temporal marítimo"),
    ("Incendi forestal i interfície urbanoforestal", 15, "Incendio forestal e interfaz urbanoforestal"),
    ("Onada de fred, neu i calefacció", 18, "Ola de frío, nieve y calefacción"),
    ("Onada de calor, radiació solar i activitat física", 21, "Ola de calor, radiación solar y actividad física"),
    ("Terratrèmol", 23, "Terremoto"),
    ("Risc tecnològic", 26, "Riesgo tecnológico"),
    ("Pirotècnia", 28, "Pirotécnia"),
    ("Riscos freqüents a casa", 30, "Riesgos frecuentes en casa"),
    ("Recuperació inicial i suport", 32, "Recuperación inicial y apoyo"),
    ("Annexos operatius", 33, "Anexos operativos"),
    ("Glossari operatiu", 42, "Glosario operativo"),
    ("Referències tècniques bàsiques i bibliografia", 44, "Referencias técnicas básicas y bibliografía"),
]

UI = {
    "va": {
        "lang": "va", "title": "Còmic d'emergències · Protecció Civil",
        "kicker": "MATERIAL OFICIAL · 112CV",
        "h1": "Còmic d'emergències",
        "lead": "Les 15 infografies del Nivell 3, per llegir com un còmic: una pàgina, una emergència. Cada làmina explica què fer abans, durant i després.",
        "tabs": ["Nivell 3", "Nivell 2", "Nivell 1", "Guia"],
        "read": "Llegir la pàgina", "page": "Pàgina", "close": "Tancar",
        "download": "Descarregar l'original", "prev": "Anterior", "next": "Següent",
        "guide": "Guia tècnica del professorat", "guideLead": "51 pàgines de consulta ràpida. Ací tens l'índex i les pàgines clau; el PDF complet està en el botó.",
        "guideBtn": "Obrir la guia (PDF)", "back": "Tornar al curs", "other": "Castellà",
        "note": "Material elaborat per la Generalitat Valenciana (112CV). Distribució gratuïta; es reprodueix amb finalitat educativa i s'enllaça la font original.",
        "count": "15 làmines", "count2": "10 làmines", "count1": "8 làmines",
    },
    "es": {
        "lang": "es", "title": "Cómic de emergencias · Protección Civil",
        "kicker": "MATERIAL OFICIAL · 112CV",
        "h1": "Cómic de emergencias",
        "lead": "Las 15 infografías del Nivel 3, para leer como un cómic: una página, una emergencia. Cada lámina explica qué hacer antes, durante y después.",
        "tabs": ["Nivel 3", "Nivel 2", "Nivel 1", "Guía"],
        "read": "Leer la página", "page": "Página", "close": "Cerrar",
        "download": "Descargar el original", "prev": "Anterior", "next": "Siguiente",
        "guide": "Guía técnica del profesorado", "guideLead": "51 páginas de consulta rápida. Aquí tienes el índice y las páginas clave; el PDF completo está en el botón.",
        "guideBtn": "Abrir la guía (PDF)", "back": "Volver al curso", "other": "Valenciano",
        "note": "Material elaborado por la Generalitat Valenciana (112CV). Distribución gratuita; se reproduce con finalidad educativa y se enlaza la fuente original.",
        "count": "15 láminas", "count2": "10 láminas", "count1": "8 láminas",
    },
}

TEMPLATE = r"""<!doctype html>
<html lang="__LANG__">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
:root{color-scheme:dark;--bg:#0b0f14;--panel:#121922;--line:#222d39;--ink:#e6edf3;--muted:#93a3b1;--accent:#5fa8c0;--blue:#1f5fa8}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"Helvetica Neue",Arial,sans-serif}
a{color:#9fc7e8}
.top{position:sticky;top:0;z-index:20;background:rgba(11,15,20,.9);backdrop-filter:blur(12px);border-bottom:1px solid #1b2530}
.bar{max-width:1280px;margin:0 auto;height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 24px;gap:16px}
.brand{font-weight:800;letter-spacing:.2px;font-size:15px}
.brand small{display:block;color:var(--accent);font-size:11px;letter-spacing:2.5px;font-weight:800}
.links{display:flex;align-items:center;gap:18px;font-size:14px}
.wrap{max-width:1280px;margin:0 auto;padding:0 24px}
.hero{padding:46px 0 8px}
.hero h1{font-size:56px;line-height:1.02;letter-spacing:-2.5px;margin:10px 0 14px}
.hero .lead{color:var(--muted);font-size:18px;line-height:1.55;max-width:780px;margin:0}
.kicker{color:var(--accent);font-size:12px;letter-spacing:3px;font-weight:800}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:28px 0 20px}
.tab{border:1px solid #2a3440;background:#111821;color:#c8d4de;padding:9px 15px;border-radius:999px;cursor:pointer;font-weight:650;font-size:14px}
.tab[aria-selected="true"]{background:var(--blue);border-color:var(--blue);color:#fff}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(265px,1fr));gap:16px;padding-bottom:22px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;cursor:pointer;transition:transform .18s,border-color .18s;text-align:left;color:inherit;font:inherit;padding:0}
.card:hover{transform:translateY(-3px);border-color:#3d5c7c}
.card img{width:100%;display:block;aspect-ratio:16/9;object-fit:cover;background:#0a0e13}
.card .body{padding:12px 15px 16px}
.card .n{font-size:11px;color:var(--accent);font-weight:800;letter-spacing:2px}
.card h3{margin:4px 0 6px;font-size:17px;line-height:1.3}
.card p{margin:0;color:#8fa0ae;font-size:13px;line-height:1.45}
.card .go{display:inline-block;margin-top:10px;font-size:12.5px;color:#9fc7e8}
.guide{display:grid;grid-template-columns:1.05fr .95fr;gap:26px;padding:8px 0 60px}
.guide .cover img{width:100%;border-radius:12px;border:1px solid var(--line);display:block}
.guide .mini{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:12px}
.guide .mini img{width:100%;border-radius:8px;border:1px solid var(--line);display:block;cursor:pointer}
.toc{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 22px}
.toc h2{margin:0 0 12px;font-size:19px}
.toc ol{margin:0;padding-left:20px;color:#b9c7d3;line-height:1.85;font-size:14px}
.toc li b{color:#e6edf3;font-weight:650}
.btn{display:inline-block;background:var(--blue);color:#fff;text-decoration:none;font-weight:750;padding:11px 16px;border-radius:9px;margin-top:16px}
.note{color:#7f8e9b;font-size:12.5px;line-height:1.6;margin-top:18px}
.reader{position:fixed;inset:0;background:rgba(4,7,11,.97);display:none;flex-direction:column;z-index:100}
.reader.open{display:flex}
.rbar{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px 22px;color:#c8d4de}
.rbar .t{font-weight:750;font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rbar .c{font-variant-numeric:tabular-nums;color:#8fa0ae;font-size:13px}
.close{background:none;border:1px solid #2a3440;color:#c8d4de;border-radius:9px;padding:8px 13px;cursor:pointer}
.stage{flex:1;display:flex;align-items:center;justify-content:center;position:relative;padding:0 72px 66px;min-height:0}
.paper{background:#fff;padding:10px;border-radius:6px;box-shadow:0 30px 90px rgba(0,0,0,.65);max-width:min(1420px,94vw);max-height:100%;display:flex;flex-direction:column}
.paper img{display:block;max-width:100%;max-height:calc(100vh - 230px);width:auto;height:auto;margin:0 auto}
.paper .cap{color:#33424f;font-size:12.5px;display:flex;justify-content:space-between;gap:14px;padding:8px 6px 2px}
.paper .cap a{color:#1f5fa8}
.paper.turn{animation:turn .22s ease-out}
@keyframes turn{from{opacity:.35;transform:translateX(26px)}to{opacity:1;transform:none}}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:52px;height:52px;border-radius:50%;border:1px solid #2a3440;background:#121922;color:#fff;font-size:22px;cursor:pointer}
.prev{left:12px}.next{right:12px}
.nav:disabled{opacity:.22;cursor:default}
.dots{display:flex;gap:6px;justify-content:center;padding:0 0 14px;flex-wrap:wrap}
.dot{width:7px;height:7px;border-radius:4px;background:#2a3440}
.dot.on{background:var(--accent)}
@media(max-width:800px){.hero h1{font-size:38px}.guide{grid-template-columns:1fr}.stage{padding:0 10px 58px}.nav{width:42px;height:42px}.paper img{max-height:calc(100vh - 210px)}.links a.hide{display:none}}
</style>
<body>
<header class="top"><div class="bar">
  <div class="brand"><small>112 · PROTECCIÓ CIVIL</small>__H1__</div>
  <div class="links">
    <a href="__COURSE__">← __BACK__</a>
    <a href="__OTHER__" hreflang="__OTHERLANG__">__OTHERLABEL__</a>
  </div>
</div></header>

<main class="wrap">
  <section class="hero">
    <div class="kicker">__KICKER__</div>
    <h1>__H1__</h1>
    <p class="lead">__LEAD__</p>
    <div class="tabs" role="tablist" aria-label="Nivells">
      <button class="tab" role="tab" data-list="n3" aria-selected="true">__TAB3__ · __C3__</button>
      <button class="tab" role="tab" data-list="n2" aria-selected="false">__TAB2__ · __C2__</button>
      <button class="tab" role="tab" data-list="n1" aria-selected="false">__TAB1__ · __C1__</button>
      <button class="tab" role="tab" data-list="guia" aria-selected="false">__TABG__</button>
    </div>
    <div id="grid" class="grid"></div>
    <section id="guia" class="guide" hidden>
      <div class="cover">
        <img src="__ASSET__guia/p1-01.webp" alt="Portada de la guia tècnica">
        <div class="mini">
          <img src="__ASSET__guia/p9-09.webp" alt="Pàgina de mostra de la guia" data-pdf="1">
          <img src="__ASSET__guia/p37-37.webp" alt="Pàgina d'annexos de la guia" data-pdf="1">
          <img src="__ASSET__guia/p11-11.webp" alt="Pàgina de mostra de la guia" data-pdf="1">
        </div>
        <div class="mini" style="grid-template-columns:repeat(2,1fr)">
          <a href="__DIPTICO__" target="_blank" rel="noopener"><img src="__ASSET__misc/diptico-1.webp" alt="Díptic Inundacions, com protegir-nos"></a>
          <a href="__CARTELL__" target="_blank" rel="noopener"><img src="__ASSET__misc/cartell.webp" alt="Cartell Inundacions, com protegir-nos"></a>
        </div>
      </div>
      <div class="toc">
        <h2>__GUIDE__</h2>
        <p class="note" style="margin-top:0">__GUIDELEAD__</p>
        <ol>__TOC__</ol>
        <a class="btn" href="__GUIDEPDF__" target="_blank" rel="noopener">__GUIDEBTN__</a>
        <p class="note">__NOTE__</p>
      </div>
    </section>
    <p class="note" id="foot">__NOTE__</p>
  </section>
</main>

<div class="reader" id="reader" role="dialog" aria-modal="true" aria-labelledby="rt">
  <div class="rbar">
    <div class="t" id="rt"></div>
    <div class="c" id="rc"></div>
    <button class="close" id="rclose">__CLOSE__ ✕</button>
  </div>
  <div class="stage" id="stage">
    <button class="nav prev" id="rprev" aria-label="__PREV__">‹</button>
    <div class="paper" id="paper">
      <img id="rimg" alt="">
      <div class="cap"><span id="rdesc"></span><a id="rsrc" href="#" target="_blank" rel="noopener">__DOWNLOAD__</a></div>
    </div>
    <button class="nav next" id="rnext" aria-label="__NEXT__">›</button>
  </div>
  <div class="dots" id="rdots"></div>
</div>

<script>
const DATA = __DATA__;
const ASSET = "__ASSET__";
const UI = __UI__;
let listName = "n3", index = 0;

const $ = (s) => document.querySelector(s);
const grid = $("#grid");
const guide = $("#guia");
const reader = $("#reader");
const paper = $("#paper");
const img = $("#rimg");

function card(item) {
  const el = document.createElement("button");
  el.className = "card";
  el.type = "button";
  el.innerHTML = '<img loading="lazy" src="' + ASSET + item.thumb + '" alt="' + item.alt + '">' +
    '<div class="body"><div class="n">' + item.n + '</div><h3>' + item.title + '</h3>' +
    '<p>' + (item.desc || "") + '</p><span class="go">' + UI.read + ' →</span></div>';
  el.addEventListener("click", () => openReader(item.list, item.i));
  return el;
}

function renderGrid(name) {
  listName = name;
  document.querySelectorAll(".tab").forEach(t => t.setAttribute("aria-selected", String(t.dataset.list === name)));
  const isGuide = name === "guia";
  guide.hidden = !isGuide;
  grid.hidden = isGuide;
  $("#foot").hidden = isGuide;
  if (isGuide) return;
  grid.innerHTML = "";
  DATA[name].forEach(item => grid.appendChild(card(item)));
}

function openReader(name, i) {
  listName = name; index = i;
  reader.classList.add("open");
  history.replaceState(null, "", "#" + DATA[name][i].id);
  render();
  $("#rclose").focus();
}

function closeReader() {
  reader.classList.remove("open");
  history.replaceState(null, "", location.pathname + location.search);
}

function render() {
  const arr = DATA[listName];
  const it = arr[index];
  img.src = ASSET + it.img;
  img.alt = it.alt;
  $("#rt").textContent = it.title;
  $("#rc").textContent = (index + 1) + " / " + arr.length;
  $("#rdesc").textContent = it.desc || "";
  $("#rsrc").href = it.src || "#";
  $("#rprev").disabled = index === 0;
  $("#rnext").disabled = index === arr.length - 1;
  const dots = $("#rdots");
  dots.innerHTML = "";
  arr.forEach((_, n) => {
    const d = document.createElement("span");
    d.className = "dot" + (n === index ? " on" : "");
    dots.appendChild(d);
  });
  paper.classList.remove("turn");
  void paper.offsetWidth;
  paper.classList.add("turn");
  const next = arr[index + 1], prev = arr[index - 1];
  if (next) new Image().src = ASSET + next.img;
  if (prev) new Image().src = ASSET + prev.img;
}

function go(delta) {
  const arr = DATA[listName];
  const n = index + delta;
  if (n < 0 || n >= arr.length) return;
  index = n;
  history.replaceState(null, "", "#" + arr[index].id);
  render();
}

document.querySelectorAll(".tab").forEach(t => t.addEventListener("click", () => renderGrid(t.dataset.list)));
$("#rprev").addEventListener("click", () => go(-1));
$("#rnext").addEventListener("click", () => go(1));
$("#rclose").addEventListener("click", closeReader);
reader.addEventListener("click", (e) => { if (e.target === reader) closeReader(); });
document.addEventListener("keydown", (e) => {
  if (!reader.classList.contains("open")) return;
  if (e.key === "Escape") closeReader();
  if (e.key === "ArrowLeft") go(-1);
  if (e.key === "ArrowRight") go(1);
});
let tx = 0;
$("#stage").addEventListener("touchstart", (e) => { tx = e.touches[0].clientX; }, {passive: true});
$("#stage").addEventListener("touchend", (e) => {
  const dx = e.changedTouches[0].clientX - tx;
  if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1);
}, {passive: true});
document.querySelectorAll("[data-pdf]").forEach(el => el.addEventListener("click", () => window.open("__GUIDEPDF__", "_blank")));

const h = decodeURIComponent(location.hash.slice(1));
if (h) {
  if (h === "guia") { renderGrid("guia"); guide.scrollIntoView({behavior: "smooth"}); }
  else {
    for (const k in DATA) {
      const i = DATA[k].findIndex(x => x.id === h);
      if (i >= 0) { renderGrid(k); openReader(k, i); break; }
    }
  }
} else {
  renderGrid("n3");
}
</script>
</body>
</html>
"""


def build(lang: str) -> str:
    ui = UI[lang]
    asset = "../assets/materials/" if lang == "va" else "../../assets/materials/es/"
    course = "../index.html" if lang == "va" else "../index.html"
    other = "../es/materials/index.html" if lang == "va" else "../../materials/index.html"
    otherlang = "es" if lang == "va" else "va"

    data = {"n3": [], "n2": [], "n1": []}
    for i, (sid, tva, dva, tes, des) in enumerate(N3, 1):
        data["n3"].append({
            "id": sid.replace("_", "-"), "n": f"{i:02d}", "title": tva if lang == "va" else tes,
            "desc": dva if lang == "va" else des,
            "alt": (tva if lang == "va" else tes) + " · infografia oficial del 112CV",
            "img": f"n3/full/{sid}.webp", "thumb": f"n3/thumb/{sid}.webp",
            "src": FUENTES[sid]["href"], "list": "n3", "i": i - 1,
        })
    for n in range(1, 11):
        title = N2_TITLES.get(n, ("Infografia N2 · pàgina " if lang == "va" else "Infografía N2 · página ") + str(n))
        data["n2"].append({
            "id": f"n2-{n}", "n": f"{n:02d}", "title": title, "desc": "",
            "alt": title + " · 112CV", "img": f"n2/full/{n:02d}.webp", "thumb": f"n2/thumb/{n:02d}.webp",
            "src": FUENTES["inf2"]["href"], "list": "n2", "i": n - 1,
        })
    for n in range(1, 9):
        title = N1_TITLES.get(n, ("Infografia N1 · pàgina " if lang == "va" else "Infografía N1 · página ") + str(n))
        data["n1"].append({
            "id": f"n1-{n}", "n": f"{n:02d}", "title": title, "desc": "",
            "alt": title + " · 112CV", "img": f"n1/full/{n}.webp", "thumb": f"n1/thumb/{n}.webp",
            "src": FUENTES["inf1"]["href"], "list": "n1", "i": n - 1,
        })

    toc = "".join(f"<li><b>{t[0] if lang == 'va' else t[2]}</b> · p. {t[1]}</li>" for t in TOC)
    pdf = FUENTES["guia"]["href"] if lang == "va" else "https://www.112cv.gva.es/documents/163565706/413620410/Guia+cas+DIGITAL+05-08.pdf/518e48e1-ae85-0e40-6a57-bd344ed3a7a2?t=1786354187342"
    h1 = ui["h1"]

    html = (TEMPLATE
            .replace("__LANG__", lang)
            .replace("__TITLE__", ui["title"])
            .replace("__KICKER__", ui["kicker"])
            .replace("__H1__", h1)
            .replace("__LEAD__", ui["lead"])
            .replace("__TAB3__", ui["tabs"][0]).replace("__TAB2__", ui["tabs"][1])
            .replace("__TAB1__", ui["tabs"][2]).replace("__TABG__", ui["tabs"][3])
            .replace("__C3__", ui["count"]).replace("__C2__", ui["count2"]).replace("__C1__", ui["count1"])
            .replace("__GUIDE__", ui["guide"]).replace("__GUIDELEAD__", ui["guideLead"])
            .replace("__GUIDEBTN__", ui["guideBtn"]).replace("__TOC__", toc)
            .replace("__NOTE__", ui["note"]).replace("__BACK__", ui["back"])
            .replace("__OTHER__", other).replace("__OTHERLABEL__", ui["other"]).replace("__OTHERLANG__", otherlang)
            .replace("__COURSE__", course).replace("__ASSET__", asset)
            .replace("__CLOSE__", ui["close"]).replace("__DOWNLOAD__", ui["download"])
            .replace("__PREV__", ui["prev"]).replace("__NEXT__", ui["next"])
            .replace("__GUIDEPDF__", pdf)
            .replace("__DIPTICO__", FUENTES["diptico"]["href"])
            .replace("__CARTELL__", FUENTES["cartell"]["href"])
            .replace("__DATA__", json.dumps(data, ensure_ascii=False))
            .replace("__UI__", json.dumps(ui, ensure_ascii=False)))
    return html


def main() -> None:
    (ROOT / "materials").mkdir(parents=True, exist_ok=True)
    (ROOT / "es/materials").mkdir(parents=True, exist_ok=True)
    (ROOT / "materials/index.html").write_text(build("va"), encoding="utf-8")
    (ROOT / "es/materials/index.html").write_text(build("es"), encoding="utf-8")
    print("OK · materials/index.html + es/materials/index.html")


if __name__ == "__main__":
    main()
