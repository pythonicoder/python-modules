# lambda_spells.py

from typing import List, Dict


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"}
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))
