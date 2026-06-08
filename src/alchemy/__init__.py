def _create_element(element: str) -> str:
    return f"{element} element created"


from .elements import create_air  # noqa: E402
from .potions import healing_potion, strength_potion  # noqa: E402
from .transmutation import lead_to_gold  # noqa: E402

# create_earth is intentionally NOT exposed (see ft_alembic_4.py)
__all__ = [
    "lead_to_gold",
    "strength_potion",
    "healing_potion",
    "heal",
    "create_air",
]
heal = healing_potion
