"""Custom garden error types.

Defines a hierarchy of garden-specific exceptions.
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


class WaterError(GardenError):
    """Error for problems with watering."""

    def __init__(self, message: str = "Unknown water error"):
        """Initialize WaterError."""
        super().__init__(message)


def test_plant_error() -> None:
    """Raise and catch a PlantError."""
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    """Raise and catch a WaterError."""
    raise WaterError("Not enough water in the tank!")


print("=== Custom Garden Errors Demo ===")
print("Testing PlantError...")
try:
    test_plant_error()
except PlantError as e:
    print(f"Caught PlantError: {e}")

print("Testing WaterError...")
try:
    test_water_error()
except WaterError as e:
    print(f"Caught WaterError: {e}")

print("Testing catching all garden errors...")
for fn in [test_plant_error, test_water_error]:
    try:
        fn()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

print("All custom error types work correctly!")
