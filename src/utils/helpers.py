def create_circle(radius):
    from manim import Circle
    return Circle(radius=radius)

def create_square(side_length):
    from manim import Square
    return Square(side_length=side_length)

def create_rectangle(width, height):
    from manim import Rectangle
    return Rectangle(width=width, height=height)

def create_oval(width, height):
    from manim import Ellipse
    return Ellipse(width=width, height=height)

def create_pentagon(side_length):
    from manim import RegularPolygon
    return RegularPolygon(n=5, radius=side_length)

def create_hexagon(side_length):
    from manim import RegularPolygon
    return RegularPolygon(n=6, radius=side_length)

def create_cube(side_length):
    from manim import Cube
    return Cube(side_length=side_length)

def create_sphere(radius):
    from manim import Sphere
    return Sphere(radius=radius)

def create_cone(radius, height):
    from manim import Cone
    return Cone(radius=radius, height=height)

def create_cylinder(radius, height):
    from manim import Cylinder
    return Cylinder(radius=radius, height=height)

def create_pyramid(base_length, height):
    from manim import Pyramid
    return Pyramid(base_length=base_length, height=height)

def animate_shape_transformation(scene, shape_from, shape_to, duration=2):
    from manim import Transform
    scene.play(Transform(shape_from, shape_to), run_time=duration)