"""Agricultural data validation.

Basic exception handling for sensor temperature input.
"""


def input_temperature(temp_str: str) -> int:
    """Convert temperature string to integer."""
    return int(temp_str)


def test_temperature() -> None:
    """Test input_temperature with valid and invalid inputs."""
    print("=== Garden Temperature ===")
    for temp_str in ["25", "abc"]:
        print(f"Input data is '{temp_str}'")
        try:
            temp: int = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


test_temperature()
