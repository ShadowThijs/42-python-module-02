"""Handle different errors."""

def garden_operations(operation_type: str) -> None:
    """Perform operations that might raise different errors."""
    if operation_type == "value":
        _ = int("abc")
    elif operation_type == "zero":
        _ = 10 / 0
    elif operation_type == "file":
        _ = open("missing.txt")
    elif operation_type == "key":
        dictionary: dict[str, str] = {"plant": "rose"}
        _ = dictionary["missing_plant"]
    elif operation_type == "multiple":
        value = int("maybe_bad_input")
        _ = value / 0

def test_error_types() -> None:
    """Test all error types."""
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print("\nTesting multiple errors together...")
    try:
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


print("=== Garden Error Types Demo ===")
test_error_types()
