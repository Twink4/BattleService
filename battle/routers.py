from fastapi import APIRouter, Body

from typing import Annotated

from .schemas import SchemaUser
from .utils import reg_battle, battle_result


battle = APIRouter(
    prefix="/battle"
)


@battle.post("/start")
async def start_battle(
    battlers: Annotated[
        list[SchemaUser],
        Body(
            min_length=2,
            max_length=2
        )
    ]
):
    return await reg_battle(battlers)


@battle.get("/{id}")
async def result(
    id,
):
    return await battle_result(id)
