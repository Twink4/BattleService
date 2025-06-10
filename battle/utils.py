import uuid
import random

from .db import database
from .schemas import SchemaUser


async def check_battle_id(battle_id):
    return battle_id in database


async def reg_battle(battlers: list[SchemaUser]) -> str:
    battle_id = str(uuid.uuid4())

    database[battle_id] = battlers

    return battle_id if await check_battle_id(battle_id) else "Ошибка создания битвы"


async def game(battle_id):
    battlers = database[battle_id]

    if battlers[0].power < battlers[1].power:
        winner_id = 1
    elif battlers[0].power > battlers[1].power:
        winner_id = 0
    else:
        winner_id = random.randint(0, 1)

    database[battle_id] = {
        "id_game": battle_id,
        "winner": battlers[winner_id].name
    }


async def battle_result(battle_id):
    if not await check_battle_id(battle_id):
        return {"error": "Игра не найдена, введен неверный идентификатор игры"}
    await game(battle_id)
    return database[battle_id]
