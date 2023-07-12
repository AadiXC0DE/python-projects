def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")

    choice = int(input("Enter your choice: "))
    temperature = float(input("Enter the temperature: "))

    if choice == 1:
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temperature}°F")
    elif choice == 2:
        converted_temperature = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equal to {converted_temperature}K")
    elif choice == 3:
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temperature}°C")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
