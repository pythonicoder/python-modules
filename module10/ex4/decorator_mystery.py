import time
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Casting {func.__name__}...")

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(
            f"Spell completed in "
            f"{end_time - start_time:.3f} seconds"
        )

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            if len(args) > 1:
                power = args[-1]
            else:
                power = args[0]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)

                except Exception:

                    attempts += 1

                    if attempts < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempts}/{max_attempts})"
                        )

            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def validate_mage_name(name: str) -> bool:

        return (
            len(name) >= 3
            and all(
                char.isalpha() or char.isspace()
                for char in name
            )
        )

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int
    ) -> str:

        return (
            f"Successfully cast {spell_name} "
            f"with {power} power"
        )


@spell_timer
def fireball():

    time.sleep(0.101)

    return "Fireball cast!"


@retry_spell(3)
def unstable_spell():

    raise ValueError("Spell failed")


if __name__ == "__main__":

    print("Testing spell timer...")

    result = fireball()

    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    print(unstable_spell())

    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")

    guild = MageGuild("Merlin")

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("A1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
