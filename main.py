from db.db import get_db
from services.Games import GamesService

db = get_db()
service = GamesService(db)

linhadf = service.preencherFormulario()
service.registrarGame(linhadf)
service.atualizarDb()