from manim import *
try:
    #
    from manim.mobject.three_dimensions.solids import Pyramid
except Exception:
    Pyramid = None

class ShapeTransformScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=-35*DEGREES, distance=8)
        self.transform_shapes()

    def transform_shapes(self):
        
        circle = Circle()
        triangle = Triangle()
        square = Square()
        rectangle = Rectangle(width=3, height=1.5)
        oval = Ellipse(width=3, height=1.5)
        pentagon = RegularPolygon(n=5)
        hexagon = RegularPolygon(n=6)

        self.play(Create(circle))
        self.play(Transform(circle, triangle))
        self.play(Transform(circle, square))
        self.play(Transform(circle, rectangle))
        self.play(Transform(circle, oval))
        self.play(Transform(circle, pentagon))
        self.play(Transform(circle, hexagon))
        self.play(FadeOut(circle))

    
        self.begin_ambient_camera_rotation(rate=0.15)

        sphere = Sphere(radius=1)
        self.play(FadeIn(sphere, shift=OUT))

        cube = Cube(side_length=2)
        self.play(Transform(sphere, cube))

        cone = Cone(base_radius=1, height=2)
        self.play(Transform(sphere, cone))

        cylinder = Cylinder(radius=1, height=2)
        self.play(Transform(sphere, cylinder))

        pyr = Pyramid() if Pyramid else Cone(base_radius=1, height=2)  
        self.play(Transform(sphere, pyr))
        self.wait(0.5)

        self.play(FadeOut(sphere))
        self.stop_ambient_camera_rotation()