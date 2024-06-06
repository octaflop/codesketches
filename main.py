from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

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


class SortTenThousandItems(Scene):
    def construct(self):
        self.camera.background_color = MODE["background_color"]

        # Title
        title = Text("Sorting 10,000 Items", color=MODE["text_color"]).scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create a list of 10,000 items
        num_items = 10000
        items = [Square(side_length=0.1).set_fill(MODE["dense_color"], opacity=0.5) for _ in range(num_items)]
        grid = VGroup(*items).arrange_in_grid(rows=100, cols=100, buff=0.05)
        self.play(FadeIn(grid))
        self.wait(1)

        # Sort the items (for simplicity, we just rearrange them)
        sorted_grid = VGroup(*sorted(items, key=lambda x: x.get_center()[0])).arrange_in_grid(rows=100, cols=100,
                                                                                              buff=0.05)
        self.play(Transform(grid, sorted_grid))
        self.wait(2)


class RandomSort(Scene):
    def construct(self):
        self.camera.background_color = MODE["background_color"]

        # Title
        title = Text("Random Sort of 10,000 Items", color=MODE["text_color"]).scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create a list of 10,000 items
        num_items = 10000
        items = [Square(side_length=0.1).set_fill(MODE["dense_color"], opacity=0.5) for _ in range(num_items)]

        # Place items randomly
        for item in items:
            item.move_to(np.array([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0]))

        grid = VGroup(*items)
        self.play(FadeIn(grid))
        self.wait(1)

        # Sort the items into a grid
        sorted_grid = VGroup(*items).arrange_in_grid(rows=100, cols=100, buff=0.05)
        self.play(Transform(grid, sorted_grid))
        self.wait(2)


# To run the animation, use the following command in your terminal:
# manim -p -qk main.py SparseVsDense SortTenThousandItems RandomSort


# Simply inherit from VoiceoverScene instead of Scene to get all the
# voiceover functionality.
class RecorderExample(VoiceoverScene):
    def construct(self):
        # You can choose from a multitude of TTS services,
        # or in this example, record your own voice:
        self.set_speech_service(RecorderService())

        circle = Circle()

        # Surround animation sections with with-statements:
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            # The duration of the animation is received from the audio file
            # and passed to the tracker automatically.

        # This part will not start playing until the previous voiceover is finished.
        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)
