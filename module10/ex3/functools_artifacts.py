from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce spell powers using functools.reduce.
    """

    if not spells:
        return 0

    if operation == "add":
        return reduce(add, spells)

    if operation == "multiply":
        return reduce(mul, spells)

    if operation == "max":
        return reduce(max, spells)

    if operation == "min":
        return reduce(min, spells)

    raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "lightning": partial(base_enchantment, 50, "Lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n < 0:
        raise ValueError("n must be non-negative")

    if n in (0, 1):
        return n

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


# Example enchantment function

def enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment ({power}) on {target}"


if __name__ == "__main__":

    print("Testing spell reducer...")

    spells = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")

    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher(3.14))
