import math
from typing import Tuple


def get_player_pos() -> Tuple[float, float, float]:
    while True:
        coords = input(
            "Enter new coordinates as floats in format 'x,y,z: "
        )
        try:
            x, y, z = coords.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            position = (
                float(x),
                float(y),
                float(z)
            )
            return position
        except ValueError as e:
            if not x.replace('.', '', 1).isdigit():
                bad = x
            elif not y.replace('.', '', 1).isdigit():
                bad = y
            else:
                bad = z

            print("Error on parameter '" +
                  bad +
                  "':",
                  e)


print("=== Game Coordinate System ===")

print("\nGet a first set of coordinates")
pos1 = get_player_pos()

print("Got a first tuple:", pos1)

print(
    "It includes:",
    "X=" + str(pos1[0]) + ",",
    "Y=" + str(pos1[1]) + ",",
    "Z=" + str(pos1[2])
)

distance_center = math.sqrt(
    pos1[0] ** 2 +
    pos1[1] ** 2 +
    pos1[2] ** 2
)

print("Distance to center:",
      round(distance_center, 4))

print("\nGet a second set of coordinates")
pos2 = get_player_pos()

distance_between = math.sqrt(
    (pos2[0] - pos1[0]) ** 2 +
    (pos2[1] - pos1[1]) ** 2 +
    (pos2[2] - pos1[2]) ** 2
)

print("Distance between two set of coordinates:",
      round(distance_between, 4))
