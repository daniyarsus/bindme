from typing import Type, TypeVar, Dict, Any
from abc import ABC, abstractmethod
import inspect

T = TypeVar('T', bound=ABC)

class DIContainer:
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


container = DIContainer()
