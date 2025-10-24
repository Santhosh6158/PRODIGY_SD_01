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