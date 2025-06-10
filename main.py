import uvicorn

from fastapi import FastAPI

from battle.routers import battle

app = FastAPI()

app.include_router(battle)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app"
    )