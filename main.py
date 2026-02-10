from db.db import get_db
from services.Games import GamesService

db = get_db()
service = GamesService(db)

while True:
    print("===========CATALOGO DE GAMES============")
    print("1 - Cadastrar jogo")
    print("2 - Listar jogos")
    print("3 - Deletar jogo")
    print("0 - Sair")
    opcao = input("Escolha uma opcao: \n")

    if opcao == "1":
        linhadf = service.preencherFormulario()
        service.registrarGame(linhadf)
        service.atualizarDb()
    elif opcao == "2":
        service.listarGames()
    elif opcao == "3":
        service.deletarGame()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opcao invalida.")