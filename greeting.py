def greet(name: str) -> str:
    if name is None:
        raise ValueError("name must not be None")
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
