import json
import pandas as pd

characters = {
    "characters": [
        {"name": "Lucas", "age": 22},
        {"name": "Nathan", "age": 18},
        {"name": "Haley", "age": 22},
        {"name": "Brooke", "age": 20},
        {"name": "Peyton", "age": 20}
    ]
}

with open("hw3.json", "w") as file:
    json.dump(characters, file, indent=4)
    
with open("hw3.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["characters"])
print("Favourite Characters DataFrame")
print(df)

oldest = df["age"].max()
oldest_characters = df[df["age"] == oldest]
print("\nOldest Character(s):")
print(oldest_characters)