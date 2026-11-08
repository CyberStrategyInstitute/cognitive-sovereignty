"use strict";
(() => {
  const script = [...document.scripts].find((s) =>
    /\/assets\/practice\.js/.test(s.src),
  );
  const base = new URL("../", script.src);
  const repo =
    "https://github.com/CyberStrategyInstitute/cognitive-sovereignty/blob/main/";
  const node = (tag, text, cls) => {
    const el = document.createElement(tag);
    if (text !== undefined) el.textContent = String(text);
    if (cls) el.className = cls;
    return el;
  };
  const link = (label, path) => {
    const a = node("a", label);
    a.href = path.startsWith("https://") ? path : new URL(path, base).href;
    return a;
  };
  const read = async (name) => {
    const r = await fetch(new URL("data/" + name + ".json", base));
    if (!r.ok) throw new Error("Data unavailable");
    return r.json();
  };
  const domainNumber = (id) => Number(id.slice(1));
  let controls = [],
    domains = [],
    readinessData = { results: [] };
  function controlCard(c, compact = false) {
    const card = node("article", undefined, "card");
    card.id = c.id;
    card.append(
      node("p", c.id + " Ã‚Â· " + c.domain_id + " Ã‚Â· " + c.kind, "eyebrow"),
      node("h3", c.name),
      node("p", c.implementation),
    );
    if (!compact) {
      card.append(
        node("h4", "Expected outcome"),
        node("p", c.expected_outcome),
        node("h4", "Check"),
        node("p", c.test),
        node("h4", "If it fails"),
        node("p", c.failure_response),
        node("p", "Owner role: " + c.owner_role + ". " + c.evidence_status),
      );
      card.append(
        node("p", "Why: " + c.rationale),
        link(
          "Related watch and action signals",
          "research.html?signal=" + encodeURIComponent(c.id) + "#signals",
        ),
      );
    }
    card.append(node("p", "Threats: " + c.taxonomy.join(", ")));
    for (const note of c.research_notes) {
      const p = node("p");
      p.append(link(note.split("/").pop(), repo + note));
      card.append(p);
    }
    return card;
  }
  function summary() {
    for (const container of document.querySelectorAll(
      "[data-domain-summary]",
    )) {
      container.replaceChildren();
      container.classList.add("csf-domain-cards");
      for (const d of domains) {
        const selected = controls.filter((c) => c.domain_id === d.id);
        const refined = selected.filter((c) => c.kind === "refined").length;
        const card = node("article", undefined, "card");
        card.append(
          node("h3", d.id + " Ã‚Â· " + d.name),
          node(
            "p",
            d.baseline_controls.length +
              " retained Ã‚Â· " +
              refined +
              " refined Ã‚Â· " +
              d.extension_controls.length +
              " added",
          ),
          node(
            "p",
            "Readiness: unknown. No observed unit results supplied.",
            "muted",
          ),
        );
        const observed = readinessData.results
          .slice()
          .sort((a, b) => b.assessment_date.localeCompare(a.assessment_date));
        if (observed.length) {
          const latest = observed[0];
          const result = latest.domains.find((row) => row.domain_id === d.id);
          const value = (profile) =>
            result.profiles[profile].score === null
              ? "unknown"
              : result.profiles[profile].score + "/100";
          card.querySelector(".muted").textContent =
            "Latest scoped assessment " +
            latest.assessment_date +
            ": inherited " +
            value("legacy-v1") +
            ", research extension " +
            value("research-extension-v1") +
            ". Scope: " +
            latest.scope;
        }
        card.append(
          link(
            "Inspect domain controls",
            "practice.html?domain=" + d.id + "#controls",
          ),
        );
        container.append(card);
      }
    }
    const selector = document.getElementById("control-domain");
    if (selector)
      for (const d of domains)
        selector.append(new Option(d.id + " Ã‚Â· " + d.name, d.id));
  }
  function showControls() {
    const list = document.getElementById("control-list");
    if (!list) return;
    const value = (id) => document.getElementById(id).value;
    const search = value("control-search").trim().toLocaleLowerCase();
    const rows = controls.filter(
      (c) =>
        (!value("control-domain") || c.domain_id === value("control-domain")) &&
        (!value("control-kind") || c.kind === value("control-kind")) &&
        JSON.stringify(c).toLocaleLowerCase().includes(search),
    );
    const mode = value("control-sort");
    rows.sort((a, b) =>
      mode === "name"
        ? a.name.localeCompare(b.name)
        : mode === "id"
          ? a.id.localeCompare(b.id)
          : mode === "change"
            ? ["added", "refined", "inherited"].indexOf(a.kind) -
                ["added", "refined", "inherited"].indexOf(b.kind) ||
              a.id.localeCompare(b.id)
            : domainNumber(a.domain_id) - domainNumber(b.domain_id) ||
              a.id.localeCompare(b.id),
    );
    list.replaceChildren(...rows.map((c) => controlCard(c)));
    document.getElementById("control-results").textContent =
      rows.length +
      " of " +
      controls.length +
      " controls shown. Guidance is not field validation.";
  }
  function showTechnique(id) {
    const body = document.getElementById("dp-body");
    if (!body) return;
    let box = document.getElementById("related-research-controls");
    if (!box) {
      box = node("section");
      box.id = "related-research-controls";
      box.className = "csf-related-controls";
      body.append(box);
    }
    box.replaceChildren(node("h3", "Research-linked catalog controls"));
    const matches = controls.filter((c) => c.taxonomy.includes(id));
    if (!matches.length)
      box.append(
        node(
          "p",
          "No exact catalog mapping is recorded. Review the mechanism before adding a control.",
        ),
      );
    for (const c of matches) {
      const p = node("p");
      p.append(
        link(
          c.id + " Ã‚Â· " + c.name,
          "practice.html?control=" + encodeURIComponent(c.id) + "#controls",
        ),
      );
      box.append(p);
    }
    box.append(
      node(
        "p",
        "These are documented checks, not measured mitigation effectiveness.",
      ),
    );
  }
  window.CSFPractice = { showTechnique };
  async function init() {
    try {
      [controls, domains, readinessData] = await Promise.all([
        read("controls"),
        read("domains"),
        read("readiness"),
      ]);
      summary();
      if (document.getElementById("control-list")) {
        const params = new URLSearchParams(location.search);
        const domain = params.get("domain");
        if (domains.some((d) => d.id === domain))
          document.getElementById("control-domain").value = domain;
        if (params.get("control"))
          document.getElementById("control-search").value =
            params.get("control");
        for (const id of [
          "control-search",
          "control-domain",
          "control-kind",
          "control-sort",
        ])
          document
            .getElementById(id)
            .addEventListener(
              id === "control-search" ? "input" : "change",
              showControls,
            );
        showControls();
        const [resources, roadmap, readiness] = await Promise.all([
          read("resources"),
          read("roadmap"),
          read("readiness"),
        ]);
        for (const r of resources) {
          const card = node("article", undefined, "card");
          card.append(
            node("h3", r.title),
            node("p", r.outcome),
            link("Open resource", repo + r.path),
          );
          document.getElementById("resource-list").append(card);
        }
        for (const r of roadmap) {
          const tr = node("tr");
          tr.append(
            node("td", r.title),
            node("td", r.target),
            node("td", r.status),
          );
          const detail = node("td");
          detail.append(
            node("p", r.evidence),
            node("p", r.next_action),
            link("Supporting record", repo + r.path),
          );
          tr.append(detail);
          document.getElementById("roadmap-rows").append(tr);
        }
        document.getElementById("readiness-status").textContent =
          readiness.status;
        document.getElementById("practice-status").textContent =
          "Controls, resources, and roadmap loaded from the shared catalog.";
      }
      const selected = document.getElementById("dp-id");
      if (selected && selected.textContent)
        showTechnique(selected.textContent.split(" Ã‚Â· ")[0]);
    } catch {
      const status = document.getElementById("practice-status");
      if (status)
        status.textContent =
          "Data could not be loaded. Serve the docs folder or use the repository catalog.";
      for (const el of document.querySelectorAll("[data-domain-summary]"))
        el.replaceChildren(
          link(
            "Read the domain control catalog",
            repo + "resources/mitigation-catalog.md",
          ),
        );
    }
  }
  init();
})();
