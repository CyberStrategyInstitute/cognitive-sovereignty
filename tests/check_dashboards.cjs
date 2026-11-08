// Check browser script syntax and shared score wiring without external packages.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
for (const [name, variable, field] of [
  ['command-center/index.html', 'techniques', 'score'],
  ['docs/csf-command-center.html', 'CTSS', 's'],
  ['docs/csf-explorer.html', 'T', 's'],
  ['docs/index.html', null, null],
  ['docs/research.html', null, null],
  ['docs/guide.html', null, null],
  ['docs/practice.html', null, null],
  ['docs/page-map.html', null, null],
]) {
  const html = fs.readFileSync(path.join(root, name), 'utf8');
  const scripts = [...html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)];
  for (const [, attrs, code] of scripts) {
    const src = attrs.match(/src="([^"]+)"/);
    if (src && !src[1].startsWith('https:')) {
      assert.ok(fs.existsSync(path.resolve(root, path.dirname(name), src[1])), `${name}: missing script`);
      new vm.Script(fs.readFileSync(path.resolve(root, path.dirname(name), src[1]), 'utf8'), { filename: src[1] });
    }
    new vm.Script(code, { filename: name });
  }
  if (!variable) continue;
  const context = vm.createContext({ window: {} });
  vm.runInContext(fs.readFileSync(path.join(root, 'assets/csf-scores.js'), 'utf8'), context);
  const code = scripts.map(s => s[2]).join('\n');
  const start = code.indexOf(`const ${variable}`);
  const end = code.indexOf('\n', code.indexOf(`${variable}.sort(`, start));
  vm.runInContext(code.slice(start, end), context);
  const entries = vm.runInContext(variable, context);
  assert.equal(entries.length, 18);
  for (const entry of entries) {
    assert.equal(entry[field], context.window.CSF_SCORES[entry.id].score);
    assert.equal(entry.tier, context.window.CSF_SCORES[entry.id].tier);
  }
  assert.equal(entries[0].id, 'T-CT-010');
  if (name === 'docs/csf-explorer.html') {
    const fields = Object.fromEntries(['technique-search', 'technique-domain', 'technique-sort', 'technique-results', 'tgrid'].map(id => [id, { value: '', children: [], appendChild(child) { this.children.push(child); } }]));
    const grid = fields.tgrid;
    Object.defineProperty(grid, 'innerHTML', { set() { this.children = []; } });
    context.document = { getElementById: id => fields[id], createElement: () => ({ dataset: {}, addEventListener() {} }) };
    vm.runInContext(code.slice(code.indexOf("let currentTier='all';"), code.indexOf('function selT(')), context);
    fields['technique-sort'].value = 'score-asc';
    vm.runInContext("buildGrid('all')", context);
    assert.equal(grid.children.length, 18);
    const scores = grid.children.map(c => context.window.CSF_SCORES[c.dataset.id].score);
    assert.deepEqual(scores, [...scores].sort((a,b) => a-b));
    fields['technique-domain'].value = 'Purpose & Moral';
    vm.runInContext('buildGrid()', context);
    assert.ok(grid.children.length > 0);
    assert.ok(grid.children.every(c => context.window.CSF_SCORES[c.dataset.id].domains.includes('Purpose & Moral')));
    fields['technique-domain'].value = '';
    fields['technique-search'].value = 'T-CT-006';
    vm.runInContext("buildGrid('critical')", context);
    assert.deepEqual(grid.children.map(c => c.dataset.id), ['T-CT-006']);
    vm.runInContext("buildGrid('elevated')", context);
    assert.equal(grid.children.length, 0);
  }
}
console.log('PASS: eight pages and local scripts parse; shared scores, ranking, combined search/domain/tier filtering, and sorting pass. Rendered layout is not tested here.');
