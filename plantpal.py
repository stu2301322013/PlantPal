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
