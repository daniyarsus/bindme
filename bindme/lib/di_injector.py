from typing import Callable, get_type_hints

from .di_container import container


def inject(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        type_hints = get_type_hints(func)
        for param, param_type in type_hints.items():
            if param not in kwargs:
                kwargs[param] = container.resolve(param_type)
        return func(*args, **kwargs)
    return wrapper
