class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 0.8

    def age_up(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    plant.show()

    initial_height = plant.height

    for day in range(1, 8):
        print(f"\n=== Day {day} ===")
        plant.grow()
        plant.age_up()
        plant.show()

    total_growth = plant.height - initial_height
    print(f"\nGrowth this week: {round(total_growth, 1)}cm")
