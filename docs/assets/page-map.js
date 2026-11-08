"use strict";
(() => {
  let pages = [];
  const get = (id) => document.getElementById(id);
  const node = (tag, text) => {
    const el = document.createElement(tag);
    if (text !== undefined) el.textContent = text;
    return el;
  };
  function render() {
    const search = get("page-search").value.trim().toLocaleLowerCase();
    const rows = pages.filter(
      (p) =>
        (!get("page-module").value || p.module === get("page-module").value) &&
        (!get("page-change").value || p.change === get("page-change").value) &&
        JSON.stringify(p).toLocaleLowerCase().includes(search),
    );
    get("page-rows").replaceChildren();
    for (const page of rows) {
      const row = node("tr");
      const cell = node("td");
      const a = node("a", page.title);
      a.href =
        "https://github.com/CyberStrategyInstitute/cognitive-sovereignty/blob/main/" +
        page.path;
      cell.append(a, node("p", page.path));
      row.append(
        cell,
        node("td", page.module),
        node("td", page.change),
        node("td", page.status),
      );
      get("page-rows").append(row);
    }
    get("page-status").textContent =
      rows.length +
      " of " +
      pages.length +
      " documentation pages shown. Historical records retain their original bodies.";
  }
  async function init() {
    try {
      const response = await fetch("page-map.json");
      if (!response.ok) throw new Error("Page map unavailable");
      const data = await response.json();
      pages = data.pages;
      for (const [id, key] of [
        ["page-module", "module"],
        ["page-change", "change"],
      ])
        for (const value of [...new Set(pages.map((p) => p[key]))].sort())
          get(id).append(new Option(value, value));
      for (const id of ["page-search", "page-module", "page-change"])
        get(id).addEventListener(
          id === "page-search" ? "input" : "change",
          render,
        );
      render();
    } catch {
      get("page-status").textContent =
        "The page map could not load. Use PAGE_MAP.md in the repository or serve the docs folder through a local web server.";
    }
  }
  init();
})();
