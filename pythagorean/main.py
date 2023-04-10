from copy import deepcopy
from manim import *

A = 1.5
B = 2.0
C = np.sqrt(A**2 + B**2)
TH = np.arctan(B / A)
FADE = 3
SHIFT = 3
MARGIN = (B - A) / 2

class PythagoreanTheorem(Scene):
    def create_shapes(self):
        self.a = VGroup(Square(A, color=RED, fill_opacity=1), MathTex("a^2", color=WHITE))
        self.b = VGroup(Square(B, color=BLUE, fill_opacity=1), MathTex("b^2", color=WHITE))
        self.c = VGroup(Square(C, color=GREEN, fill_opacity=1), MathTex("c^2", color=WHITE).rotate(-TH))

        self.a.move_to((A + B) / 2 * LEFT)
        self.b.move_to((A + B) / 2 * DOWN)
        self.c.move_to([np.cos(TH) * C / 2, np.sin(TH) * C / 2, 0])
        self.c.rotate(TH)

        self.t = Polygon(self.a.get_corner(UR), self.b.get_corner(UL), self.b.get_corner(UR), color=WHITE)

        self.play(AnimationGroup(
            FadeIn(self.a, run_time=FADE),
            FadeIn(self.b, run_time=FADE),
            FadeIn(self.c, run_time=FADE),
            FadeIn(self.t, run_time=FADE)
        ))

    def move_squares(self):
        self.play(self.a.animate.shift(SHIFT * LEFT))
        self.play(self.b.animate.shift(SHIFT * LEFT + (A + B) * UP))
        self.play(self.c.animate.shift(SHIFT * RIGHT))

    def move_triangles(self):
        l1 = deepcopy(self.t)
        r1 = deepcopy(self.t)
        self.play(AnimationGroup(
            ApplyMethod(l1.shift, SHIFT * LEFT),
            ApplyMethod(r1.shift, SHIFT * RIGHT)
        ))

        l2 = deepcopy(self.t)
        r2 = deepcopy(self.t)
        self.play(AnimationGroup(
            Rotate(l2, TAU / 4),
            Rotate(r2, TAU / 4)
        ))
        self.play(AnimationGroup(
            ApplyMethod(l2.shift, (SHIFT + B - MARGIN) * LEFT + (A + MARGIN) * UP),
            ApplyMethod(r2.shift, (SHIFT + B - MARGIN) * RIGHT + MARGIN * UP)
        ))

        l3 = deepcopy(self.t)
        r3 = deepcopy(self.t)
        self.play(AnimationGroup(
            Rotate(l3, -TAU / 4),
            Rotate(r3, -TAU / 4)
        ))
        self.play(AnimationGroup(
            ApplyMethod(l3.shift, (SHIFT + A + MARGIN) * LEFT + (A + MARGIN) * UP),
            ApplyMethod(r3.shift, (SHIFT - MARGIN) * RIGHT + (A + MARGIN) * UP)
        ))

        l4 = deepcopy(self.t)
        r4 = deepcopy(self.t)
        self.play(AnimationGroup(
            Rotate(l4, TAU / 2),
            Rotate(r4, TAU / 2)
        ))
        self.play(AnimationGroup(
            ApplyMethod(l4.shift, SHIFT * LEFT),
            ApplyMethod(r4.shift, (SHIFT + A) * RIGHT + B * UP)
        ))

    def construct(self):
        self.create_shapes()
        self.move_squares()
        self.move_triangles()
        self.wait(3)
