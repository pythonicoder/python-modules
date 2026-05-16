from ex1 import HealingCreatureFactory, TransformCreatureFactory

from ex1.heal import HealCapability
from ex1.transform import TransformCapability

from ex0.factory import CreatureFactory


def test_heal(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    if isinstance(base, HealCapability):
        print("base:")
        print(base.describe())
        print(base.attack())
        print(base.heal())

    if isinstance(evolved, HealCapability):
        print("evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.heal())


def test_transform(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    if isinstance(base, TransformCapability):
        print("base:")
        print(base.describe())
        print(base.attack())
        print(base.transform())
        print(base.attack())
        print(base.revert())

    if isinstance(evolved, TransformCapability):
        print("evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    test_heal(HealingCreatureFactory())

    print("\nTesting Creature with transform capability")
    test_transform(TransformCreatureFactory())
