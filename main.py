from manim import *
import random

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
MODE = DAYLIGHT_MODE


class SparseVsDense(Scene):
    def construct(self):
        self.camera.background_color = MODE["background_color"]

        # Title
        title = Text("Visualizing Dense and Sparse Arrays", color=MODE["text_color"])
        self.play(Write(title))
        self.wait()

        # Create a dense array
        dense_array = self.create_array(1000, dense=True)
        dense_label = Text("Dense Array", color=MODE["text_color"]).next_to(dense_array, UP)
        self.play(Create(dense_array), Write(dense_label))
        self.wait()
        self.play(FadeOut(dense_array), FadeOut(dense_label))

        # Create a sparse array
        sparse_array = self.create_array(1000, dense=False)
        sparse_label = Text("Sparse Array", color=MODE["text_color"]).next_to(sparse_array, UP)
        self.play(Create(sparse_array), Write(sparse_label))
        self.wait()

        # Explanation
        explanation = Text(
            "Dense arrays store all elements, including zeros.\n"
            "Sparse arrays store only non-zero elements.",
            t2c={"Dense arrays": MODE["dense_color"], "Sparse arrays": MODE["sparse_color"]},
            color=MODE["text_color"]
        ).scale(0.8).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

    def create_array(self, size, dense=True):
        array = VGroup()
        for i in range(size):
            value = random.randint(0, 10)
            if value == 0 and not dense:
                continue
            element = Square(side_length=0.2)
            if value == 0:
                element.set_fill(MODE["zero_color"], opacity=0.2)
            else:
                element.set_fill(MODE["dense_color"] if dense else MODE["sparse_color"], opacity=0.8)
            element.move_to(np.array([i % 20 - 10, 5 - i // 20, 0]))
            array.add(element)
        return array
