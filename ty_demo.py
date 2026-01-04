def greet(name: str) -> str:
    return f"Hello, {name}"

def add_numbers(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> None:
    for item in items:
        print(item.upper())

def main() -> None:
    # Rule 1: Invalid Argument Type (passing int instead of str)
    # ty: invalid-argument-type
    print(greet(123))

    # Rule 2: Incompatible Assignment (assigning str to int)
    # ty: incompatible-assignment
    count: int = "five"
    add_numbers(count, 10)

    # Rule 3: List Homogeneity (appending int to list[str])
    names: list[str] = ["Alice", "Bob"]
    names.append(42)

    # Rule 4: Optional Handling (passing None where not optional)
    # ty: argument-type
    greet(None)

    # Rule 5: Container Type Mismatch (passing set instead of list)
    # ty: argument-type
    process_items({"apple", "banana"})


if __name__ == "__main__":
    main()
