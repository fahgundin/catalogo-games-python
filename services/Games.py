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
        linhadf = pd.DataFrame([FormularioJogo.__dict__])

        return linhadf

    def registrarGame(self,game):
        maiorid = self.db["id"].max()
        if pd.isnull(maiorid):
            maiorid = 0
        game["id"] = maiorid + 1
        self.db = pd.concat([self.db,game], ignore_index=True)
        print(self.db)

    def listarGames(self):
        if self.db.empty:
            print("Nenhum jogo cadastrado.")
            return
        print("===========JOGOS CADASTRADOS============ \n")
        print(self.db.to_string(index=False))
        print()

    def deletarGame(self):
        print("===========DELETAR JOGO============ \n")
        cod = int(input("Insira o código do jogo que deseja excluir (um numero inteiro sem ponto): \n"))
        game = self.db[self.db["id"] == cod]
        if game.empty:
            print(f"Jogo com código {cod} não encontrado.")
            return
        self.db = self.db[self.db["id"] != cod].reset_index(drop=True)
        self.atualizarDb()
        print(f"Jogo com código {cod} removido com sucesso.")

    def atualizarDb(self):
        self.db.to_csv("./db/games_cadastrados.csv", index=False)


