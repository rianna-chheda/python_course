import json

data = {
    "course": "Python:",
    "students":[
        {"name": "Rianna", "age": 16, "city": "Mumbai"},
        {"name": "Priya", "age": 15, "city": "Mumbai"},
        {"name": "Anya", "age": 17, "city": "Delhi"}
    ]
}
with open ('data.json', 'w') as file:
    json.dump(data, file, indent=4)
    
with open('data.json', 'r') as file:
    loaded = json.load(file)

print(loaded['course'])
print(loaded['students'][0]['name'])