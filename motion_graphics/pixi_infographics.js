/**
 * PixiJS WebGL Infographics & Kinetic Chart Engine.
 * High-performance 2D WebGL rendering for dynamic data visualizations.
 */

function generatePixiChartScript() {
  return `
  const app = new PIXI.Application({
    width: 1080,
    height: 1920,
    backgroundColor: 0x0E131F,
    resolution: 1
  });
  document.getElementById('stage-container').appendChild(app.view);

  // Animated Bars
  const bars = [];
  const barData = [
    { label: "Classical CPU", val: 120, color: 0x4A5568 },
    { label: "Supercomputer", val: 480, color: 0x3182CE },
    { label: "Quantum Core", val: 1400, color: 0xED8936 }
  ];

  barData.forEach((d, idx) => {
    const bar = new PIXI.Graphics();
    bar.y = 800 + idx * 160;
    bar.targetW = d.val;
    bar.color = d.color;
    app.stage.addChild(bar);
    bars.push(bar);
  });

  window.setSeekTime = function(t) {
    const progress = Math.min(1.0, t / 2.0);
    bars.forEach((bar) => {
      bar.clear();
      bar.beginFill(bar.color);
      bar.drawRoundedRect(180, 0, bar.targetW * progress, 80, 12);
      bar.endFill();
    });
  };
  `;
}

module.exports = { generatePixiChartScript };
