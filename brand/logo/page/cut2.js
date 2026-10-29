(() => {
  // How far each spot of the plate is from the logo's ink, one byte per spot, two steps to a pixel.
  const COLS = /*COLS*/, ROWS = /*ROWS*/;
  const far = Uint8Array.from(atob("/*FIELD*/"), (c) => c.charCodeAt(0));
  const css = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  const PLATE = css("--plate"), SAND = css("--sand");
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const cv = document.getElementById("plate"), ctx = cv.getContext("2d");
  const slider = document.getElementById("clarity"), trace = document.getElementById("trace");
  const N = 12000, px = new Float32Array(N), py = new Float32Array(N);
  let clarity = 1;

  function away(x, y) {
    const i = Math.min(COLS - 2, Math.max(0, x | 0)), j = Math.min(ROWS - 2, Math.max(0, y | 0));
    const u = x - i, v = y - j, o = j * COLS + i;
    return ((far[o] * (1 - u) + far[o + 1] * u) * (1 - v) + (far[o + COLS] * (1 - u) + far[o + COLS + 1] * u) * v) / 2;
  }
  function scatter() { for (let i = 0; i < N; i++) { px[i] = Math.random() * (COLS - 1); py[i] = Math.random() * (ROWS - 1) } }

  // Sand hops at random. A hop toward the line always sticks; a hop away from it rarely does.
  // So loose grains drift in and pile up on the line. With clarity at 0 every hop sticks and nothing gathers.
  const HOP = 1.8, HEAT = 0.45;
  const fold = (v, top) => (v < 0 ? -v : v > top ? 2 * top - v : v);
  function step(times) {
    for (let k = 0; k < times; k++) for (let i = 0; i < N; i++) {
      const x = fold(px[i] + (Math.random() - 0.5) * 2 * HOP, COLS - 1), y = fold(py[i] + (Math.random() - 0.5) * 2 * HOP, ROWS - 1);
      const rise = (away(x, y) - away(px[i], py[i])) * clarity;
      if (rise <= 0 || Math.random() < Math.exp(-rise / HEAT)) { px[i] = x; py[i] = y }
    }
  }
  function draw() {
    const k = cv.width / COLS;
    ctx.fillStyle = PLATE; ctx.fillRect(0, 0, cv.width, cv.height);
    ctx.fillStyle = SAND;
    for (let i = 0; i < N; i++) ctx.fillRect(px[i] * k - 1.2, py[i] * k - 1.2, 2.4, 2.4);
  }
  function readout() {
    let on = 0;
    for (let i = 0; i < N; i++) if (away(px[i], py[i]) < 0.6) on++;
    const share = Math.round(100 * on / N), state = document.getElementById("r-state");
    document.getElementById("r-on").textContent = share + "%";
    state.textContent = share > 70 ? "Clear" : share > 35 ? "Clearing" : "Loose";
    state.classList.toggle("tune", share > 70);
  }

  let seen = true, raf = 0, tick = 0;
  function loop() { raf = 0; if (!seen) return; step(1); draw(); if (++tick % 12 === 0) readout(); raf = requestAnimationFrame(loop) }
  function wake() { if (still) { step(160); draw(); readout() } else if (!raf) raf = requestAnimationFrame(loop) }
  slider.addEventListener("input", () => { clarity = +slider.value; wake() });
  document.getElementById("scatter").addEventListener("click", () => { scatter(); draw(); readout(); wake() });
  document.getElementById("overlay").addEventListener("change", (e) => { trace.hidden = !e.target.checked });
  new IntersectionObserver((e) => { seen = e[0].isIntersecting; if (seen) wake() }).observe(cv);
  scatter(); step(160); draw(); readout();
})();
