# relative import
from ..elements import create_air

# absolute import
from elements import create_fire

# relative import
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and "
        f"'{strength_potion()}' mixed with "
        f"'{create_fire()}'"
    )
