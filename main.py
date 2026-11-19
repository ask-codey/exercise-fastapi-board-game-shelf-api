"""The Rolling Dice café's API. Ready to use: it makes the app and adds the games router.

Run it with:  fastapi dev main.py
Then open http://127.0.0.1:8000/docs to try every route. Stop it with Ctrl+C.
"""
from fastapi import FastAPI

from routers import games

app = FastAPI(title="Rolling Dice")
app.include_router(games.router)
