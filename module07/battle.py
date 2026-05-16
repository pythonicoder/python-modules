from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    print("Testing factory")
    test_factory(FlameFactory())
    print()

    print("Testing factory")
    test_factory(AquaFactory())
    print()

    print("Testing battle")
    battle(FlameFactory(), AquaFactory())
