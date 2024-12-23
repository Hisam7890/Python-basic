# Temperature Converter for Baking
def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: F = C * (9/5) + 32
    """
    return celsius * 9 / 5 + 32

def temperature_conversion_tool():
    print("👩‍🍳 Welcome to Sadia's Baking Temperature Converter! 🍰")
    print("Effortlessly convert baking temperatures from Celsius to Fahrenheit.\n")
    
    while True:
        try:
            # Get input from the user
            celsius_input = input("Enter the temperature in Celsius (or type 'exit' to quit): ").strip()
            if celsius_input.lower() == 'exit':
                print("\nHappy baking, Sadia! Goodbye! 👋")
                break
            
            # Convert input to float and calculate Fahrenheit
            celsius_temp = float(celsius_input)
            fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
            
            # Display the result
            print(f"🌡️ {celsius_temp:.2f}°C is equivalent to {fahrenheit_temp:.2f}°F\n")
        except ValueError:
            print("⚠️ Invalid input. Please enter a numerical value or 'exit' to quit.\n")

# Run the tool
if __name__ == "__main__":
    temperature_conversion_tool()
