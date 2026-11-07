"use strict";
const state = { events: [], signals: [] };
const $ = (id) => document.getElementById(id);
const el = (tag, text, className) => {
  const n = document.createElement(tag);
  if (text !== undefined) n.textContent = String(text);
  if (className) n.className = className;
  return n;
};
const repo =
  "https://github.com/CyberStrategyInstitute/cognitive-sovereignty/blob/main/";
function link(text, url) {
  const a = el("a", text);
  try {
    const u = new URL(url, location.href);
    if (!["https:", "http:"].includes(u.protocol)) return el("span", text);
    a.href = u.href;
    if (u.origin !== location.origin) a.rel = "noopener noreferrer";
  } catch {
    return el("span", text);
  }
  return a;
}
function options(id, items) {
  for (const value of [...new Set(items)].sort()) {
    $(id).append(new Option(value, value));
  }
}
function textMatch(row, value) {
  return JSON.stringify(row)
    .toLocaleLowerCase()
    .includes(value.trim().toLocaleLowerCase());
}
function showEvents() {
  const rows = state.events
    .filter(
      (e) =>
        textMatch(e, $("event-search").value) &&
        (!$("event-week").value || e.week_end === $("event-week").value) &&
        (!$("event-role").value || e.role === $("event-role").value) &&
        (!$("event-theme").value || e.theme === $("event-theme").value),
    )
    .sort((a, b) => b.ctss - a.ctss || a.id.localeCompare(b.id));
  $("event-rows").replaceChildren();
  for (const event of rows) {
    const tr = el("tr");
    const title = el("td");
    const button = el("button", event.title, "link-button");
    button.type = "button";
    button.addEventListener("click", () => {
      showScorecard(event);
      $("scorecard").scrollIntoView();
      $("scorecard").focus({ preventScroll: true });
    });
    title.append(button, el("div", event.id, "muted"));
    tr.append(title, el("td", event.week_end), el("td", event.role));
    const cell = el("td");
    cell.append(el("span", event.ctss + "/100", "tag " + event.priority));
    tr.append(cell);
    $("event-rows").append(tr);
  }
  $("event-results").textContent =
    rows.length + " of " + state.events.length + " assessments shown.";
}
function showScorecard(event) {
  const panel = $("scorecard-content");
  panel.replaceChildren();
  panel.append(
    el(
      "p",
      event.id + " · " + event.assessment_date + " · " + event.score_status,
      "eyebrow",
    ),
    el("h3", event.title),
    el("p", event.analysis),
  );
  const layout = el("div", undefined, "score-layout");
  const overall = el("div", undefined, "overall");
  overall.append(
    el("span", "CSI CTSS assessment"),
    el("strong", event.ctss, "number"),
    el("span", "/100 · " + event.priority),
    el("span", event.role + " evidence", "muted"),
  );
  const right = el("div");
  const factors = el("div", undefined, "factors");
  const labels = {
    L: ["Likelihood", 5],
    Ia: ["Impact on agency", 6],
    R: ["Population reach", 4],
    D: ["Detection difficulty", 3],
    RecD: ["Recovery difficulty", 2],
  };
  for (const [key, [label, points]] of Object.entries(labels)) {
    const box = el("div", undefined, "factor");
    box.append(
      el("span", label),
      el("strong", event.inputs[key] + "/5"),
      el("span", event.inputs[key] * points + " points", "points"),
    );
    factors.append(box);
  }
  right.append(factors, el("p", "Why it matters: " + event.us_relevance));
  const details = el("details");
  details.append(el("summary", "Inspect each input and its reason"));
  for (const [key, [label]] of Object.entries(labels)) {
    details.append(
      el("h4", label + " · " + event.inputs[key] + "/5"),
      el("p", event.input_reasons[key]),
    );
  }
  right.append(details);
  layout.append(overall, right);
  panel.append(
    layout,
    el("h4", "Action and expected outcome"),
    el("p", event.action),
    el("h4", "Research or escalation trigger"),
    el("p", event.research_trigger),
    el("h4", "Evidence and limits"),
    el("p", event.source_review),
  );
  const sources = el("ul");
  event.source_urls.forEach((url, i) => {
    const li = el("li");
    li.append(link("Source " + (i + 1), url));
    sources.append(li);
  });
  panel.append(sources);
  panel.append(
    link(
      "Read the full weekly assessment and preserved context",
      repo + "research/intake/reports/" + event.week_end + ".md",
    ),
  );
}
function showSignals() {
  const rows = state.signals.filter(
    (s) =>
      textMatch(s, $("signal-search").value) &&
      (!$("signal-status").value || s.status === $("signal-status").value) &&
      (!$("signal-kind").value || s.kind === $("signal-kind").value) &&
      (!$("signal-priority").value ||
        s.priority === $("signal-priority").value),
  );
  $("signal-rows").replaceChildren();
  for (const s of rows) {
    const tr = el("tr");
    const description = el("td", undefined, "signal-text");
    description.append(
      el("strong", s.id),
      el("p", s.source_text),
      el("small", s.source_id + " / paragraph " + s.source_paragraph),
    );
    const status = el("td");
    status.append(el("span", s.status, "tag"));
    const owner = el("td");
    owner.append(
      el("div", s.owner_role + " (role)"),
      el("small", "Proposed review: " + s.review_on),
      el("div", "Assignee: " + (s.assigned_to || "unassigned"), "muted"),
    );
    const next = el("td");
    next.append(el("p", s.disposition));
    const details = el("details");
    details.append(
      el("summary", "Trigger, evidence, and history"),
      el("p", s.review_trigger),
      el("p", s.validation_status),
    );
    s.evidence_paths.forEach((path) => {
      const p = el("p");
      p.append(link(path, repo + path));
      details.append(p);
    });
    for (const h of s.history)
      details.append(el("p", h.date + " · " + h.status + " · " + h.note));
    next.append(details);
    tr.append(description, status, owner, next);
    $("signal-rows").append(tr);
  }
  $("signal-results").textContent =
    rows.length + " of " + state.signals.length + " source signals shown.";
}
async function init() {
  try {
    const [events, signals, trends, slow] = await Promise.all(
      ["events", "signals", "weekly-trends", "slow-signals"].map(
        async (name) => {
          const response = await fetch("data/" + name + ".json");
          if (!response.ok) throw new Error("Data could not be loaded");
          return response.json();
        },
      ),
    );
    state.events = events;
    state.signals = signals;
    $("item-count").textContent = events.length;
    $("signal-count").textContent = signals.length;
    $("week-count").textContent = trends.length;
    options(
      "event-week",
      events.map((e) => e.week_end),
    );
    options(
      "event-role",
      events.map((e) => e.role),
    );
    options(
      "event-theme",
      events.map((e) => e.theme),
    );
    options(
      "signal-status",
      signals.map((s) => s.status),
    );
    options(
      "signal-kind",
      signals.map((s) => s.kind),
    );
    for (const id of [
      "event-search",
      "event-week",
      "event-role",
      "event-theme",
    ])
      $(id).addEventListener(
        id.endsWith("search") ? "input" : "change",
        showEvents,
      );
    for (const id of [
      "signal-search",
      "signal-status",
      "signal-kind",
      "signal-priority",
    ])
      $(id).addEventListener(
        id.endsWith("search") ? "input" : "change",
        showSignals,
      );
    for (const row of trends) {
      const tr = el("tr");
      for (const value of [
        row.week_end,
        row.items,
        row.mean_associated_risk,
        row.mean_threat_risk ?? "Not applicable",
        row.high_or_critical,
      ])
        tr.append(el("td", value));
      $("trend-rows").append(tr);
    }
    slow.forEach((s) =>
      $("slow-signals").append(
        el(
          "li",
          s.week_end +
            ": " +
            s.theme +
            " appeared in three consecutive available collections. Research the mechanism.",
        ),
      ),
    );
    showEvents();
    showSignals();
    if (events.length)
      showScorecard([...events].sort((a, b) => b.ctss - a.ctss)[0]);
    $("load-status").textContent =
      "Data loaded. Sources and provisional judgments are available for inspection.";
  } catch (error) {
    $("load-status").textContent =
      "The data could not be loaded. Serve the docs folder through a local web server or use the repository JSON files.";
  }
}
init();
