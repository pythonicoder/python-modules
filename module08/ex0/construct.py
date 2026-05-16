import sys
import os
import site


def status() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    matrix_status = status()

    print()

    if not matrix_status:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()

        print("Global package location:")
        try:
            print(site.getsitepackages()[0])
        except Exception:
            print("Unavailable")

        print()

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")

    else:
        env_name = os.path.basename(sys.prefix)

        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
        print()

        print("SUCCESS: You're in an isolated environment!")
        print("You can install packages without affecting")
        print("the global system.")
        print()

        print("Virtual package location:")
        try:
            print(site.getsitepackages()[0])
        except Exception:
            print("Unavailable")

    print()


if __name__ == "__main__":
    main()
