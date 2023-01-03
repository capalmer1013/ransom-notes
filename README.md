# Ransom notes
ransom notes game backend

cli frontend

# game states
- pre-game
- awaiting responses
- judges selection
# api

actions
- create game
- join game
- start game
- poll current game
- play card
- pick card

## POST /games
create game

request:
```json
{
    "player_name": "Don Johnson",
}
```

response:
```json
{
    "game_id": "1234",
    "player_id": "3456",
}
```
## POST /games/:id/players
join game

request:
```json
{
    "player_name": "Don Johnson",
}
```
response:
```json
{
    "player_id": "4567",
    "game_state": "pregame",
    "players": ["Walter Sobcheck", "Don Johnson"],
    "prompt": "Setup here",
    "responses": ["punchline here"]
}
```

## GET /games/:id?player_id=4567
long-poll current game
- player_id will return available words for that player
- player_id acts as kinda auth prevent directly sharing all words with everyone


response:
```json
{
    "game_state": "selection",
    "players": ["Walter Sobcheck", "Don Johnson", "Ricky Bobby"],
    "prompt": "Setup here",
    "responses": ["punchline here"],
    "words": ["this", "is", "full", "of", "words"]
}
```

## POST /games/:id/cards
play card

request:
```json
{
    "response": "punchline here",
}
```
response:
```json
{
    "responses": ["punchline here"],
}
```
## POST /games/:id/cards/winner
pick card

request:
```json
{
    "response": "punchline here",
}
```
response:
```json
{
    "players": [],
    "prompt": "",
}
```

# Setup
**Python setup**
install python
`wget  https://bootstrap.pypa.io/get-pip.py`
`python3 get-pip.py`
`python3 -m pip install pipenv`

**App setup**
`pipenv install`
`cp .env.example .env`
*update env variables*
`make db-upgrade`
`make local-server`