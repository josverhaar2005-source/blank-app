import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="VKP Verschillen Dashboard", layout="wide")

people = [
    {"id": "alexander", "name": "Alexander", "role": "Vuren: BIM-engineer & Innovatie"},
    {"id": "mark", "name": "Mark", "role": "Vuren: Bedrijfsleider & Hoofd tekenkamer"},
    {"id": "micha", "name": "Micha", "role": "Vuren: Projectleider"},
    {"id": "jasper", "name": "Jasper", "role": "Vuren: Productieleider"},
    {"id": "leo", "name": "Leo", "role": "Vuren: BIM-engineer"},
    {"id": "demi", "name": "Demi", "role": "Vuren: BIM-engineer"},
    {"id": "patrick", "name": "Patrick", "role": "Kapelle: Calculator"},
    {"id": "martijn", "name": "Martijn", "role": "Kapelle: BIM-engineer"},
    {"id": "julian", "name": "Julian", "role": "Kapelle: BIM-engineer & Innovatie"},
    {"id": "willem", "name": "Willem", "role": "Kapelle: BIM-engineer / werkvoorbereider"},
]

main_rows = [
    {"id": 1, "cat": "A", "vuren": "Medewerkers werken vestigingbreed goed samen.", "kapelle": "Medewerkers werken vestigingbreed minder goed samen.", "toelichting": "Samenwerking tussen locaties"},
    {"id": 2, "cat": "A", "vuren": "Draait productie voor projecten die zowel in Vuren als Kapelle zijn gemodelleerd.", "kapelle": "Draait uitsluitend productie voor projecten die in Kapelle zijn gemodelleerd.", "toelichting": "Herkomst van projecten in productie"},
    {"id": 3, "cat": "A", "vuren": "Focust zich op de relatief kleinere projecten, zoals woningbouw met prefab daken.", "kapelle": "Focust zich op de relatief grotere en complexere projecten zonder prefab daken.", "toelichting": "Type projecten per vestiging"},
    {"id": 4, "cat": "C", "vuren": "Geen calculatie", "kapelle": "Wel calculatie", "toelichting": "Aanwezigheid van calculatie op locatie"},
    {"id": 5, "cat": "E", "vuren": "Werkt soms een 3D-fragment uit tijdens het 2D-tekenwerk.", "kapelle": "Werkt altijd een 3D-fragment uit tijdens het 2D-tekenwerk.", "toelichting": "Mate van 3D-gebruik tijdens 2D-uitwerking"},
    {"id": 6, "cat": "E", "vuren": "Maakt gebruik van externe constructeur Cerfix.", "kapelle": "Maakt gebruik van een andere vaste externe constructeur (zzp'er).", "toelichting": "Vaste externe constructeur"},
    {"id": 7, "cat": "E", "vuren": "Projectleider organiseert losse kick-offs met de calculator en later met de BIM-engineer.", "kapelle": "Er vindt één kick-off plaats met de BIM-engineer en calculator.", "toelichting": "Opzet van de kick-off"},
    {"id": 8, "cat": "E", "vuren": "De projectleider vraagt alle projectspecifieke offertes op.", "kapelle": "De projectleider en/of de werkvoorbereider vraagt alle projectspecifieke offertes op.", "toelichting": "Verantwoordelijkheid projectspecifieke offertes"},
    {"id": 9, "cat": "E", "vuren": "Hoger engineeringsniveau. (door 2 zeer ervaren BIM-engineers)", "kapelle": "Lager engineeringsniveau", "toelichting": "Engineeringsniveau"},
    {"id": 10, "cat": "E", "vuren": "De BIM-engineer onderhoudt rechtstreeks contact met de werkvoorbereiding van de opdrachtgever.", "kapelle": "De projectleider/werkvoorbereider heeft meer contact met de opdrachtgever en ontlast daarin de BIM-engineer.", "toelichting": "Contact met opdrachtgever"},
    {"id": 11, "cat": "E", "vuren": "Projectteam bestaat uit projectleider en BIM-engineer", "kapelle": "Projectteam bestaat uit projectleider, werkvoorbereider & BIM-engineer", "toelichting": "Samenstelling projectteam"},
    {"id": 12, "cat": "E", "vuren": "Tekla Bibliotheek Vuren.", "kapelle": "Tekla Bibliotheek Kapelle.", "toelichting": "Gebruikte Tekla-bibliotheek"},
    {"id": 13, "cat": "E", "vuren": "Exporteert geen BTL-SAM-bestanden.", "kapelle": "Het exporteren van BTL-SAM-bestanden voor zowel de steenstriprobot als het PMS-systeem.", "toelichting": "Export van BTL-SAM-bestanden"},
    {"id": 14, "cat": "E", "vuren": "BIM-engineer maakt uittrekstaten vanuit Tekla van de te bestellen materialen voor de inkoop. Inkoper heeft geen technische kennis en bestelt zonder inhoudelijke controle.", "kapelle": "Werkvoorbereider productie haalt uit Trimble Connect de uittrekstaten en bestelt de materialen. Hierbij heeft de werkvoorbereider productie wel technische kennis.", "toelichting": "Proces van materiaalbestellingen"},
    {"id": 15, "cat": "E", "vuren": "Werkt niet met het basisformat van Kapelle in Tekla Structures, omdat het te complex en foutgevoelig is.", "kapelle": "Werkt met een ver doorontwikkeld basisformat in Tekla Structures.", "toelichting": "Gebruik van basisformat in Tekla"},
    {"id": 16, "cat": "E", "vuren": "Wordt geëngineerd zodat het goed en makkelijk geproduceerd kan worden.", "kapelle": "Wordt geëngineerd naar de wens van de opdrachtgever.", "toelichting": "Uitgangspunt van engineering"},
    {"id": 17, "cat": "E", "vuren": "Engineert met alle mogelijke kopmaten, net wat handig uitkomt in het detail.", "kapelle": "Engineert door gebruik te maken van standaard kopmaten.", "toelichting": "Gebruik van kopmaten"},
    {"id": 18, "cat": "E", "vuren": "2D-tekeningen zijn gekoppeld aan het 3D-model.", "kapelle": "2D-tekeningen zijn niet gekoppeld aan het 3D-model omdat het model dan te zwaar gevonden wordt en onhandig is richting de opdrachtgever.", "toelichting": "Koppeling 2D-tekeningen aan 3D-model"},
    {"id": 19, "cat": "P", "vuren": "P&O & Inkoop is verantwoordelijk voor de bestellingen van materialen.", "kapelle": "Werkvoorbereider productie is verantwoordelijk voor de bestellingen van materialen.", "toelichting": "Verantwoordelijkheid voor materiaalbestellingen"},
    {"id": 20, "cat": "P", "vuren": "De productieplanning is inzichtelijk voor het productiepersoneel.", "kapelle": "Productieplanning is niet inzichtelijk voor het productiepersoneel.", "toelichting": "Transparantie van de productieplanning"},
    {"id": 21, "cat": "P", "vuren": "De productieleider heeft contact met de inkoop betreft het bestellen van materialen.", "kapelle": "De werkvoorbereider heeft contact met de inkoop betreft het bestellen van materialen.", "toelichting": "Afstemming met inkoop over materiaalbestellingen"},
    {"id": 22, "cat": "P", "vuren": "De productie heeft weinig voorraad van materialen waardoor problemen moeilijk kunnen worden opgelost.", "kapelle": "De productie van Kapelle heeft een redelijke voorraad van materialen waardoor kleine problemen eenvoudig kunnen worden opgelost.", "toelichting": "Beschikbare materiaalvoorraad in productie"},
    {"id": 23, "cat": "P", "vuren": "De productie legt de meeste fouten van de engineering terug bij de engineering.", "kapelle": "De productie lost de meeste problemen van de engineering zelf op.", "toelichting": "Omgang met fouten vanuit engineering"},
    {"id": 24, "cat": "P", "vuren": "Productieleider maakt bokkenschema's.", "kapelle": "Werkvoorbereider productie maakt bokkenschema's.", "toelichting": "Verantwoordelijkheid voor bokkenschema's"},
]

