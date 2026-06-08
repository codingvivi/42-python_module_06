from alchemy.grimoire.light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    ingredient_tokens = {t.strip(",.").lower() for t in ingredients.split()}
    output: str = f"{ingredients} - "

    if any(a in ingredient_tokens for a in allowed):
        output += "VALID"
    else:
        output += "INVALID"

    return output
