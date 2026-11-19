# Exercise: Board Game Shelf API

Exercise code for the lesson **Exercise: Board Game Shelf API** in the Python Web APIs course on [ask-codey.com](https://www.ask-codey.com).

The Rolling Dice board game café keeps getting the same questions at the door: "Do you have something for four of us?", "Anything quick?". You'll finish the café's FastAPI app so its staff app can answer them: a games router that lists the shelf with filters for group size and playing time, finds one game by its id, and adds a donated game. Tests send each request to the app and check what comes back.

## What's here

- `routers/games.py`: the games router, for you to finish. The comment at its top lists every request it should answer, with the status code and the body. For now it has no routes, so every request answers 404.
- `routers/__init__.py`: makes the `routers` folder a package, so `main.py` can bring in `routers/games.py`. Ready to use.
- `main.py`: makes the app, `app = FastAPI(title="Rolling Dice")`, and adds the games router with `app.include_router`. Ready to use.
- `data.py`: the café's eight games, in the list `GAMES`, and `reset_games()`, which the tests use to put the shelf back before each test. Ready to use.
- `tests/test_games.py`: tests that send requests to your app and check each answer. You don't need to change this file.
- `requirements.txt`: the packages the app and the tests need (FastAPI and what it runs on, and pytest), at exact versions. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `main.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The app and the tests need FastAPI and pytest, and they go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it. It takes a minute: FastAPI brings several packages with it.

*Virtual Environments and pip* explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Run it

```bash
fastapi dev main.py
```

Then open `http://127.0.0.1:8000/docs` in your browser. The docs page lists every route the app has: none yet, until you add them. Click a route, then **Try it out** and **Execute**, to send it a real request. The app restarts each time you save a file. Stop it with **Ctrl+C**.

## Check your work

```bash
pytest
```

No server needs to be running: the tests hand each request straight to the app. At first every test fails: that is expected, because the router has no routes yet, so every request answers 404. Each route you finish turns its tests green. A failing test's message says what it sent, what it expected and what came back, for example *GET /games/4 should answer 200, but it answered 404 with {"detail":"Not Found"}*.

## The rules

- Write the routes in `routers/games.py`, on its `router`. Don't change `main.py`, `data.py` or the tests.
- The router's prefix is `/games` and its tag is `games`. The list's address is exactly `/games`, with no slash at the end.
- Read the games from `GAMES` in `data.py`, and add a new game to that same list with `GAMES.append()`.
- `players` and `max_minutes` are optional whole numbers: each filter is used only when the request sends it.
- A game suits a group when the group's size is between its `min_players` and `max_players`, both included. A game is quick enough when its `minutes` are `max_minutes` or fewer.
- A new game's body has four fields, `title`, `min_players`, `max_players` and `minutes`, all required. Its id is one more than the number of games on the shelf, and it's always `available`.

## Tips

- Start with the router: `APIRouter(prefix="/games", tags=["games"])`. Then `GET /games` with no filters, then add one filter at a time.
- A default of `None` makes a query parameter optional, and `is not None` tells you whether the request sent it.
- A type hint on a path or query parameter does the 422s for you: you don't write any code for `chess` or `four`.
- Raise `HTTPException` for the 404; returning it sends a 200.
- A small Pydantic model, `NewGame`, describes the body. `model_dump()` turns it into a dictionary you can add the id and `available` to.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
