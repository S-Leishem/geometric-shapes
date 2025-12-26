from manim import *

class ShapeTransformScene(Scene):
    def construct(self):
        self.transform_shapes()

    def transform_shapes(self):
        # Circle to Triangle
        circle = Circle()
        triangle = Triangle()
        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle, triangle))
        self.wait(1)

        # Triangle to Square
        square = Square()
        self.play(Transform(circle, square))
        self.wait(1)

        # Square to Rectangle
        rectangle = Rectangle(width=2, height=1)
        self.play(Transform(circle, rectangle))
        self.wait(1)

        # Rectangle to Oval
        oval = Ellipse(width=2, height=1)
        self.play(Transform(circle, oval))
        self.wait(1)

        # Oval to Pentagon
        pentagon = RegularPolygon(n=5)
        self.play(Transform(circle, pentagon))
        self.wait(1)

        # Pentagon to Hexagon
        hexagon = RegularPolygon(n=6)
        self.play(Transform(circle, hexagon))
        self.wait(1)

        # 3D Transformations
        self.play(FadeOut(circle))
        self.wait(1)

        # Cube
        cube = Cube()
        self.play(Create(cube))
        self.wait(1)

        # Sphere
        sphere = Sphere()
        self.play(Transform(cube, sphere))
        self.wait(1)

        # Cone
        cone = Cone()
        self.play(Transform(sphere, cone))
        self.wait(1)

        # Cylinder
        cylinder = Cylinder()
        self.play(Transform(cone, cylinder))
        self.wait(1)

        # Pyramid
        pyramid = Pyramid()
        self.play(Transform(cylinder, pyramid))
        self.wait(1)

        self.play(FadeOut(pyramid))
        self.wait(1)