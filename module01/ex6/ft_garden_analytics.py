class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def __init__(self, name, height, age):
        self.name = name
        self._height = round(height, 1)
        self._age = age
        self._stats = Plant.Stats()

    def grow(self):
        self._stats.grow_calls += 1

    def age_up(self):
        self._age += 20
        self._stats.age_calls += 1

    def show(self):
        self._stats.show_calls += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


# flower
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def grow(self):
        self._height = round(self._height + 8.0, 1)
        self._stats.grow_calls += 1

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


# tree
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self):
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


# seed
class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def grow(self):
        self._height = round(self._height + 30.0, 1)
        self._stats.grow_calls += 1

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


# globalstats
def show_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f"{plant._shade_calls} shade")


if __name__ == "__main__":

    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    sunflower.show()
    show_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    show_statistics(unknown)
