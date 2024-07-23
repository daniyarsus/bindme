from typing import Type, TypeVar, Dict, Any
from abc import ABC, abstractmethod
import inspect

T = TypeVar('T', bound=ABC)

class DIContainer:
    """
    A simple Dependency Injection (DI) Container for managing and resolving dependencies.

    This container allows you to register abstract classes with their concrete implementations,
    and automatically resolves and injects dependencies when creating instances.

    Example:
        container = DIContainer()

        # Define abstract class and its implementation
        class AbstractService(ABC):
            @abstractmethod
            def perform_action(self) -> None:
                pass

        class ConcreteService(AbstractService):
            def perform_action(self) -> None:
                print("Action performed!")

        # Register the implementation with the container
        container.register(AbstractService, ConcreteService)

        # Resolve the implementation and use it
        service = container.resolve(AbstractService)
        service.perform_action()  # Output: Action performed!
    """
    def __init__(self):
        self._registrations: Dict[Type[ABC], Type[ABC]] = {}

    def register(self, abstract_class: Type[T], concrete_class: Type[T]) -> None:
        if not issubclass(concrete_class, abstract_class):
            raise ValueError(f"{concrete_class} is not subclass of {abstract_class}!")
        self._registrations[abstract_class] = concrete_class

    def resolve(self, abstract_class: Type[T]) -> T:
        concrete_class = self._registrations.get(abstract_class)
        if not concrete_class:
            raise ValueError(f"{abstract_class}'s realization hasn't been registered!")
        return self._create_instance(concrete_class)

    def _create_instance(self, concrete_class: Type[T]) -> T:
        constructor_params = inspect.signature(concrete_class.__init__).parameters
        kwargs = {}
        for param in constructor_params.values():
            if param.annotation in self._registrations:
                kwargs[param.name] = self.resolve(param.annotation)
        return concrete_class(**kwargs)

    def clear(self) -> None:
        self._registrations.clear()

    def list_registrations(self) -> Dict[Type[ABC], Type[ABC]]:
        return self._registrations.copy()


container = DIContainer()
