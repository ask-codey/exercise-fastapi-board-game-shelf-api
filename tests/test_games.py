# Tests for the games router. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test sends one request to the app, the request in its name, and checks the status code and the body that come
# back. TestClient hands each request straight to the app, so no server needs to be running. A failing test says what
# it sent, what it expected and what came back.
# You don't need to change this file. Module 2 shows how tests like these are written.
import pytest
from fastapi.testclient import TestClient

from data import STARTING_GAMES, reset_games
from main import app

client = TestClient(app)

LANTERN_FESTIVAL = {"title": "Lantern Festival", "min_players": 2, "max_players": 4, "minutes": 35}


@pytest.fixture(autouse=True)
def fresh_shelf():
    """Puts the shelf back to its eight games before every test, so a game one test adds isn't there in the next."""
    reset_games()


def check_status(request, response, status):
    """Fails with a message that says what the request answered, when its status code isn't the one expected."""
    assert response.status_code == status, (
        f"{request} should answer {status}, but it answered {response.status_code} with {response.text}"
    )


def check_body(request, response, body):
    """Fails with a message that says what came back, when the body isn't the one expected."""
    assert response.json() == body, f"{request} should answer {body!r}, but it answered {response.json()!r}."


def check_game_ids(request, response, ids):
    """Checks a 200 with a list of games, by their ids, and says which games came back when they're wrong."""
    check_status(request, response, 200)
    body = response.json()
    assert isinstance(body, list), f"{request} should answer a list of games, but it answered {body!r}."
    got = [game.get("id") if isinstance(game, dict) else game for game in body]
    assert got == ids, f"{request} should answer the games with ids {ids}, but it answered the games with ids {got}."


def test_1_get_games_answers_200_with_all_8_games():
    response = client.get("/games")
    check_status("GET /games", response, 200)
    check_body("GET /games", response, STARTING_GAMES)


def test_2_get_games_players_4_answers_games_1_2_4_and_6():
    check_game_ids("GET /games?players=4", client.get("/games?players=4"), [1, 2, 4, 6])


def test_3_get_games_max_minutes_30_answers_games_2_3_5_and_6():
    check_game_ids("GET /games?max_minutes=30", client.get("/games?max_minutes=30"), [2, 3, 5, 6])


def test_4_get_games_players_4_and_max_minutes_30_answers_games_2_and_6():
    request = "GET /games?players=4&max_minutes=30"
    check_game_ids(request, client.get("/games?players=4&max_minutes=30"), [2, 6])


def test_5_get_games_players_12_answers_an_empty_list():
    check_game_ids("GET /games?players=12", client.get("/games?players=12"), [])


def test_6_get_games_players_four_answers_422():
    check_status("GET /games?players=four", client.get("/games?players=four"), 422)


def test_7_get_games_4_answers_200_with_dragons_picnic():
    response = client.get("/games/4")
    check_status("GET /games/4", response, 200)
    check_body("GET /games/4", response, STARTING_GAMES[3])


def test_8_get_games_99_answers_404_theres_no_game_99():
    response = client.get("/games/99")
    check_status("GET /games/99", response, 404)
    check_body("GET /games/99", response, {"detail": "There's no game 99."})


def test_9_get_games_chess_answers_422():
    check_status("GET /games/chess", client.get("/games/chess"), 422)


def test_10_post_games_lantern_festival_answers_201_with_id_9():
    response = client.post("/games", json=LANTERN_FESTIVAL)
    check_status("POST /games with Lantern Festival", response, 201)
    check_body("POST /games with Lantern Festival", response, {"id": 9, **LANTERN_FESTIVAL, "available": True})


def test_11_post_games_lantern_festival_then_get_games_9_finds_it():
    client.post("/games", json=LANTERN_FESTIVAL)
    response = client.get("/games/9")
    check_status("GET /games/9, after POST /games with Lantern Festival,", response, 200)
    check_body("GET /games/9, after POST /games with Lantern Festival,", response,
               {"id": 9, **LANTERN_FESTIVAL, "available": True})


def test_12_post_games_with_no_minutes_answers_422():
    body = {"title": "Lantern Festival", "min_players": 2, "max_players": 4}
    check_status("POST /games with no minutes", client.post("/games", json=body), 422)


def test_13_the_docs_page_lists_get_games_under_the_tag_games():
    paths = client.get("/openapi.json").json()["paths"]
    route = paths.get("/games", {}).get("get")
    slash = " A route written @router.get(\"/\") answers at /games/, with a slash: write \"\" instead." \
        if "/games/" in paths else ""
    assert route is not None, (
        "The docs page should list GET /games, but it doesn't. It lists: " + (", ".join(paths) or "no routes")
        + "." + slash
    )
    assert route.get("tags") == ["games"], (
        f"GET /games should be listed under the tag games, but its tags are {route.get('tags', [])}."
    )
