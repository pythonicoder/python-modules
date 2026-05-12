def test_errors():
    print("=== Garden Error Types Demo ===")

    operations = [
        lambda: int("abc"),
        lambda: 10 / 0,
        lambda: open("/non/existent/file"),
        lambda: "hello" + 5,
        lambda: int("42")
    ]

    for i, op in enumerate(operations):
        print(f"Testing operation {i}...")
        try:
            op()
            print("Operation completed succesfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Cught TypeError: {e}")

    print("\nAll error types tested succesfully!")


if __name__ == "__main__":
    test_errors()
