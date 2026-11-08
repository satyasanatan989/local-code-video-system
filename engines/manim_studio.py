"""
Manim Studio Integration Engine.
Generates and executes mathematical, geometric, and scientific animations via Manim Community CLI.
"""

from pathlib import Path
from typing import Optional, Union
import subprocess
import sys

class ManimStudio:
    """Manages programmatic Manim scene generation and rendering."""

    def __init__(self, output_dir: Optional[Union[str, Path]] = None):
        self.output_dir = Path(output_dir or Path.cwd() / "output" / "manim")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_calculus_scene_script(self, script_path: Union[str, Path]) -> Path:
        """Writes a sample mathematical animation script demonstrating Riemann sums & Euler curves."""
        script_path = Path(script_path)
        script_path.parent.mkdir(parents=True, exist_ok=True)
        code = '''from manim import *

class CalculusExplainer(Scene):
    def construct(self):
        title = Text("The Beauty of Calculus", font_size=44, color=YELLOW)
        subtitle = Text("Area under the curve: ∫ f(x) dx", font_size=28, color=LIGHT_GRAY).next_to(title, DOWN)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 6, 1],
            x_length=7,
            y_length=4.5,
            axis_config={"color": BLUE},
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        
        curve = ax.plot(lambda x: 0.25 * x**2 + 0.5, color=GREEN)
        area = ax.get_area(curve, x_range=[0.5, 4.5], color=YELLOW, opacity=0.4)
        
        formula = MathTex(r"\\int_{0}^{4} \\left( \\frac{1}{4}x^2 + \\frac{1}{2} \\right) dx = \\frac{22}{3}").to_edge(UP)
        
        self.play(Create(ax), Write(labels))
        self.play(Create(curve), run_time=1.5)
        self.play(FadeIn(area), Write(formula))
        self.wait(1.5)
'''
        script_path.write_text(code, encoding="utf-8")
        return script_path

    def render_scene(
        self,
        script_path: Union[str, Path],
        scene_name: str,
        quality: str = "m",  # 'l' (480p), 'm' (720p), 'h' (1080p)
        fps: int = 30
    ) -> Path:
        """
        Executes Manim rendering via CLI.
        quality: 'l', 'm', 'h'
        """
        script_path = Path(script_path)
        cmd = [
            "manim",
            f"-q{quality}",
            f"--fps", str(fps),
            "--media_dir", str(self.output_dir),
            str(script_path),
            scene_name
        ]
        
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0:
            raise RuntimeError(f"Manim render error: {res.stderr}")

        # Find rendered MP4
        candidates = list(self.output_dir.glob(f"**/{scene_name}.mp4"))
        if not candidates:
            raise FileNotFoundError(f"Rendered Manim video not found for scene {scene_name}")
        return candidates[0]
