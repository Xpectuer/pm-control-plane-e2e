def greet(name: str) -> str:
    if name is None:
        raise ValueError("name must not be null")
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = " ".join(name.split())
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
