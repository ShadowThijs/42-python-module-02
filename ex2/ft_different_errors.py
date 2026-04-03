"""Different types of problems.

Demonstrates handling multiple exception types in garden operations.
"""


def garden_operations(operation_number: int) -> None:
    """Run a garden operation that may raise different exceptions."""
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        result: int = 1 // 0  # noqa: F841
    elif (operation_number == 2):
        open("/non/existent/file")
    elif (operation_number == 3):
        result2: str = "garden" + 42  # type: ignore


def test_error_types() -> None:
    """Show each error type occurring and being caught."""
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            error_name: str = type(e).__name__
            print(f"Caught {error_name}: {e}")
    print("All error types tested successfully!")


test_error_types()
