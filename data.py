"""The Rolling Dice café's shelf of games. Ready to use: you don't need to change this file.

Each game is made for groups of min_players to max_players people, and takes about `minutes` to play.
The routes read and change the GAMES list. Keep it the same list: add to it with GAMES.append().
"""
import copy

STARTING_GAMES = [
    {"id": 1, "title": "Harbor Lights", "min_players": 2, "max_players": 4, "minutes": 45, "available": True},
    {"id": 2, "title": "Moon Mice", "min_players": 3, "max_players": 6, "minutes": 20, "available": False},
    {"id": 3, "title": "Tile Town", "min_players": 1, "max_players": 2, "minutes": 30, "available": True},
    {"id": 4, "title": "Dragon's Picnic", "min_players": 3, "max_players": 5, "minutes": 60, "available": True},
    {"id": 5, "title": "Pocket Pirates", "min_players": 2, "max_players": 2, "minutes": 15, "available": True},
    {"id": 6, "title": "Word Garden", "min_players": 2, "max_players": 8, "minutes": 25, "available": False},
    {"id": 7, "title": "Castle Cooks", "min_players": 1, "max_players": 1, "minutes": 50, "available": True},
    {"id": 8, "title": "Night Train", "min_players": 5, "max_players": 10, "minutes": 40, "available": True},
]

GAMES = copy.deepcopy(STARTING_GAMES)


def reset_games():
    """Puts the shelf back to the eight games above. The tests call it before each test, so every test starts the same."""
    GAMES.clear()
    GAMES.extend(copy.deepcopy(STARTING_GAMES))
