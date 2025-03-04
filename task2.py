def calculate_sum(numbers):
    """Returns the sum of the given list of numbers."""
    return sum(numbers)

def calculate_average(numbers):
    """Returns the average of the given list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def find_maximum(numbers):
    """Returns the maximum number from the list."""
    return max(numbers)

def find_minimum(numbers):
    """Returns the minimum number from the list."""
    return min(numbers)

def main():
    """Main function to handle user input and perform selected mathematical operations."""
    operations = {
        "1": ("Sum", calculate_sum),
        "2": ("Average", calculate_average),
        "3": ("Maximum", find_maximum),
        "4": ("Minimum", find_minimum)
    }
    
    print("Mathematical Operations on a List of Numbers")
    print("Select an operation:")
    for key, (desc, _) in operations.items():
        print(f"{key}. {desc}")
    
    operation_choice = input("Enter your choice (1-4): ")
    if operation_choice not in operations:
        print("Invalid choice. Please restart and select a valid option.")
        return
    
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        if not numbers:
            raise ValueError("The list cannot be empty.")
        
        _, operation_function = operations[operation_choice]
        result = operation_function(numbers)
        print(f"Result: {result:.4f}")
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers separated by spaces.")

if __name__ == "__main__":
    main()