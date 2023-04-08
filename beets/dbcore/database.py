import inspect
from typing import Callable, NamedTuple, Optional, Set


class FunctionDef(NamedTuple):
    name: str
    arg_count: int
    func: Callable


FUNCTIONS_TO_REGISTER: Set[FunctionDef] = set()


def add_db_function(name: Optional[str] = None) -> Callable:
    def add_db_function_to_register(func: Callable) -> Callable:
        num_args = len(inspect.signature(func).parameters)
        FUNCTIONS_TO_REGISTER.add(FunctionDef(name or func.__name__, num_args, func))
        return func

    return add_db_function_to_register
