# Manim Shape Transformations

This project utilizes Manim to create professional and clean animations that transform various shapes, including circles, triangles, squares, rectangles, ovals, pentagons, hexagons, and their 3D counterparts such as cubes, spheres, cones, cylinders, and pyramids.

## Project Structure

```
manim-shape-transformations
├── src
│   ├── main.py                # Entry point for the Manim animation
│   ├── scenes
│   │   ├── __init__.py        # Marks the scenes directory as a package
│   │   └── shape_transform_scene.py  # Contains the ShapeTransformScene class
│   └── utils
│       ├── __init__.py        # Marks the utils directory as a package
│       └── helpers.py         # Utility functions for animations
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/S-Leishem/geometric-shapes.git
   cd manim-shape-transformations
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the animation:**
   Execute the following command to run the main animation:
   ```bash
   manim -pql src/main.py
   ```

## Usage Examples

- The `ShapeTransformScene` class in `shape_transform_scene.py` defines various methods for transforming shapes. You can customize the transformations by modifying the parameters in these methods.

## Animations Included

- Circle to Triangle
- Triangle to Square
- Square to Rectangle
- Rectangle to Oval
- Oval to Pentagon
- Pentagon to Hexagon
- 3D transformations including:
  - Cube
  - Sphere
  - Cone
  - Cylinder
  - Pyramid

## Contributing

Feel free to submit issues or pull requests to enhance the project. Your contributions are welcome!
