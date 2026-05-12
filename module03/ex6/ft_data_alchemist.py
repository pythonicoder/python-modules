import random

print("=== Game Data Alchemist ===")


players = [
    'Alice',
    'bob',
    'Charlie',
    'dylan',
    'Emma',
    'Gregory',
    'john',
    'kevin',
    'Liam'
]

print(
    "\nInitial list of players:",
    players
)

all_caps = []

for name in players:
    all_caps.append(
        name.capitalize()
    )

print(
    "New list with all names capitalized:",
    all_caps
)

caps_only = []

for name in players:
    if name[0].isupper():
        caps_only.append(name)

print(
    "New list of capitalized names only:",
    caps_only
)

scores = {name: random.randint(1, 1000) for name in all_caps}

print(
    "\nScore dict:",
    scores
)

avg = round(
    sum(scores.values()) /
    len(scores),
    2
)

print(
    "Score average is",
    avg
)

high_scores = {name: score for name, score in scores.items() if score > avg}

print(
    "High scores:",
    high_scores
)
