from manim import *

# Define color schemes
DAYLIGHT_MODE = {
    "background_color": "#fdf6e3",
    "text_color": "#657b83",
    "dense_color": "#268bd2",
    "sparse_color": "#2aa198",
    "zero_color": "#eee8d5"
}

DEFAULT_MODE = {
    "background_color": BLACK,
    "text_color": WHITE,
    "dense_color": BLUE,
    "sparse_color": GREEN,
    "zero_color": GRAY
}

# Choose the mode
MODE = DAYLIGHT_MODE  # Change to DEFAULT_MODE to switch back


class SparseVsDense(Scene):
    def construct(self):
        self.camera.background_color = MODE["background_color"]

        # Title
        title = Text("Sparse vs Dense Data Sets", color=MODE["text_color"]).scale(0.8)
        subtitle = Text("(Welcome to SLCPython, BTW)", color=MODE["text_color"]).scale(0.3).next_to(title, UP)
        self.play(Write(title))
        self.wait(0.8)
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title))
        self.play(FadeOut(subtitle))

        # Create a grid for dense data
        dense_matrix = self.create_matrix(5, 5, dense=True)
        dense_label = Text("Dense Matrix", color=MODE["text_color"]).scale(0.5).next_to(dense_matrix, UP)
        self.play(Create(dense_matrix), Write(dense_label))
        self.wait(1)
        self.play(FadeOut(dense_matrix), FadeOut(dense_label))

        # Create a grid for sparse data
        sparse_matrix = self.create_matrix(5, 5, dense=False)
        sparse_label = Text("Sparse Matrix", color=MODE["text_color"]).scale(0.5).next_to(sparse_matrix, UP)
        self.play(Create(sparse_matrix), Write(sparse_label))
        self.wait(1)
        self.play(FadeOut(sparse_matrix), FadeOut(sparse_label))

        # Position matrices side by side
        dense_matrix_group = VGroup(dense_matrix, dense_label).shift(LEFT * 3)
        sparse_matrix_group = VGroup(sparse_matrix, sparse_label).shift(RIGHT * 3)
        self.play(FadeIn(dense_matrix), FadeIn(dense_label))
        self.play(FadeIn(sparse_matrix), FadeIn(sparse_label))
        self.play(dense_matrix_group.animate.shift(LEFT * 2), sparse_matrix_group.animate.shift(RIGHT * 2))
        self.wait(1)

        # Explanation text
        explanation = Text(
            "Dense matrices store all elements, including zeros.\n"
            "Sparse matrices store only non-zero elements.",
            t2c={"Dense matrices": MODE["dense_color"], "Sparse matrices": MODE["sparse_color"]},
            color=MODE["text_color"]
        ).scale(0.5).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

    def create_matrix(self, rows, cols, dense=True):
        matrix = VGroup()
        for i in range(rows):
            for j in range(cols):
                if dense or (i + j) % 2 == 0:  # Sparse condition: only some elements are non-zero
                    element = Square(side_length=0.5).set_fill(MODE["dense_color"], opacity=0.5)
                else:
                    element = Square(side_length=0.5).set_fill(MODE["zero_color"], opacity=0.1)
                element.move_to(np.array([j - cols / 2, rows / 2 - i, 0]))
                matrix.add(element)
        return matrix

# To run the animation, use the following command in your terminal:
# manim -pql main.py SparseVsDense
