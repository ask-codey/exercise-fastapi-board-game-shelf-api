"""The Rolling Dice café's games router: for you to finish.

Every request it should answer, with its status code and body:

  GET /games                           200, every game in data.py
  GET /games?players=4                 200, only the games made for a group of 4 (min_players 4 or fewer
                                       and max_players 4 or more): games 1, 2, 4 and 6
  GET /games?max_minutes=30            200, only the games that take 30 minutes or less: games 2, 3, 5 and 6
  GET /games?players=4&max_minutes=30  200, only the games that pass both filters: games 2 and 6
  GET /games?players=12                200, an empty list, []: no game is made for a group of 12
  GET /games?players=four              422, FastAPI's own answer: players is a whole number
  GET /games/4                         200, game 4 (every game's id works the same way)
  GET /games/99                        404, {"detail": "There's no game 99."}
  GET /games/chess                     422, FastAPI's own answer: a game's id is a whole number
  POST /games                          201, the new game, kept on the shelf. For the body
                                       {"title": "Lantern Festival", "min_players": 2, "max_players": 4, "minutes": 35}
                                       the answer is {"id": 9, "title": "Lantern Festival", "min_players": 2,
                                       "max_players": 4, "minutes": 35, "available": true}: its id is one more
                                       than the number of games on the shelf, and a new game is always available
  POST /games, a body with no minutes  422, FastAPI's own answer: the body needs all four fields

The docs page lists these routes under the heading "games", and the list's address is exactly /games
(no slash at the end).
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from data import GAMES

# Give the router the prefix "/games" and the tag "games". Then add the routes below it.
router = APIRouter()
