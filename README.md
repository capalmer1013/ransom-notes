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
    game_id: "1234",

}
```
## PATCH /games/:id
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
    game_state: "awaiting",
    players: ["Walter Sobcheck"],
    prompt: "",

}
```

## GET /games/:id
long-poll current game

response:
```json
{
    players: [],
    prompt: "",

}
```

## POST /games/:id/cards
play card

response:
```json
{
    players: [],
    prompt: "",

}
```
## POST /games/:id/cards/winner
pick card

response:
```json
{
    players: [],
    prompt: "",

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