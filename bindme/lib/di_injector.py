from functools import wraps
import inspect
from typing import Callable, Type, Any
from bindme.lib.di_container import container


def inject(func: Callable) -> Callable:
    """
    A decorator that automatically injects dependencies into the decorated function or method.

    This decorator uses the `container` to resolve dependencies based on the type annotations
    of the function's parameters. If a parameter type is registered in the container, it will
    be injected automatically. Otherwise, the original argument value will be used.

    Args:
        func (Callable): The function or method to decorate.

    Returns:
        Callable: The wrapped function with dependencies injected.

    Example:
        @inject
        def my_function(service: MyService, value: int):
            service.do_something(value)

        container.register(MyService, MyServiceImplementation())
        my_function(value=42)  # MyServiceImplementation instance is injected automatically
    """
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
