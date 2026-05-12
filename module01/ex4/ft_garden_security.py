class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print(
        f"Plant created: {plant.name}: "
        f"{plant.get_height()}cm, "
        f"{plant.get_age()} days old\n"
    )

    plant.set_height(25.0)
    plant.set_age(30)

    print()

    plant.set_height(-5)
    plant.set_age(-10)

    print("\nCurrent state:", end=" ")
    plant.show()
