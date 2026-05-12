import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Unstoppable",
        "Hidden Path Finder"
    ]

    amount = random.randint(4, 8)

    player_set: set[str] = set()

    while len(player_set) < amount:
        player_set.add(
            random.choice(achievements)
        )
    return player_set


print("=== Achievement Tracker System ===")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print("\nPlayer Alice:", alice)
print("Player Bob:", bob)
print("Player Charlie:", charlie)
print("Player Dylan:", dylan)

all_ach = (
    alice
    .union(bob)
    .union(charlie)
    .union(dylan)
)
print("\nAll distinct achievements:", all_ach)

common = (
    alice
    .intersection(bob)
    .intersection(charlie)
    .intersection(dylan)
)

print("\nCommon achievements:", common)

print(
    "\nOnly Alice has:",
    alice.difference(
        bob.union(charlie).union(dylan)
    )
)

print(
    "Only Bob has:",
    bob.difference(
        alice.union(charlie).union(dylan)
    )
)

print(
    "Only Charlie has:",
    charlie.difference(
        alice.union(bob).union(dylan)
    )
)

print(
    "Only Dylan has:",
    dylan.difference(
        alice.union(bob).union(charlie)
    )
)

print("\nAlice is missing:",
      all_ach.difference(alice))

print("Bob is missing:",
      all_ach.difference(bob))

print("Charlie is missing:",
      all_ach.difference(charlie))

print("Dylan is missing:",
      all_ach.difference(dylan))
