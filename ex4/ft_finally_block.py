"""Finally block - always clean up.

Demonstrates try/except/finally for guaranteed resource cleanup.
"""


class GardenError(Exception):
    """Base error for garden problems."""

    def __init__(self, message: str = "Unknown garden error"):
        """Initialize GardenError."""
        super().__init__(message)


class PlantError(GardenError):
    """Error for problems with plants."""

    def __init__(self, message: str = "Unknown plant error"):
        """Initialize PlantError."""
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """Water a plant if its name is capitalized."""
    if (plant_name != plant_name.capitalize()):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    """Test the watering system with a list of plant names."""
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


print("=== Garden Watering System ===")
print("Testing valid plants...")
test_watering_system(["Tomato", "Lettuce", "Carrots"])
print("Testing invalid plants...")
test_watering_system(["Tomato", "lettuce"])
print("Cleanup always happens, even with errors!")
