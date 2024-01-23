# Math Painting App

## Overview

This simple drawing app allows users to create and visualize rectangles and squares on a customizable canvas. Users can specify canvas dimensions, colors, and draw multiple shapes interactively. The application is triggered by the `main.py` file.

## Getting Started

To run the app, follow these steps:

1. Open a terminal window.
2. Install requirements
3. Navigate to the project directory.
4. Run the following command:

```bash
python main.py
```

4. Follow the prompts to input canvas dimensions, color, and draw rectangles or squares.

## Features

- Create rectangles with specified dimensions and color.
- Create squares with specified side length and color.
- Visualize shapes on a customizable canvas.

## Usage

1. **Canvas Setup:**
   - Enter the width and height of the canvas when prompted.
   - Choose the canvas color by entering 'black' or 'white'.

2. **Draw Shapes:**
   - Enter 'rectangle' to draw a rectangle.
     - Specify x, y, width, height, and color.
   - Enter 'square' to draw a square.
     - Specify x, y, side length, and color.

3. **Quit:**
   - Enter 'quit' to exit the drawing loop.

4. **Generate Canvas Image:**
   - A canvas image will be generated in the 'outputfiles' directory with a random number attached to its name.

## Example

```bash
Enter canvas width: 800
Enter canvas height: 600
Enter canvas color(black or white): white

What do you like to draw? Enter 'quit' to quit. rectangle
Enter x of the rectangle: 100
Enter y of the rectangle: 50
Enter width of the rectangle: 200
Enter height of the rectangle: 150
How much red should the rectangle have(0 to 255)? 255
How much green should the rectangle have(0 to 255)? 0
How much blue should the rectangle have(0 to 255)? 0

...

What do you like to draw? Enter 'quit' to quit. quit
```

## Output

The canvas image will be saved as `outputfiles/canvas_<random_number>.png`.