from peewee import (
    CharField,
    DateField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
)

db = SqliteDatabase("confereaposta.db")


class Concurso(Model):
    numero = IntegerField(unique=True, index=True)
    data = DateField()

    class Meta:
        database = db


class Sorteio(Model):
    concurso = ForeignKeyField(Concurso)
    primeira_dezena = CharField()
    segunda_dezena = CharField()
    terceira_dezena = CharField()
    quarta_dezena = CharField()
    quinta_dezena = CharField()
    sexta_dezena = CharField()

    class Meta:
        database = db


class Jogo(Model):
    numeros = CharField()
    concurso = ForeignKeyField(Concurso)

    class Meta:
        database = db


class Resultado(Model):
    jogo = ForeignKeyField(Jogo)
    sorteio = ForeignKeyField(Sorteio)
    data_hora_conferencia = DateTimeField()
    quantidade_acertos = IntegerField()
    numeros_acertados = CharField()

    class Meta:
        database = db
