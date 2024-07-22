# create interface

from abc import ABC, abstractmethod
from typing import Any, NoReturn


class ItemServiceInterface:
    @abstractmethod
    def create_one(self, dto: dict[str, Any]) -> NoReturn:
        raise NotImplementedError("<create one> method is not implemented!")

    @abstractmethod
    def get_one(self, dto: dict[str, Any]) -> NoReturn:
        raise NotImplementedError("<get one> method is not implemented!")


# create implement


class ItemServiceImplement(ItemServiceInterface):
    def create_one(self, dto: dict[str, Any]) -> None:
        print(f"Item with {dto} is created!")

    def get_one(self, dto: dict[str, Any]) -> None:
        print(f"Item with {dto} is get!")


# configure bindme


from bindme import container

container.register(abstract_class=ItemServiceInterface, concrete_class=ItemServiceImplement)

# use container directly from code

from bindme import container


def get_item_service():
    item_service = container.resolve(abstract_class=ItemServiceInterface)
    item_service.create_one({"name": "Bob"})
    # item_service.get_one({"name": "Bob"})


get_item_service()

# use @injection decorator

from bindme import inject


@inject
def get_item_service(item_service: ItemServiceInterface):
    item_service.create_one(dto={"name": "Bob"})
    # item_service.get_one(dto={"name": "Bob"})


get_item_service(item_service=ItemServiceImplement)