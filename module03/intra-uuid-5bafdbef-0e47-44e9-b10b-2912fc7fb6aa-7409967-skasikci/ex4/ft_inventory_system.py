import sys

print("=== Inventory System Analysis ===")

if len(sys.argv) == 1:
    print(
        "Usage: python3 ft_inventory_system.py item:quantity ..."
    )
    sys.exit()

inventory = {}

i = 1
while i < len(sys.argv):

    arg = sys.argv[i]

    if ":" not in arg:
        print("Error - invalid parameter '" + arg + "'")
        i += 1
        continue

    item, qty = arg.split(":")

    if item in inventory:
        print("Redundant item '" + item + "' - discarding")
        i += 1
        continue

    try:
        inventory.update({
            item: int(qty)
        })

    except ValueError as e:
        print("Quantity error for '" +
              item +
              "':",
              e)

    i += 1


print("Got inventory:", inventory)


items = list(inventory.keys())

print("Item list:", items)


total = sum(
    inventory.values()
)

print("Total quantity of the 5 items:", total)

if total > 0:
    for item in inventory:
        percent = round(
            (inventory[item] / total) * 100,
            1
        )

        print(
            "Item",
            item,
            "represents",
            str(percent) + "%"
        )

if len(items) == 0:
    sys.exit()

# most abundant
most_item = items[0]

for item in items:
    if inventory[item] > inventory[most_item]:
        most_item = item


# least abundant
least_item = items[0]

for item in items:
    if inventory[item] < inventory[least_item]:
        least_item = item


print(
    "Item most abundant:",
    most_item,
    "with quantity",
    inventory[most_item]
)

print(
    "Item least abundant:",
    least_item,
    "with quantity",
    inventory[least_item]
)


inventory.update({
    "magic_item": 1
})

print(
    "Updated inventory:",
    inventory
)
