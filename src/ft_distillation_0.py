import alchemy.potions

if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(
        f"Testing {alchemy.potions.strength_potion.__name__}: "
        f"{alchemy.potions.strength_potion()}"
    )
    print(
        f"Testing {alchemy.potions.healing_potion.__name__}: "
        f"{alchemy.potions.healing_potion()}"
    )
