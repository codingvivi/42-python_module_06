import alchemy.potions

if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(
        f"Testing {alchemy.potions.strength_potion.__name__}: {alchemy.potions.strength_potion()}"
    )
    print(f"Testing {alchemy.potions.healing_potion.__name__}: {alchemy.potions.healing_potion()}")
