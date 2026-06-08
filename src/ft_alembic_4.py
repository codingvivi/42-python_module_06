import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")

    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    # create_earth is not exposed by the package: AttributeError at runtime,
    # and a mypy error here on purpose (per the subject).
    print(
        "Testing the hidden create_earth: "
        f"{alchemy.create_earth()}"  # type: ignore[attr-defined]
    )
