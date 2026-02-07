from db.db import get_db
from schemas.GameSchema import GameSchema
from services.Games import GamesService
import pandas as pd

db = get_db()
service = GamesService(db)

linhadf = service.preencherFormulario()
service.registrarGame(linhadf)
service.atualizarDb()