import random
from collections.abc import Generator

Event = tuple[str, str]


def gen_event() -> Generator[Event, None, None]:

    players = [
        "alice",
        "bob",
        "charlie",
        "dylan"
    ]

    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "use",
        "release"
    ]

    while True:

        yield (
            random.choice(players),
            random.choice(actions)
        )


def consume_event(
    events: list[Event],
) -> Generator[Event, None, None]:

    while len(events) > 0:

        index = random.randint(
            0,
            len(events)-1
        )

        picked = events[index]

        events.pop(index)

        yield picked


print("=== Game Data Stream Processor ===")


stream = gen_event()

for i in range(1000):

    event = next(stream)

    print(
      "Event",
      str(i)+":",
      "Player",
      event[0],
      "did action",
      event[1]
    )


events = []

for i in range(10):
    events.append(
        next(stream)
    )

print(
    "\nBuilt list of 10 events:",
    events
)


for event in consume_event(events):

    print(
        "Got event from list:",
        event
    )

    print(
        "Remains in list:",
        events
    )
