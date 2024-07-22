from typing import Type, TypeVar, Dict, Any
from abc import ABC, abstractmethod

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
        return concrete_class()


container = DIContainer()