shared_rows = [
    {"id": 101, "onderwerp": "Prioritering engineering vs productie", "toelichting": "Soms wordt engineering afgerond om productie te starten, terwijl in andere gevallen projecten juist worden voorgetrokken voor controle door de opdrachtgever"},
    {"id": 102, "onderwerp": "Start 3D-tekenwerk", "toelichting": "Afhankelijk van de situatie wordt gewacht op feedback van de opdrachtgever voordat gestart wordt met het volledige 3D-tekenwerk"},
    {"id": 103, "onderwerp": "Opzet 3D-modellen", "toelichting": "3D-tekenwerk wordt soms opgezet op basis van eerdere projecten en soms met behulp van de module VKP Frame"},
    {"id": 104, "onderwerp": "Kwaliteit projectinformatie", "toelichting": "Projectaanvragen bevatten doorgaans architect- en constructeurstekeningen, maar de kwaliteit en volledigheid varieert per project; grotere aannemers leveren vaak betere informatie, terwijl kleinere partijen vaker onvolledig zijn (bijv. ontbreken van 3D- of DWG-bestanden)"},
    {"id": 105, "onderwerp": "Mate van zelfstandigheid engineers", "toelichting": "Ervaren engineers werken zelfstandiger richting de opdrachtgever, terwijl minder ervaren engineers vaker ondersteuning krijgen van projectleider of werkvoorbereider"},
]

