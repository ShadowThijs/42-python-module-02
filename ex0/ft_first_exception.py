"""First Exception handling."""


def check_temperature(temp_str: str) -> None:
    """Gracefully check temperature."""
    print(f"\nTesting temperature: {temp_str}")
    lower_bound: int = 0
    upper_bound: int = 40
    try:
        int_str: int = int(temp_str)
        if (int_str > lower_bound and int_str < upper_bound):
            print(f"Temperature {int_str}°C is perfect for plants!")
        elif (int_str > upper_bound):
            print(f"Error: {int_str}°C is too hot for plants (max 40°C)")
        elif (int_str < 0):
            print(f"Error: {int_str}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


print("=== Garden Temperature Checker ===")
check_temperature("25")
check_temperature("abc")
check_temperature("100")
check_temperature("-50")
print("\nAll tests completed - program didn't crash!")
