from .dark_spellbook import dark_spell_allowed_ingredients


ALLOWED = dark_spell_allowed_ingredients()


def validate_ingredients(ingredients: str) -> str:
    ingredients_lower = ingredients.lower()

    for item in ALLOWED:
        if item in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
