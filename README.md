🧮 Calculator Pro: A Tkinter GUI Calculator

This project is a simple yet functional calculator application built using the standard Python library Tkinter, providing a graphical user interface (GUI) for performing basic arithmetic operations.

Features ✨

    Graphical User Interface (GUI): A clean and user-friendly interface powered by Tkinter.

    Basic Operations: Supports addition (+), subtraction (-), multiplication (x), division (/), and percentage (%).

    Complex Inputs: Ability to handle complex expressions using parentheses ( and ).

    Clear Button (C): To wipe the entry and start a new calculation.

Prerequisites

You only need Python 3.x installed. The tkinter library is a standard library and is usually included with your Python installation.

How to Run 🚀

    Save the code in a file named (for example) calculator_pro.py.

    Run the file using the Python interpreter:
    Bash

    python calculator_pro.py

    The calculator window will appear, and you can begin entering your calculations.

Technical Structure

The calculator is built around a single class named Calculator:

    __init__(self, master): Initializes the main window (title, geometry, colors) and creates all the necessary buttons and the display entry field.

    show(self, value): Appends numbers and operators to the display string.

    clear(self): Resets the entry string and the display.

    solve(self): Calculates the result of the current expression on the screen using the built-in Python function eval().
