import json


games = {
    "favourite_games":[
        {"name": "UNO", "genre": "card game", "goal": "have 1 card left"},
        {"name": "Monopoly", "genre": "board game", "goal": "be the last player standing"},
        {"name": "Battle Ship", "genre": "board game", "goal": "kill other ships"}
    ]
}
with open ('games.json', 'w') as file:
    json.dump(games, file, indent=4)
with open('games.json', 'r') as file:
    loaded = json.load(file)

print(f"My first favourite game is {loaded['favourite_games'][0]['name']}")
print(f"My second favourite game is {loaded['favourite_games'][1]['name']}")
print(f"My third favourite game is {loaded['favourite_games'][2]['name']}")
print(f"I have {len(loaded['favourite_games'])} favourite games.")