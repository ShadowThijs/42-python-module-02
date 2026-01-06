"""Using Finally block to cleanup."""


def water_plants(plant_list: list) -> None:
    """Water plants."""
    print("Opening watering system")
    current_plant: str = ""
    try:
        for plant in plant_list:
            current_plant = plant
            _ = plant + ""
            print(f"Watering {plant}")
    except TypeError:
        print(f"Error: Cannot water {current_plant} - invalid plant!")
    except Exception:
        print(f"Error: Cannot water {current_plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    list_plants: list = ["tomato", "lettuce", "carrots"]
    water_plants(list_plants)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    wrong_list: list = ["tomato", None]
    water_plants(wrong_list)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
