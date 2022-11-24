from .models import Concurso, Jogo, Resultado, Sorteio, db


def criar_tabelas():
    tabelas = [Resultado, Sorteio, Jogo, Concurso]
    if db.connect():
        db.create_tables(tabelas)
