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


class ItemServiceImplement(ItemServiceInterface):
    def create_item(self, dto: dict[str, Any]) -> dict[str, Any]:
        return dto

    def get_item(self, dto: dict[str, Any]) -> dict[str, Any]:
        return dto


### --- BindMe DI settings

from bindme import container, inject


container.register(abstract_class=ItemServiceInterface, concrete_class=ItemServiceImplement)


### --- FastAPI routers settings

from pydantic import BaseModel


class ItemDTO(BaseModel):
    name: str


from fastapi import APIRouter

router = APIRouter()


@router.post("/item")
@inject
def create_item_controller(
        dto: ItemDTO,
        item_service: ItemServiceInterface # by @inject - implement will parse in function parameters
) -> dict[str, Any]:
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