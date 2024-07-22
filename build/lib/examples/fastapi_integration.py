# --- abstraction

from abc import ABC, abstractmethod
from typing import NoReturn, Any


class ItemServiceInterface(ABC):
    @abstractmethod
    def create_item(self, dto: dict[str, Any]) -> NoReturn:
        raise NotImplementedError("<create_item> method must be implemented")

    @abstractmethod
    def get_item(self, dto: dict[str, Any]) -> NoReturn:
        raise NotImplementedError("<get_item> method must be implemented")


### --- implementation


from pydantic import BaseModel


class ItemDTO(BaseModel):
    name: str


class ItemServiceImplement(ItemServiceInterface):
    def create_item(self, dto: ItemDTO) -> dict[str, Any]:
        return {"name": dto.name}

    def get_item(self, dto: dict[str, Any]) -> dict[str, Any]:
        return dto.copy()


### --- BindMe DI settings

from bindme import container, inject


container.register(abstract_class=ItemServiceInterface, concrete_class=ItemServiceImplement)


@inject
def get_item(dto: ItemDTO, item_service: ItemServiceInterface) -> Any:
    print(item_service.create_item(dto))


get_item(dto=ItemDTO(name="Bob"), item_service=ItemServiceInterface)


class ItemServiceNew:
    @inject
    def __init__(self, item_service: ItemServiceInterface):
        self.item_service = item_service

    def create_item(self, dto: ItemDTO) -> dict[str, Any]:
        self.item_service.create_item(dto)
        print(dto.name)


item_service = ItemServiceNew(item_service=ItemServiceInterface)
item_service.create_item(dto=ItemDTO(name="Bob"))


### --- FastAPI routers settings

from fastapi import APIRouter

router = APIRouter()


@router.post("/item")
def create_item_controller(
        dto: ItemDTO
) -> dict[str, Any]:
    item_service = container.resolve(abstract_class=ItemServiceInterface) #  you can use container directly in code
    return item_service.create_item(dto=dto)


@router.get("/item")
def get_item_controller(
    id: int
) -> dict[str, Any]:
    item_service = container.resolve(abstract_class=ItemServiceInterface) #  you can use container directly in code
    dto = {"id": id}
    return item_service.get_item(dto=dto)


### --- run application :)

if __name__ == "__main__":
    import uvicorn
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )