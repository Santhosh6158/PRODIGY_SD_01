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
def convert_temperature(value, unit):
    if unit == "C":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin
    elif unit == "F":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif unit == "K":
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit
    else:
        return None
def temperature_conversion():
    print(" Temperature Conversion Program")
    print("Convert between Celsius (C), Fahrenheit (F), and Kelvin (K).")

    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C, F, or K): ").strip().upper()

        result = convert_temperature(value, unit)

        if result:
            if unit == "C":
                print(f"{value}°C = {result[0]:.2f}°F, {result[1]:.2f}K")
            elif unit == "F":
                print(f"{value}°F = {result[0]:.2f}°C, {result[1]:.2f}K")
            elif unit == "K":
                print(f"{value}K = {result[0]:.2f}°C, {result[1]:.2f}°F")
        else:
            print(" Invalid unit. Please enter C, F, or K.")
    except ValueError:
        print(" Please enter a valid numeric temperature.")

temperature_conversion()
