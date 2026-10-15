import json
import os

DATA_FILE = "plants.json"


def load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save(plants):
    with open(DATA_FILE, "w") as f:
        json.dump(plants, f, indent=2)


def new_plant(name, species=""):
    return {"id": 0, "name": name, "species": species, "photo": None,
            "every_days": None, "last_watered": None}


def cmd_add(name, species=""):
    plants = load()
    plant = new_plant(name, species)
    plant["id"] = max([p["id"] for p in plants], default=0) + 1
    plants.append(plant)
    save(plants)
    plants.append(plant)
    save(plants)
    print("added", plant["name"])


def cmd_list():
    for p in load():
        print(p["id"], p["name"], p["species"])


def cmd_edit(plant_id, name):
    plants = load()
    for p in plants:
        if p["id"] == int(plant_id):
            p["name"] = name
    save(plants)


def cmd_delete(plant_id):
    save([p for p in load() if p["id"] != int(plant_id)])


def cmd_search(text):
    for p in load():
        if text.lower() in p["name"].lower():
            print(p["id"], p["name"])


def cmd_photo(plant_id, path):
    plants = load()
    for p in plants:
        if p["id"] == int(plant_id):
            p["photo"] = path
    save(plants)


def cmd_schedule(plant_id, every_days):
    plants = load()
    for p in plants:
        if p["id"] == int(plant_id):
            p["every_days"] = int(every_days)
    save(plants)
