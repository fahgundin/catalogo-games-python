

class GameSchema:
    nome:str
    genero: list[str]
    tags: list[str]
    preco: float
    disponivelEmPortugues: bool

    def __init__ (
        self,
        nome: str,
        genero: str,
        tags: str,
        preco: float,
        disponivelEmPortugues: bool):
            
            self.nome = nome
            self.genero = [g for g in genero.split(',')]
            self.tags = [t for t in tags.split(',')]
            self.preco = preco
            self.disponivelEmPortugues = disponivelEmPortugues