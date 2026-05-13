from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def _potion(type: str, element1: str, element2: str) -> str:
    return f"{type} potion brewed with {element1} and {element2}"


def healing_potion() -> str:
    return _potion("Healing", create_earth(), create_air())


def strength_potion() -> str:
    return _potion("Strenght", create_fire(), create_water())
