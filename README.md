# Shapes Drawing and Calculator

This is a Python script that allows users to calculate the area and perimeter of different geometric shapes and also draw them using the `turtle` graphics library.

## Features

- Calculates the area and perimeter for:
    - Circles
    - Isosceles Triangles
    - Squares
- Draws the shapes using Python's `turtle` module.
- Interactive command-line interface to get user input for shape properties.
- Supports both filled and unfilled shapes.

## Requirements

- Python 3.x

The script uses the `turtle`, `math`, `time`, and `abc` modules, which are all part of the standard Python library, so no external packages are required.

## How to Run

1.  Save the code as a Python file (e.g., `shapes_drawing.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script with the following command:

```bash
python shapes_drawing.py
```

## Usage

The program will first ask you to choose a shape.

```
tell me which shape's area and perimeter you want to know: triangle, circle or square
```

Based on your choice, it will ask for more details.

### Circle

Enter the properties in the format: `colour, is it filled?(true or false), radius`

**Example:** `red, true, 50`

### Triangle

The script currently draws isosceles triangles. Enter the properties in the format: `colour, is it filled?(true or false), height, base`

**Example:** `blue, false, 100, 120`

### Square

Enter the properties in the format: `colour, is it filled?(true or false), height`

**Example:** `green, true, 150`

After providing the details, the script will print the area and perimeter. It will then ask if you want to draw the shape. If you respond with `yes`, a turtle graphics window will open and draw the shape.

## Code Structure

The code is structured using object-oriented principles.

- **`Shape` (Abstract Base Class):** Defines the basic structure for any shape with `__init__` and `area` as abstract methods.
- **`Circle`, `Triangle`, `Square`:** These classes inherit from `Shape` and provide concrete implementations for calculating area, perimeter, and drawing the specific shape.
- **Main execution block:** Handles user input for selecting a shape and its properties, and then calls the appropriate class methods.