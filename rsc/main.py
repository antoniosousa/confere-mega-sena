import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def captura_resultado_no_site(concursos: list[int]) -> dict[int, str]:
    resultado_dezenas: dict[int, str] = {}
    driver = webdriver.Chrome()
    driver.get("https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx")
    elem = driver.find_element(By.ID, "buscaConcurso")
    for concurso in concursos:
        elem.clear()
        elem.send_keys(f"{concurso}")
        elem.send_keys(Keys.RETURN)
        time.sleep(4)
        resultado: str = driver.find_element(By.ID, "ulDezenas").text
        if concurso not in list(resultado_dezenas):
            resultado_dezenas[concurso] = resultado
    driver.close()
    return resultado_dezenas


def string_para_lista(strings: str) -> list[str]:
    return [
        strings[:2],
        strings[2:4],
        strings[4:6],
        strings[6:8],
        strings[8:10],
        strings[10:12],
    ]


def conferir(resultado: dict[int, str], jogos: list[str]) -> None:
    for jogo in jogos:
        jogo_normalizado: list[str] = string_para_lista(jogo)
        for con in resultado:
            result: str | None = resultado.get(con)
            if result:
                resultado_normalizado: list[str] = string_para_lista(result)
                acertos: set[str] = set(jogo_normalizado).intersection(
                    set(resultado_normalizado)
                )
                if len(acertos) > 0:
                    print("Acertos:", len(acertos))
                    print("Concurso:", con)
                    print("Números:", acertos)
                    print()


if __name__ == "__main__":
    mensagem_concurso: str = """\
    Quais os concursos a serem verificados?
    Se for mais de um pode digitar o interval: 2536 2543

    """
    mensagem_jogo: str = """\
    Quais os jogos feitos?
    Se for mais de um pode digitar o interval: 010408071413 a 090805030407

    """
    concursos: list[str] = input(mensagem_concurso).split(" ")
    concursos.sort()
    jogos: list[str] = input(mensagem_jogo).split(" ")
    if not isinstance(jogos, list):
        jogos = [jogos]
    con: list[int] = list(range(int(concursos[0]), int(concursos[-1]) + 1))
    resultados: dict[int, str] = captura_resultado_no_site(con)
    conferir(resultados, jogos)
