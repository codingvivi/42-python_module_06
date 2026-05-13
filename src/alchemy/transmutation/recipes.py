from elements import create_fire

from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    intro: str = "Recipe transmuting Lead to Gold: "
    content: str = f"brew '{create_air}' and '{strength_potion}' mixed with '{create_fire}'"
    return intro + content
