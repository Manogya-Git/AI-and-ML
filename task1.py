def meters_to_feet(meters):
    """Converts meters to feet."""
    return meters * 3.28084

def feet_to_meters(feet):
    """Converts feet to meters."""
    return feet / 3.28084

def kg_to_lbs(kg):
    """Converts kilograms to pounds."""
    return kg * 2.20462

def lbs_to_kg(lbs):
    """Converts pounds to kilograms."""
    return lbs / 2.20462

def liters_to_gallons(liters):
    """Converts liters to gallons."""
    return liters * 0.264172

def gallons_to_liters(gallons):
    """Converts gallons to liters."""
    return gallons / 0.264172

def main():
    """Main function to handle user input and perform conversions."""
    conversions = {
        "1": ("Length", {"1": ("Meters to Feet", meters_to_feet), "2": ("Feet to Meters", feet_to_meters)}),
        "2": ("Weight", {"1": ("Kilograms to Pounds", kg_to_lbs), "2": ("Pounds to Kilograms", lbs_to_kg)}),
        "3": ("Volume", {"1": ("Liters to Gallons", liters_to_gallons), "2": ("Gallons to Liters", gallons_to_liters)})
    }
    
    print("Unit Conversion Program")
    print("Select a conversion type:")
    for key, (category, _) in conversions.items():
        print(f"{key}. {category}")
    
    conversion_type = input("Enter your choice (1-3): ")
    if conversion_type not in conversions:
        print("Invalid choice. Please restart and select a valid option.")
        return
    
    category, options = conversions[conversion_type]
    print(f"{category} Conversions:")
    for key, (desc, _) in options.items():
        print(f"{key}. {desc}")
    
    conversion_option = input("Enter your choice: ")
    if conversion_option not in options:
        print("Invalid choice. Please restart and select a valid option.")
        return
    
    _, conversion_function = options[conversion_option]
    
    try:
        value = float(input("Enter the value to convert: "))
        result = conversion_function(value)
        print(f"Converted value: {result:.4f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
