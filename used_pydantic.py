from pydantic import validate_arguments


@validate_arguments
def soma(x: int, y: int) -> int:
    return x + y
