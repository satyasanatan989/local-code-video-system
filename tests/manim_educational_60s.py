"""
60-Second Educational Video in Manim (16:9, 1280x720).
Pure Pango Text without requiring external LaTeX compiler.
"""

from manim import *

class EducationalSixtySecondExplainer(Scene):
    def construct(self):
        # 1. Title & Intro (0s - 10s)
        title = Text("Fourier Analysis & Harmonic Waves", font_size=42, color=GOLD)
        subtitle = Text("How complex sound waves break down into pure sine tones", font_size=24, color=LIGHT_GRAY).next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle), run_time=3)
        self.wait(4)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=2)

        # 2. Coordinate System & Fundamental Wave (10s - 25s)
        ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE_C}
        )
        x_lab = Text("Time (t)", font_size=20, color=BLUE_B).next_to(ax.x_axis, RIGHT)
        y_lab = Text("Amplitude", font_size=20, color=BLUE_B).next_to(ax.y_axis, UP)
        
        f1_label = Text("f1(t) = sin(t)", font_size=28, color=YELLOW).to_corner(UL)
        f1 = ax.plot(lambda x: np.sin(x), color=YELLOW)
        
        self.play(Create(ax), Write(x_lab), Write(y_lab), run_time=3)
        self.play(Create(f1), Write(f1_label), run_time=5)
        self.wait(5)

        # 3. Third Harmonic Overtones (25s - 45s)
        f3_label = Text("f3(t) = 1/3 sin(3t)", font_size=28, color=TEAL).next_to(f1_label, DOWN)
        f3 = ax.plot(lambda x: (1/3) * np.sin(3*x), color=TEAL)
        self.play(Create(f3), Write(f3_label), run_time=5)
        self.wait(5)

        # Composite Waveform
        comp_label = Text("S(t) = sin(t) + 1/3 sin(3t)", font_size=28, color=RED_B).to_corner(UR)
        comp = ax.plot(lambda x: np.sin(x) + (1/3) * np.sin(3*x), color=RED_B)
        self.play(FadeOut(f1), FadeOut(f3), Create(comp), Write(comp_label), run_time=6)
        self.wait(4)

        # 4. Conclusion & Energy Spectrum (45s - 60s)
        self.play(FadeOut(ax), FadeOut(x_lab), FadeOut(y_lab), FadeOut(comp), FadeOut(f1_label), FadeOut(f3_label), FadeOut(comp_label), run_time=2)
        final_box = RoundedRectangle(corner_radius=0.3, height=3.5, width=9.5, color=GOLD)
        final_title = Text("The Core Principle", font_size=36, color=GOLD).shift(UP * 0.8)
        final_text = Text("Any arbitrary periodic signal can be decomposed into an infinite sum of harmonics.", font_size=20, color=WHITE).next_to(final_title, DOWN)
        final_eq = Text("f(t) = a0/2 + Sum [ an*cos(nt) + bn*sin(nt) ]", font_size=26, color=YELLOW).next_to(final_text, DOWN)
        
        self.play(Create(final_box), Write(final_title), run_time=3)
        self.play(Write(final_text), Write(final_eq), run_time=6)
        self.wait(4)
