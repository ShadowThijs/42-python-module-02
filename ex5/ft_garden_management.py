"""Garden Management System."""


class GardenError(Exception):
    """Custom exception for errors in the garden."""


class PlantError(GardenError):
    """Custom exception for errors with plants."""


class WaterError(GardenError):
    """Custom exception for errors with water."""


class Plant:
    """Plant class."""

    def __init__(self, name: str, water: int, sun: int):
        """Create a plant class."""
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    """Garden manager class."""

    @staticmethod
    def add_plant(plant: Plant) -> None:
        """Add a plant to the garden."""
        try:
            if not plant.name:
                raise PlantError("Plant name cannot be empty!")
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    @staticmethod
    def water_plants(plants: list[Plant]) -> None:
        """Water all plants in the garden."""
        print("Opening watering system")
        try:
            for plant in plants:
                if plant.name:
                    print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_health(plant: Plant) -> None:
        """Check the health of a plant."""
        try:
            water_error: str = f"Water level {plant.water} "
            sunlight_error: str = f"Sunlight hours {plant.sun} "
            water_low: str = "is too low (min 1)"
            water_high: str = "is too high (max 10)"
            sun_low: str = "is too low (min 2)"
            sun_high: str = "is too high (max 12)"

            if plant.water <= 1:
                raise WaterError(water_error + water_low)
            elif plant.water >= 10:
                raise WaterError(water_error + water_high)
            if plant.sun <= 2:
                raise PlantError(sunlight_error + sun_low)
            elif plant.sun >= 12:
                raise PlantError(sunlight_error + sun_high)
            part2 = f"water: {plant.water}, sun: {plant.sun}"
            print(f"{plant.name}: healthy ({part2})")
        except GardenError as e:
            print(f"Error checking {plant.name}: {e}")

    @staticmethod
    def test_error_recovery() -> None:
        """Test error recovery in the system."""
        try:
            raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")


print("=== Garden Management System ===")

tomato: Plant = Plant("tomato", 5, 8)
lettuce: Plant = Plant("lettuce", 15, 9)
empty: Plant = Plant("", 4, 4)

print("\nAdding plants to garden...")
GardenManager.add_plant(tomato)
GardenManager.add_plant(lettuce)
GardenManager.add_plant(empty)

print("\nWatering plants...")
plants: list[Plant] = [tomato, lettuce]
GardenManager.water_plants(plants)

print("\nChecking plant health...")
GardenManager.check_health(tomato)
GardenManager.check_health(lettuce)

print("\nTesting error recovery...")
GardenManager.test_error_recovery()

print("\nGarden management system test complete!")
