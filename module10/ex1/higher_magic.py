from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power)
        )

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_spell


# Example spells

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target}"


# Example condition

def enough_power(target: str, power: int) -> bool:
    return power >= 20


if __name__ == "__main__":

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)

    result1, result2 = combined("Dragon", 10)

    print(f"Combined spell result: {result1}, {result2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)

    print(f"Original: 10, Amplified: {10 * 3}")

    print("\nTesting conditional caster...")
    safe_spell = conditional_caster(enough_power, fireball)

    print(safe_spell("Goblin", 10))
    print(safe_spell("Goblin", 30))

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, lightning])

    results = combo("Ogre", 25)

    for result in results:
        print(result)
