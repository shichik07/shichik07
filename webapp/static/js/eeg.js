(function () {
  "use strict";

  var canvas = document.getElementById("eeg-canvas");
  if (!canvas || !canvas.getContext) return;

  var reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  var ctx = canvas.getContext("2d");
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var width, height;

  var CHANNELS = 4;
  var traces = [];

  function resize() {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    traces = [];
    for (var i = 0; i < CHANNELS; i++) {
      traces.push({
        baseline: ((i + 0.5) / CHANNELS) * height,
        seed: Math.random() * 1000,
        speed: 0.55 + Math.random() * 0.35,
        amp: 14 + Math.random() * 10,
        nextSpike: 60 + Math.random() * 240,
        spike: 0,
      });
    }
  }

  // Simulated EEG sample: layered sine "rhythms" + noise + occasional spikes,
  // loosely modeled on alpha/beta band mixing rather than any real signal.
  function sample(trace, t) {
    var x = t + trace.seed;
    var v =
      Math.sin(x * 0.9) * 0.5 +
      Math.sin(x * 2.3 + 1.3) * 0.28 +
      Math.sin(x * 5.1 + 0.4) * 0.14 +
      (Math.random() - 0.5) * 0.22;

    trace.nextSpike -= 1;
    if (trace.nextSpike <= 0 && trace.spike <= 0) {
      trace.spike = 10;
      trace.nextSpike = 200 + Math.random() * 400;
    }
    if (trace.spike > 0) {
      v += Math.sin((10 - trace.spike) * 0.9) * 1.6;
      trace.spike -= 1;
    }

    return v * trace.amp;
  }

  var POINTS = 260;
  var history = [];

  function draw(tick) {
    ctx.clearRect(0, 0, width, height);

    for (var c = 0; c < traces.length; c++) {
      var trace = traces[c];
      if (!history[c]) history[c] = [];
      var h = history[c];

      h.push(sample(trace, tick * trace.speed * 0.02));
      if (h.length > POINTS) h.shift();

      var step = width / (POINTS - 1);
      ctx.beginPath();
      for (var i = 0; i < h.length; i++) {
        var x = i * step;
        var y = trace.baseline - h[i];
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }

      var gradient = ctx.createLinearGradient(0, 0, width, 0);
      gradient.addColorStop(0, "rgba(90, 216, 255, 0)");
      gradient.addColorStop(0.15, "rgba(90, 216, 255, 0.55)");
      gradient.addColorStop(1, "rgba(90, 216, 255, 0.9)");

      ctx.strokeStyle = gradient;
      ctx.lineWidth = 1.4;
      ctx.shadowColor = "rgba(90, 216, 255, 0.6)";
      ctx.shadowBlur = 6;
      ctx.stroke();
    }
  }

  window.addEventListener("resize", resize);
  resize();

  if (reduceMotion) {
    draw(0);
    return;
  }

  var tick = 0;
  function loop() {
    tick += 1;
    draw(tick);
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
