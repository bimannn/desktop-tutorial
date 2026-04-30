import json
import os

# Загрузка JSON или возврат стандартных значений
def load_data(filename, default):
    if not os.path.exists(filename):
        return default
    with open(filename, "r") as f:
        return json.load(f)

# Сохранение данных
def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def update_leaderboard(name, score, distance):
    lb = load_data("leaderboard.json", [])
    lb.append({"name": name, "score": int(score), "distance": int(distance)})
    lb = sorted(lb, key=lambda x: x["score"], reverse=True)[:10]
    save_data("leaderboard.json", lb)