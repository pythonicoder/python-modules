from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)
from ex0.creature import Creature
from ex2.strategy import BattleStrategy


Opponent = Tuple[CreatureFactory, BattleStrategy]


def get_family_name(creature: Creature) -> str:
    if hasattr(creature, "heal"):
        return "Healing"
    if hasattr(creature, "transform"):
        return "Transform"
    return creature.name


def format_opponents(opponents: List[Opponent]) -> str:
    result = []

    for factory, strategy in opponents:
        creature = factory.create_base()

        cname = get_family_name(creature)
        sname = strategy.__class__.__name__.replace("Strategy", "")

        result.append(f"({cname}+{sname})")

    return "[ " + ", ".join(result) + " ]"


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()
            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                s1.act(c1)
                s2.act(c2)

            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return

            print()


if __name__ == "__main__":
    print("Tournament 0 (basic)")

    t0: List[Opponent] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(),
         DefensiveStrategy()),
    ]

    print(format_opponents(t0))
    battle(t0)

    print("\nTournament 1 (error)")

    t1: List[Opponent] = [
        (FlameFactory(), AggressiveStrategy()),
        (
            HealingCreatureFactory(),
            DefensiveStrategy()
        ),
    ]

    print(format_opponents(t1))
    battle(t1)

    print("\nTournament 2 (multiple)")

    t2: List[Opponent] = [
        (AquaFactory(), NormalStrategy()),
        (
            HealingCreatureFactory(),
            DefensiveStrategy()
        ),
        (
            TransformCreatureFactory(),
            AggressiveStrategy()
        ),
    ]

    print(format_opponents(t2))
    battle(t2)
