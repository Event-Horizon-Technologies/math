from manim import *


def gen_matrix_tex(matrix):
    return r"\begin{bmatrix} " + f"{matrix[0, 0]:.2f} & {matrix[0, 1]:.2f}" + \
           r" \\ " + f"{matrix[1, 0]:.2f} & {matrix[1, 1]:.2f}" + r" \end{bmatrix}"


def gen_vector_tex(vector):
    return r"\begin{bmatrix} " + f"{vector[0]:.2f}" + r" \\ " + f"{vector[1]:.2f}" + r" \end{bmatrix}"


class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self, leave_ghost_vectors=True)

    def construct(self):
        matrix = np.array([
            [2, 1],
            [1, 1]
        ])
        evals, evecs = np.linalg.eig(matrix)
        matrix_tex = MathTex(
            f"A = {gen_matrix_tex(matrix)}\n"
        ).to_edge(UL).add_background_rectangle()

        self.add_background_mobject(matrix_tex)
        self.apply_matrix(matrix, run_time=10)
        self.wait(10)
