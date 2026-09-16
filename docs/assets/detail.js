/* 共通スクリプト: フローのステップ送りアニメ / タブ / カウントアップ */
(function () {
  // --- animated flow: .anim-flow 内の .step を順に active にする ---
  document.querySelectorAll('.anim-flow[data-anim]').forEach(function (flow) {
    var steps = Array.prototype.slice.call(flow.querySelectorAll('.step'));
    var arrs = Array.prototype.slice.call(flow.querySelectorAll('.arr'));
    if (!steps.length) return;
    var i = 0, paused = false;
    function tick() {
      if (paused) return;
      steps.forEach(function (s, k) { s.classList.toggle('active', k === i); });
      arrs.forEach(function (a, k) { a.classList.toggle('active', k === i - 1); });
      i = (i + 1) % steps.length;
    }
    steps[0].classList.add('active');
    i = 1;
    var iv = setInterval(tick, 1600);
    flow.addEventListener('mouseenter', function () { paused = true; });
    flow.addEventListener('mouseleave', function () { paused = false; });
    // クリックでそのステップに固定/解除
    steps.forEach(function (s, k) {
      s.style.cursor = 'pointer';
      s.addEventListener('click', function () {
        paused = true;
        steps.forEach(function (x, j) { x.classList.toggle('active', j === k); });
        arrs.forEach(function (a, j) { a.classList.toggle('active', j === k - 1); });
      });
    });
  });

  // --- tabs: .tabs > .tab-btns button[data-tab] / .tab-panel[data-panel] ---
  document.querySelectorAll('.tabs').forEach(function (tabs) {
    var btns = tabs.querySelectorAll('.tab-btns button');
    var panels = tabs.querySelectorAll('.tab-panel');
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        btns.forEach(function (x) { x.classList.remove('on'); });
        panels.forEach(function (p) { p.classList.remove('on'); });
        b.classList.add('on');
        var target = tabs.querySelector('.tab-panel[data-panel="' + b.dataset.tab + '"]');
        if (target) target.classList.add('on');
      });
    });
  });

  // --- count-up: .cnt[data-to] 表示時に数値をカウントアップ ---
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting || e.target.dataset.done) return;
      e.target.dataset.done = '1';
      var to = parseFloat(e.target.dataset.to), suf = e.target.dataset.suf || '';
      var dec = (String(e.target.dataset.to).split('.')[1] || '').length;
      var t0 = performance.now();
      (function step(t) {
        var p = Math.min((t - t0) / 900, 1);
        var v = to * (1 - Math.pow(1 - p, 3));
        e.target.textContent = v.toFixed(dec) + suf;
        if (p < 1) requestAnimationFrame(step);
      })(t0);
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('.cnt[data-to]').forEach(function (el) { obs.observe(el); });

  // --- SVG cycle animation: .cycle-anim 内の .cycle-stage を順に .on ---
  document.querySelectorAll('.cycle-anim').forEach(function (root) {
    var stages = root.querySelectorAll('.cycle-stage');
    if (!stages.length) return;
    var i = 0;
    setInterval(function () {
      stages.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      i = (i + 1) % stages.length;
    }, 1500);
  });
})();
