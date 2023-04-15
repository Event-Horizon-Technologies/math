from copy import deepcopy
from manim import *

A = 1.5
B = 2.0
C = np.sqrt(A**2 + B**2)
A_COLOR = RED
B_COLOR = BLUE
C_COLOR = GREEN
TH = np.arctan(B / A)
RUN_TIME = 3
SHIFT = 3
STROKE_WIDTH = 3
BORDER = STROKE_WIDTH / 200
MARGIN = (B - A) / 2

class PythagoreanTheorem(Scene):
    @staticmethod
    def create_triangle(a, b, c):
        return VGroup(
            Line(a, b, stroke_width=STROKE_WIDTH, color=A_COLOR),
            Line(b, c, stroke_width=STROKE_WIDTH, color=B_COLOR),
            Line(c, a, stroke_width=STROKE_WIDTH, color=C_COLOR)
        )

    @staticmethod
    def create_square(side_length, color):
        return VGroup(
            Line(side_length * UL / 2, side_length * UR / 2, stroke_width=STROKE_WIDTH, color=color),
            Line(side_length * UR / 2, side_length * DR / 2,  stroke_width=STROKE_WIDTH, color=color),
            Line(side_length * DR / 2, side_length * DL / 2, stroke_width=STROKE_WIDTH, color=color),
            Line(side_length * DL / 2, side_length * UL / 2, stroke_width=STROKE_WIDTH, color=color),
            Square(side_length, stroke_width=0, color=color, fill_opacity=0.5)
        )

    def create_shapes(self):
        self.a = VGroup(self.create_square(A, A_COLOR), MathTex("a^2", color=WHITE))
        self.b = VGroup(self.create_square(B, B_COLOR), MathTex("b^2", color=WHITE))
        self.c = VGroup(self.create_square(C, C_COLOR).rotate(TH), MathTex("c^2", color=WHITE))

        self.a.move_to((A + B) / 2 * LEFT)
        self.b.move_to((A + B) / 2 * DOWN)
        self.c.move_to([np.cos(TH) * C / 2, np.sin(TH) * C / 2, 0])

        self.t = self.create_triangle(self.a.get_corner(UR), self.a.get_corner(DR), self.b.get_corner(UR))

        self.play(AnimationGroup(
            FadeIn(self.a, run_time=RUN_TIME),
            FadeIn(self.b, run_time=RUN_TIME),
            FadeIn(self.c, run_time=RUN_TIME),
            FadeIn(self.t, run_time=RUN_TIME)
        ))

    def move_squares(self):
        self.play(self.a.animate.shift(SHIFT * LEFT))
        self.play(self.b.animate.shift(SHIFT * LEFT + (A + B) * UP))
        self.play(self.c.animate.shift(SHIFT * RIGHT))

    def move_triangles(self):
        self.l1 = deepcopy(self.t)
        self.r1 = deepcopy(self.t)
        self.play(AnimationGroup(
            ApplyMethod(self.l1.shift, SHIFT * LEFT),
            ApplyMethod(self.r1.shift, SHIFT * RIGHT)
        ))

        self.l2 = deepcopy(self.t)
        self.r2 = deepcopy(self.t)
        self.play(AnimationGroup(
            Rotate(self.l2, TAU / 4, about_point=ORIGIN),
            Rotate(self.r2, TAU / 4, about_point=ORIGIN)
        ))
        self.play(AnimationGroup(
            ApplyMethod(self.l2.shift, (SHIFT + B - MARGIN) * LEFT + (A + MARGIN) * UP),
            ApplyMethod(self.r2.shift, (SHIFT + B - MARGIN) * RIGHT + MARGIN * UP)
        ))

        self.l3 = deepcopy(self.t)
        self.r3 = deepcopy(self.t)
        self.play(AnimationGroup(
            Rotate(self.l3, -TAU / 4, about_point=ORIGIN),
            Rotate(self.r3, -TAU / 4, about_point=ORIGIN)
        ))
        self.play(AnimationGroup(
            ApplyMethod(self.l3.shift, (SHIFT + A + MARGIN) * LEFT + (A + MARGIN) * UP),
            ApplyMethod(self.r3.shift, (SHIFT - MARGIN) * RIGHT + (A + MARGIN) * UP)
        ))

        self.l4 = deepcopy(self.t)
        self.r4 = deepcopy(self.t)
        self.remove(self.t)
        self.play(AnimationGroup(
            Rotate(self.l4, TAU / 2, about_point=ORIGIN),
            Rotate(self.r4, TAU / 2, about_point=ORIGIN)
        ))
        self.play(AnimationGroup(
            ApplyMethod(self.l4.shift, SHIFT * LEFT),
            ApplyMethod(self.r4.shift, (SHIFT + A) * RIGHT + B * UP)
        ))

    def change_a_and_b(self, d):
        global A, B, C, TH
        _a = deepcopy(self.a).scale(1 + d / A, about_point=self.a.get_corner(DL))
        _b = deepcopy(self.b).scale(1 - d / B, about_point=self.b.get_corner(UR))
        _th = np.arctan((B - d) / (A + d))
        _c = deepcopy(self.c).rotate(_th - TH).scale(np.sqrt((A + d) ** 2 + (B - d) ** 2) / C)
        self.play(AnimationGroup(
            Transform(self.a, _a),
            Transform(self.b, _b),
            Transform(self.c, _c),

            Transform(self.l1, self.create_triangle(
                self.l1.get_corner(UL) + d * UR, self.l1.get_corner(DL) + d * RIGHT, self.l1.get_corner(DR))),
            Transform(self.l2, self.create_triangle(
                self.l2.get_corner(DL) + d * UP, self.l2.get_corner(DR) + d * UR, self.l2.get_corner(UR) + d * RIGHT)),
            Transform(self.l3, self.create_triangle(
                self.l3.get_corner(UR) + d * RIGHT, self.l3.get_corner(UL), self.l3.get_corner(DL) + d * UP)),
            Transform(self.l4, self.create_triangle(
                self.l4.get_corner(DR), self.l4.get_corner(UR) + d * UP, self.l4.get_corner(UL) + d * UR)),

            Transform(self.r1, self.create_triangle(
                self.r1.get_corner(UL) + d * UP, self.r1.get_corner(DL), self.r1.get_corner(DR) + d * LEFT)),
            Transform(self.r2, self.create_triangle(
                self.r2.get_corner(DL) + d * LEFT, self.r2.get_corner(DR), self.r2.get_corner(UR) + d * DOWN)),
            Transform(self.r3, self.create_triangle(
                self.r3.get_corner(UR) + d * RIGHT, self.r3.get_corner(UL), self.r3.get_corner(DL) + d * UP)),
            Transform(self.r4, self.create_triangle(
                self.r4.get_corner(DR) + d * DOWN, self.r4.get_corner(UR), self.r4.get_corner(UL) + d * RIGHT)),
        ), run_time=RUN_TIME)

        A, B, C, TH = A + d, B - d, np.sqrt((A + d) ** 2 + (B - d) ** 2), _th

    def construct(self):
        self.create_shapes()
        self.move_squares()
        self.move_triangles()
        _A, _B = A, B
        self.change_a_and_b(B / 2)
        self.change_a_and_b(-A / 2)
        self.change_a_and_b(_A - A)
        self.wait(3)
