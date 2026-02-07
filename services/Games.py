from schemas.GameSchema import GameSchema
import pandas as pd

class GamesService():
    def __init__(self, db):
        self.db = db

    def preencherFormulario(self):
        print("===========CADASTRO DE JOGO============ \n")

        FormularioJogo = GameSchema(
            input("Insira o nome do jogo: \n"),
            input("Insira os generos do jogo (Separe por ','): \n"),
            input("Insira as tags do jogo (Separe por ','): \n"),
            input("Insira o preco do jogo : \n"),
            input("O jogo está disponivel em Portugues? (true/false) : \n")
        )
        linhadf = pd.DataFrame(FormularioJogo.__dict__)

        return linhadf

    def registrarGame(self,game):
        maiorid = self.db["id"].max()
        if pd.isnull(maiorid):
            maiorid = 0
        game["id"] = maiorid + 1
        self.db = pd.concat([self.db,game], ignore_index=True)
        print(self.db)

    def atualizarDb(self):
        self.db.to_csv("./db/games_cadastrados.csv", index=False)


