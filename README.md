PRODIGY_SD_01 – Temperature Conversion Program

Task Overview This project is part of my Prodigy Infotech Internship (Task 01).
The objective of this task is to build a Python program that converts temperatures between the three main temperature scales — Celsius, Fahrenheit, and Kelvin.
Project Description

The program prompts the user to enter:

    A temperature value
    The unit of the temperature (C, F, or K)

It then calculates and displays the equivalent temperatures in the other two units.
Key Features

    Converts between Celsius (°C), Fahrenheit (°F), and Kelvin (K)
    Accepts user input dynamically
    Handles invalid unit inputs with clear error messages
    Uses functions for modular, clean, and reusable code

Code Explanation

The core logic is implemented in a function called convert_temperature(value, unit) which:

    Checks the unit type (C, F, or K)
    Applies the correct conversion formulas:
        C → F = (C × 9/5) + 32
        C → K = C + 273.15
        F → C = (F − 32) × 5/9
        K → C = K − 273.15

The program then prints the results neatly.
Example Output

Temperature Conversion Program Convert between Celsius (C), Fahrenheit (F), and Kelvin (K).

Enter the temperature value: 25 Enter the unit (C, F, or K): C

25°C = 77.00°F, 298.15K
