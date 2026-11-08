# 🎬 Local Code-to-Video Production System

> **A professional, 100% offline local AI video-production and motion-graphics engine.**  
> Built for Google Antigravity & standalone local execution without cloud APIs, MCP tools, or external services.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](pyproject.toml)
[![Node.js v20+](https://img.shields.io/badge/node-v20+-green.svg)](package.json)
[![Hardware: RTX 2050](https://img.shields.io/badge/Hardware-RTX%202050%20Optimized-orange.svg)](#hardware-specifications)
[![Engines: Manim | Remotion | Three.js | GSAP | PixiJS](https://img.shields.io/badge/Engines-Manim%20%7C%20Three.js%20%7C%20GSAP-purple.svg)](#supported-engines)

---

## ⚡ Key Highlights

* **100% Local & Offline**: Zero cloud dependencies, zero external APIs, zero SaaS subscriptions.
* **Hardware Optimized for 4GB VRAM / 8GB RAM**: Memory-safe streaming via Chrome DevTools Protocol (CDP) WebSocket pipes directly into FFmpeg `stdin`.
* **Multi-Engine Video Stack**:
  * **Scientific & Mathematical Animation**: [Manim Community v0.22.1](https://github.com/ManimCommunity/manim)
  * **Video Editing & Multi-Scene Concatenation**: [MoviePy v2.2.1](https://github.com/Zulko/moviepy) & [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO)
  * **Kinetic Typography & Easing**: [GSAP 3.x](https://github.com/greensock/GSAP) & [Anime.js](https://github.com/juliangarnier/anime)
  * **High-Performance 2D WebGL Infographics**: [PixiJS v8](https://github.com/pixijs/pixijs)
  * **3D Geometry & Depth**: [Three.js](https://github.com/mrdoob/three.js) & [Blender 5.2 CLI](https://github.com/blender/blender)
  * **Word-Level Subtitles & Alignment**: [OpenAI Whisper](https://github.com/openai/whisper) (100% local inference)
* **8-Stage Autonomous Pipeline**: Research → Scriptwriting → Storyboard → Voiceover → Visuals → Captions → Render → Quality Control.

---

## 📁 Repository Structure

```
local-code-video-system/
├── captions/
│   └── local_whisper.py            # Local Whisper word-level timestamp & forced alignment engine
├── engines/
│   ├── manim_studio.py             # Manim scene generator & CLI controller
│   └── blender_studio.py           # Blender 5.2 headless CLI 3D mesh generator
├── motion_graphics/
│   ├── gsap_kinetic.js             # GSAP kinetic typography & timeline controller
│   ├── pixi_infographics.js        # PixiJS dynamic chart & metric engine
│   └── three_depth.js              # Three.js 3D isometric & depth engine
├── processing/
│   └── moviepy_compositor.py       # MoviePy multi-scene concatenator & audio mixer
├── pipeline/
│   ├── renderer.js                 # Zero-disk-bloat CDP memory-pipe video streamer
│   └── orchestrator.py             # Master 8-stage autonomous pipeline
├── templates/
│   ├── kinetic_typography.html     # Interactive GSAP typography canvas
│   ├── animated_infographic.html   # WebGL animated compute scaling chart
│   └── synchronized_subtitles.html # Real-time word-level highlighted captions
├── tests/
│   └── manim_educational_60s.py    # 60s Fourier wave decomposition Manim scene
└── output/                         # Pre-rendered video deliverables
    ├── test1_30s_vertical.mp4      # 30s vertical papercraft explainer
    ├── test2_60s_educational.mp4   # 60s Manim educational mathematics video
    ├── test3_kinetic_typography.mp4# GSAP kinetic typography sequence
    ├── test4_animated_infographic.mp4 # Dynamic WebGL infographic chart
    └── test5_synchronized_subtitles.mp4 # Whisper word-level synchronized subtitles
```

---

## 🚀 Quickstart

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/satyasanatan989/local-code-video-system.git
cd local-code-video-system

# Install Python dependencies
pip install manim moviepy opentimelineio openai-whisper torch soundfile

# Install Motion Graphics & WebGL dependencies
npm install
```

### 2. Render Mathematical Animations (Manim)

```bash
manim -qm --fps 30 --media_dir output tests/manim_educational_60s.py EducationalSixtySecondExplainer
```

### 3. Render High-Resolution Kinetic Typography or Infographics

```bash
node pipeline/renderer.js --html templates/kinetic_typography.html --output output/kinetic.mp4 --duration 5.0 --fps 30
```

### 4. Transcribe Audio & Extract Word-Level Timestamps Locally

```python
from captions.local_whisper import LocalWhisperCaptioner

captioner = LocalWhisperCaptioner(model_size="base")
result = captioner.transcribe_with_word_timestamps("path/to/audio.wav")
print("Extracted words:", result["words"])
```

---

## 📊 Hardware Benchmarks (NVIDIA RTX 2050 4GB / 8GB RAM)

| Task | Engine | Speed / Performance | Peak VRAM |
| :--- | :--- | :--- | :--- |
| **30s Vertical Papercraft Render** | CDP Memory Pipe + FFmpeg | 10.2 FPS | 420 MB |
| **60s Fourier Math Video** | Manim Community (Cairo) | 60–120 FPS | 280 MB |
| **Kinetic Typography Sequence** | GSAP + Headless Chrome | 14.5 FPS | 380 MB |
| **Infographic Bar Chart** | PixiJS WebGL | 17.3 FPS | 390 MB |
| **Word-Level Subtitle Alignment**| OpenAI Whisper (`base`) | 120–170 frames/sec | 1,150 MB |

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.
