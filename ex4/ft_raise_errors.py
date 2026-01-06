"""Raise your own errors."""


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Checks the plants health."""
    water_error: str = f"Water level {water_level} "
    sunlight_error: str = f"Sunlight hours {sunlight_hours} "
    water_low: str = "is too low (min 1)"
    water_high: str = "is too high (max 10)"
    sun_low: str = "is too low (min 2)"
    sun_high: str = "is too high (max 12)"
    try:
        if not plant_name:
            raise (ValueError("Plant name cannot be empty!"))
        if (water_level <= 1):
            water_low: str = "is too low (min 1)"
            raise (ValueError(water_error + water_low))
        elif (water_level >= 10):
            raise (ValueError(water_error + water_high))
        if (sunlight_hours <= 2):
            raise (ValueError(sunlight_error + sun_low))
        elif (sunlight_hours >= 12):
            raise (ValueError(sunlight_error + sun_high))
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    """Automated tester for all plant errors."""
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    check_plant_health("tomato", 4, 6)
    print("\nTesting empty plant name...")
    check_plant_health("", 4, 6)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 8)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 4, 0)
    print("\nAll errors raising tests completed!")


test_plant_checks()
