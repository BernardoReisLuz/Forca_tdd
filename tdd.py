import pytest
from Forca import PalavraSecreta


def test_palavra_convertida_para_maiuscula():
    palavra = PalavraSecreta("casa")

    assert palavra.palavra == "CASA"


def test_remove_espacos_extras():
    palavra = PalavraSecreta("   banana   ")

    assert palavra.palavra == "BANANA"


def test_palavra_com_numeros_gera_erro():
    with pytest.raises(ValueError):
        PalavraSecreta("CASA123")


def test_palavra_com_simbolos_gera_erro():
    with pytest.raises(ValueError):
        PalavraSecreta("CA$A")


def test_letra_correta_retorna_true():
    palavra = PalavraSecreta("CASA")

    resultado = palavra.tentar_letra("A")

    assert resultado is True


def test_letra_incorreta_retorna_false():
    palavra = PalavraSecreta("CASA")

    resultado = palavra.tentar_letra("X")

    assert resultado is False


def test_letras_corretas_aparecem_no_progresso():
    palavra = PalavraSecreta("CASA")

    palavra.tentar_letra("A")

    assert palavra.exibir_progresso() == "_ A _ A"


def test_letras_nao_descobertas_aparecem_com_sublinhado():
    palavra = PalavraSecreta("CASA")

    assert palavra.exibir_progresso() == "_ _ _ _"


def test_palavra_so_e_descoberta_quando_todas_as_letras_forem_reveladas():
    palavra = PalavraSecreta("CASA")

    palavra.tentar_letra("C")
    palavra.tentar_letra("A")

    assert palavra.foi_descoberta() is False

    palavra.tentar_letra("S")

    assert palavra.foi_descoberta() is True


def test_primeira_letra_revelada_quando_ativado():
    palavra = PalavraSecreta("CASA", revelar_primeira_letra=True)

    assert palavra.exibir_progresso() == "C _ _ _"


