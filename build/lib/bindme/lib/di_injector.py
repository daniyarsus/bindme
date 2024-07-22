from functools import wraps
import inspect
from typing import Callable, Type, Any
from bindme.lib.di_container import container


def inject(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)

        resolved_args = {}

        for name, param in sig.parameters.items():
            if param.annotation in container._registrations:
                resolved_args[name] = container.resolve(param.annotation)
            else:
                resolved_args[name] = bound_args.arguments.get(name, None)

        return func(**resolved_args)

    return wrapper
