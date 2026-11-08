/**
 * GSAP Kinetic Typography & Timeline Controller.
 * Produces word-level reveals, elastic bounces, and high-impact typographic transitions.
 */

function generateKineticTypographyScene(headline, subheadline, punchline) {
  return `
  <div class="kinetic-container" id="kinetic-stage">
    <div class="kinetic-sub" id="k-sub">${subheadline}</div>
    <div class="kinetic-head" id="k-head">${headline}</div>
    <div class="kinetic-punch" id="k-punch">${punchline}</div>
  </div>
  `;
}

function generateGSAPTimelineScript() {
  return `
  // GSAP 3.x Timeline
  const tl = gsap.timeline({ paused: true });

  tl.from("#k-sub", {
    y: -40,
    opacity: 0,
    duration: 0.6,
    ease: "power3.out"
  })
  .from("#k-head", {
    scale: 0.7,
    opacity: 0,
    duration: 0.8,
    ease: "back.out(1.7)"
  }, "-=0.2")
  .from("#k-punch", {
    y: 50,
    opacity: 0,
    duration: 0.7,
    ease: "elastic.out(1, 0.5)"
  }, "-=0.3");

  window.setSeekTime = function(t) {
    tl.seek(t);
  };
  `;
}

module.exports = {
  generateKineticTypographyScene,
  generateGSAPTimelineScript
};
