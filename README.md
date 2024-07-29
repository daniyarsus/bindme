<h1 align="center">BindMe</h1>

<p align="center">
  <img src="assets/technologies/bindme-logo.png" alt="BindMe Logo" height="300">
</p>

<p align="center">
  <strong>Simple DI Framework for Python 3.x 🐍</strong>
</p>

<hr>

<h1 align="center">Usage</h1>

<p align="center">
  <strong>Installation Instructions:</strong>
</p>

<p align="center">
  To install the package, run:
</p>

<p align="center">
  <code>pip install bindme</code>
</p>

<hr>

<h1 align="center">Features</h1>

<p align="center">
  <strong>Interesting Highlights:</strong>
</p>

<ul align="center">
  <p><strong>Simple 📕</strong> - everything you need is here!</p>
  <p><strong>Fast ⚡</strong> - awesome work speed!</p>
  <p><strong>Low 🍃</strong> - weighs nothing at all!</p>
</ul>

<p align="center">
  <img src="assets/common/di_meme_1.png" alt="DI meme 1 Logo" height="250">
</p>

<hr>

<h1 align="center">Use Cases</h1>

<p align="center">
  <strong>Examples:</strong>
</p>

<h3 align="center"> project structure </h3>
<p align="center">
   <img src="assets/technologies/example_structure.png" height="160">
</p>

```python
# create interface

from abc import ABC, abstractmethod
from typing import Any, NoReturn


class ItemServiceInterface(ABC):
    @abstractmethod
    def create_one(self, dto: dict[str, Any]) -> NoReturn:
        raise NotImplementedError("<create one> method is not implemented!")

    @abstractmethod
    def get_one(self, dto: dict[str, Any]) -> NoReturn:
        raise NotImplementedError("<get one> method is not implemented!")


# create implement

from typing import override

from src.interfaces.item import ItemServiceInterface


class ItemServiceImplement(ItemServiceInterface):
    @override
    def create_one(self, dto: dict[str, Any]) -> None:
        print(f"Item with {dto} is created!")
    
    @override
    def get_one(self, dto: dict[str, Any]) -> None:
        print(f"Item with {dto} is get!")


# configure bindme

from bindme import container

from src.interfaces.item import ItemServiceInterface
from src.implements.item import ItemServiceImplement

container.register(abstract_class=ItemServiceInterface, concrete_class=ItemServiceImplement)

# use container directly from code

from bindme import container

from src.implements.item import ItemServiceInterface


def get_item_service() -> None:
    item_service = container.resolve(abstract_class=ItemServiceInterface)
    item_service.create_one({"name": "Bob"})
    # item_service.get_one({"name": "Bob"})


get_item_service()

# use @injector decorator to parse in parameters

from bindme import inject

from src.implements.item import ItemServiceInterface


@inject
def get_item_service(item_service: ItemServiceInterface) -> None:
    item_service.create_one(dto={"name": "Bob"})
    # item_service.get_one(dto={"name": "Bob"})


get_item_service(item_service=ItemServiceImplement)


```