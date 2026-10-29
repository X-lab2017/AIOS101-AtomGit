'use strict';
(() => {
  const root = document.documentElement;
  const read = (key, fallback) => { try { return localStorage.getItem('aios-atomgit.' + key) || fallback; } catch { return fallback; } };
  const save = (key, value) => { try { localStorage.setItem('aios-atomgit.' + key, value); } catch { /* Preferences are optional. */ } };
  let lang = read('language', 'zh');
  let theme = read('theme', window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  let font = Number(read('font', '17'));
  if (!Number.isFinite(font) || font < 15 || font > 22) font = 17;
  const setTheme = () => {
    if (!['light', 'dark'].includes(theme)) theme = 'light';
    root.dataset.aiosTheme = theme;
    document.querySelectorAll('[data-logo]').forEach(img => { img.src = img.src.replace(/-(light|dark)\.svg/, '-' + theme + '.svg'); });
    document.querySelector('meta[name="theme-color"]').content = theme === 'dark' ? '#171B27' : '#F6F3EB';
    document.querySelector('#theme-toggle').setAttribute('aria-label', lang === 'en' ? 'Switch to ' + (theme === 'dark' ? 'light' : 'dark') + ' theme' : '切换' + (theme === 'dark' ? '浅色' : '深色') + '主题');
  };
  const setLang = () => {
    if (!['zh','en'].includes(lang)) lang = 'zh';
    document.querySelectorAll('[data-zh][data-en]').forEach(el => { el.textContent = el.dataset[lang]; if(lang === 'en') el.lang = 'en'; else el.removeAttribute('lang'); });
    const toggle = document.querySelector('#language-toggle');
    toggle.textContent = lang === 'zh' ? 'EN' : '中文';
    toggle.setAttribute('aria-label', lang === 'zh' ? 'Switch interface to English' : '切换中文界面');
    document.querySelector('.translation-note').hidden = lang !== 'en';
    setTheme();
  };
  const setFont = () => {
    root.style.setProperty('--reading-size', font + 'px');
    document.querySelectorAll('[data-font]').forEach(b => { b.disabled = Number(b.dataset.font) < 0 ? font <= 15 : font >= 22; });
  };
  document.querySelector('#theme-toggle').addEventListener('click', () => { theme = theme === 'light' ? 'dark' : 'light'; setTheme(); save('theme', theme); });
  document.querySelector('#language-toggle').addEventListener('click', () => { lang = lang === 'zh' ? 'en' : 'zh'; setLang(); save('language', lang); });
  document.querySelectorAll('[data-font]').forEach(button => button.addEventListener('click', () => { font = Math.max(15,Math.min(22,font + Number(button.dataset.font))); setFont(); save('font',String(font)); }));
  const menu = document.querySelector('#main-nav');
  const menuButton = document.querySelector('#menu-toggle');
  const closeMenu = () => { menu.classList.remove('open'); menuButton.setAttribute('aria-expanded','false'); menuButton.setAttribute('aria-label','展开导航'); };
  menuButton.addEventListener('click', () => { const open = menu.classList.toggle('open'); menuButton.setAttribute('aria-expanded',String(open)); menuButton.setAttribute('aria-label',open ? '收起导航' : '展开导航'); });
  document.addEventListener('keydown', e => { if(e.key === 'Escape' && menu.classList.contains('open')) { closeMenu(); menuButton.focus(); } });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click',closeMenu));
  const chapterMenu = document.querySelector('.chapter-menu');
  if (chapterMenu && window.matchMedia('(min-width: 851px)').matches) chapterMenu.open = true;
  const search = document.querySelector('#chapter-search');
  if (search) search.addEventListener('input', () => {
    const query = search.value.trim().toLocaleLowerCase(); let count = 0;
    document.querySelectorAll('.chapter-row').forEach(row => { row.hidden = !row.dataset.search.toLocaleLowerCase().includes(query); if(!row.hidden) count++; });
    document.querySelectorAll('.chapter-group').forEach(group => { group.hidden = !Array.from(group.querySelectorAll('.chapter-row')).some(r => !r.hidden); });
    document.querySelector('#search-empty').hidden = count !== 0;
    document.querySelector('#search-status').textContent = '找到 ' + count + ' 个章节';
  });
  setLang(); setFont();
})();
