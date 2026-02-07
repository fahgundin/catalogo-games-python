
import pandas as pd

from schemas.GameSchema import GameSchema


def get_db():
    try:
        db = pd.read_csv("./db/games_cadastrados.csv")
    except FileNotFoundError:
        dict = {}
        colunasNome = GameSchema.__annotations__.keys()
        dict["id"] = []
        for col in colunasNome:
            dict[col] = []
        df = pd.DataFrame(dict)
        df.to_csv("./db/games_cadastrados.csv", index=False)
        db = df
    return db

def updateDb(db):
    db.to_csv("./db/games_cadastrados.csv", index=False)