counts = {"A": 0, "C": 0, "E": 0, "P": 0}
for row in main_rows:
    counts[row["cat"]] += 1

payload = {
    "people": people,
    "mainRows": main_rows,
    "sharedRows": shared_rows,
    "counts": counts,
}

html = f"""
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    :root {{
      --bg: #1a1a1a;
      --panel: #2a2b2e;
      --card: #333438;
      --line: #4b5563;
      --text: #f9fafb;
      --muted: #d1d5db;
      --accent: #fff200;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--bg); color: var(--text); font-family: Inter, Arial, sans-serif; }}
    .wrap {{ max-width: 1600px; margin: 0 auto; padding: 24px; }}
    h1 {{ color: var(--accent); font-size: 2rem; margin: 0 0 18px; }}
    .sub {{ color: var(--muted); margin-bottom: 22px; }}

    .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 22px; }}
    .stat {{ background: linear-gradient(145deg, #36373b, #2d2e31); border: 1px solid #444850; border-radius: 16px; padding: 14px; box-shadow: 0 8px 20px rgba(0,0,0,.2); }}
    .stat .title {{ color: var(--accent); font-weight: 700; }}
    .stat .count {{ color: var(--muted); font-size: .9rem; margin-top: 4px; }}

    .table {{ background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 14px; box-shadow: 0 10px 24px rgba(0,0,0,.22); }}
    .header, .row {{ display: grid; gap: 10px; align-items: start; }}
    .header {{ color: var(--accent); font-weight: 700; font-size: .95rem; padding: 4px 12px 12px; border-bottom: 1px solid var(--line); margin-bottom: 12px; }}
    .main-cols {{ grid-template-columns: .6fr 1.5fr 1.5fr 2.2fr 1.1fr .8fr; }}
    .shared-cols {{ grid-template-columns: 1.3fr 2.6fr 1.1fr .8fr; }}

    .item {{ background: var(--card); border: 1px solid var(--line); border-radius: 14px; overflow: hidden; margin-bottom: 10px; }}
    .row {{ padding: 12px; }}
    .muted {{ color: var(--muted); font-size: .86rem; }}
    .cat-pill {{ display:inline-block; min-width: 30px; text-align: center; border-radius: 999px; padding: 4px 10px; background:#1f2937; font-weight:700; }}

    .badge {{ display: inline-block; padding: 5px 10px; border-radius: 10px; font-weight: 700; color: #111827; }}
    .low {{ background: #fecaca; }}
    .medium {{ background: #fde68a; }}
    .high {{ background: #bbf7d0; }}

    .toggle {{ background: transparent; border: 0; color: var(--accent); cursor: pointer; text-decoration: underline; font-weight: 600; padding: 0; }}

    .mentions {{ display: none; background: #232427; border-top: 1px solid var(--line); padding: 12px; }}
    .mentions-grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:10px; }}
    .person {{ background: #323338; border-radius: 12px; border: 1px solid #41444b; padding: 10px; display: flex; gap: 9px; cursor: pointer; }}
    .person input {{ margin-top: 3px; accent-color: #fff200; }}
    .person strong {{ color: var(--accent); display:block; margin-bottom: 2px; }}

    h2 {{ color: var(--accent); margin: 24px 0 12px; }}
    @media (max-width: 1080px) {{
      .main-cols, .shared-cols {{ grid-template-columns: 1fr; }}
      .header {{ display:none; }}
      .row > div::before {{ content: attr(data-label); display:block; color: var(--accent); font-size:.75rem; margin-bottom: 4px; text-transform: uppercase; letter-spacing: .04em; }}
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Overzicht verschillen tussen VKP Vuren en VKP Kapelle</h1>
    <div class="sub">Interactieve HTML-weergave met consensus per verschil op basis van aangevinkte interviews.</div>

    <div class="stats" id="stats"></div>

    <div class="table">
      <div class="header main-cols">
        <div>Cat</div><div>VKP Vuren</div><div>VKP Kapelle</div><div>Toelichting</div><div>Consensus</div><div>Onderbouwing</div>
      </div>
      <div id="main-table"></div>
    </div>

    <h2>Gezamenlijke verschillen</h2>
    <div class="table">
      <div class="header shared-cols">
        <div>Onderwerp</div><div>Toelichting</div><div>Consensus</div><div>Onderbouwing</div>
      </div>
      <div id="shared-table"></div>
    </div>
  </div>

  <script>
    const data = {json.dumps(payload, ensure_ascii=False)};
    const allRows = [...data.mainRows, ...data.sharedRows];
    const state = Object.fromEntries(allRows.map(r => [r.id, {{ mentions: {{}} }}]));

    function consensusFor(rowId) {{
      const total = data.people.length;
      const checked = Object.values(state[rowId].mentions).filter(Boolean).length;
      const percentage = total ? Math.round((checked / total) * 100) : 0;
      let label = "Laag";
      if (percentage >= 70) label = "Hoog";
      else if (percentage >= 40) label = "Middel";
      return {{ total, checked, percentage, label }};
    }}

    function badgeClass(label) {{
      if (label === "Hoog") return "high";
      if (label === "Middel") return "medium";
      return "low";
    }}

    function mentionPanel(rowId) {{
      const wrap = document.createElement("div");
      wrap.className = "mentions";
      wrap.id = `mentions-${{rowId}}`;
      const grid = document.createElement("div");
      grid.className = "mentions-grid";

      data.people.forEach(person => {{
        const label = document.createElement("label");
        label.className = "person";

        const check = document.createElement("input");
        check.type = "checkbox";
        check.addEventListener("change", () => {{
          state[rowId].mentions[person.id] = check.checked;
          refreshConsensus(rowId);
        }});

        const content = document.createElement("div");
        content.innerHTML = `<strong>${{person.name}}</strong><span class="muted">${{person.role}}</span>`;

        label.append(check, content);
        grid.appendChild(label);
      }});

      wrap.appendChild(grid);
      return wrap;
    }}

    function buildMainTable() {{
      const host = document.getElementById("main-table");
      data.mainRows.forEach(row => {{
        const box = document.createElement("div");
        box.className = "item";

        const c = consensusFor(row.id);
        const line = document.createElement("div");
        line.className = "row main-cols";
        line.innerHTML = `
          <div data-label="Cat"><span class="cat-pill">${{row.cat}}</span></div>
          <div data-label="VKP Vuren">${{row.vuren}}</div>
          <div data-label="VKP Kapelle">${{row.kapelle}}</div>
          <div data-label="Toelichting">${{row.toelichting}}</div>
          <div data-label="Consensus">
            <span id="badge-${{row.id}}" class="badge ${{badgeClass(c.label)}}">${{c.label}}</span>
            <div id="meta-${{row.id}}" class="muted">${{c.checked}}/${{c.total}} interviews (${{c.percentage}}%)</div>
          </div>
          <div data-label="Onderbouwing"><button class="toggle" data-row="${{row.id}}">Openen</button></div>
        `;

        box.append(line, mentionPanel(row.id));
        host.appendChild(box);
      }});
    }}

    function buildSharedTable() {{
      const host = document.getElementById("shared-table");
      data.sharedRows.forEach(row => {{
        const box = document.createElement("div");
        box.className = "item";

        const c = consensusFor(row.id);
        const line = document.createElement("div");
        line.className = "row shared-cols";
        line.innerHTML = `
          <div data-label="Onderwerp">${{row.onderwerp}}</div>
          <div data-label="Toelichting">${{row.toelichting}}</div>
          <div data-label="Consensus">
            <span id="badge-${{row.id}}" class="badge ${{badgeClass(c.label)}}">${{c.label}}</span>
            <div id="meta-${{row.id}}" class="muted">${{c.checked}}/${{c.total}} interviews (${{c.percentage}}%)</div>
          </div>
          <div data-label="Onderbouwing"><button class="toggle" data-row="${{row.id}}">Openen</button></div>
        `;

        box.append(line, mentionPanel(row.id));
        host.appendChild(box);
      }});
    }}

    function buildStats() {{
      const stats = [
        ["A - Algemeen", data.counts.A],
        ["C - Calculatie", data.counts.C],
        ["E - Engineering", data.counts.E],
        ["P - Productie", data.counts.P],
      ];

      const host = document.getElementById("stats");
      stats.forEach(([title, count]) => {{
        const item = document.createElement("div");
        item.className = "stat";
        item.innerHTML = `<div class="title">${{title}}</div><div class="count">${{count}} verschillen</div>`;
        host.appendChild(item);
      }});
    }}

    function refreshConsensus(rowId) {{
      const c = consensusFor(rowId);
      const badge = document.getElementById(`badge-${{rowId}}`);
      const meta = document.getElementById(`meta-${{rowId}}`);
      badge.className = `badge ${{badgeClass(c.label)}}`;
      badge.textContent = c.label;
      meta.textContent = `${{c.checked}}/${{c.total}} interviews (${{c.percentage}}%)`;
    }}

    function wireToggles() {{
      document.querySelectorAll(".toggle").forEach(btn => {{
        btn.addEventListener("click", () => {{
          const rowId = btn.dataset.row;
          const panel = document.getElementById(`mentions-${{rowId}}`);
          const isOpen = panel.style.display === "block";
          panel.style.display = isOpen ? "none" : "block";
          btn.textContent = isOpen ? "Openen" : "Sluiten";
        }});
      }});
    }}

    buildStats();
    buildMainTable();
    buildSharedTable();
    wireToggles();
  </script>
</body>
</html>
"""

components.html(html, height=1800, scrolling=True)
