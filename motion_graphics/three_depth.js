/**
 * Three.js 3D Graphics & Depth Engine for Local Video Production.
 * Renders hardware-accelerated WebGL meshes, isometric grids, and particle fields.
 */

function generateThreeJsSceneScript() {
  return `
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, 1080 / 1920, 0.1, 1000);
  camera.position.set(0, 0, 8);

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(1080, 1920);
  renderer.setPixelRatio(1);
  document.getElementById('stage-container').appendChild(renderer.domElement);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
  scene.add(ambientLight);

  const dirLight = new THREE.DirectionalLight(0xd4af37, 2.5);
  dirLight.position.set(5, 5, 7);
  scene.add(dirLight);

  // 3D Icosahedron Geometric Core
  const geometry = new THREE.IcosahedronGeometry(2.2, 0);
  const material = new THREE.MeshStandardMaterial({
    color: 0x9B111E,
    metalness: 0.85,
    roughness: 0.2,
    wireframe: false
  });
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  // Wireframe outer cage
  const wireGeo = new THREE.IcosahedronGeometry(2.6, 1);
  const wireMat = new THREE.MeshBasicMaterial({ color: 0xD4AF37, wireframe: true });
  const wireMesh = new THREE.Mesh(wireGeo, wireMat);
  scene.add(wireMesh);

  window.setSeekTime = function(t) {
    mesh.rotation.x = t * 1.2;
    mesh.rotation.y = t * 1.8;
    wireMesh.rotation.x = -t * 0.8;
    wireMesh.rotation.y = -t * 1.1;
    renderer.render(scene, camera);
  };
  `;
}

module.exports = { generateThreeJsSceneScript };
