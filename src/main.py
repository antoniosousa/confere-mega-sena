import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def fecha_site(web_driver) -> None:
    web_driver.close()


def abre_site() -> WebDriver:
    driver: WebDriver = WebDriver()
    driver.get("https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx")
    return driver


def seleciona_concurso(concurso, web_driver) -> str:
    time.sleep(4)
    elemento = web_driver.find_element(By.ID, "buscaConcurso")
    elemento.clear()
    elemento.send_keys(f"{concurso}")
    elemento.send_keys(Keys.RETURN)
    resultado: str = web_driver.find_element(By.ID, "ulDezenas").text
    return resultado


def busca_resultado(concursos: list[int], web_driver) -> dict[int, str]:
    resultado_dezenas: dict[int, str] = {}
    for concurso in concursos:
        resultado: str = seleciona_concurso(concurso, web_driver)
        if concurso not in list(resultado_dezenas):
            resultado_dezenas[concurso] = resultado
    return resultado_dezenas


def captura_resultado_no_site(concursos: list[int]) -> dict[int, str]:
    web_driver: WebDriver = abre_site()
    resultado_dezenas: dict[int, str] = busca_resultado(concursos, web_driver)
    fecha_site(web_driver)
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
                if len(acertos) > 3:
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
