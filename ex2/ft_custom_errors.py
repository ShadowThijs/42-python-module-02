"""Raise Custom errors."""


class GardenError(Exception):
    """Custom exception for errors in the garden."""


class PlantError(GardenError):
    """Custom exception for errors with plants."""


class WaterError(GardenError):
    """Custom exception for errors with water."""


print("=== Custom Garden Errors Demo ===")
print("\nTesting PlantError...")
plant_error: str = "The tomato plant is wilting!"
water_error: str = "Not enough water in the tank!"
try:
    raise PlantError(plant_error)
except PlantError as e:
    print(f"Caught PlantError: {e}")
print("\nTesting WaterError...")
try:
    raise WaterError(water_error)
except WaterError as e:
    print(f"Caught WaterError: {e}")

print("\nTesting catching all garden errors...")
try:
    raise PlantError(plant_error)
except GardenError as e:
    print(f"Caught a garden error: {e}")

try:
    raise WaterError(water_error)
except GardenError as e:
    print(f"Caught a garden error: {e}")

print("\nAll custom error types work correctly!")
