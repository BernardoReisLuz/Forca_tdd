import os
import random
from typing import List, Set

class PalavraSecreta:
    """
    Classe responsável por armazenar a palavra secreta e controlar as letras
    descobertas pelo jogador.
    """

    def __init__(self, palavra: str, revelar_primeira_letra: bool = False) -> None:
        # Remove espaços extras e converte para maiúsculas
        palavra = palavra.strip().upper()

        # Valida se contém apenas letras
        if not palavra.isalpha():
            raise ValueError("A palavra deve conter apenas letras.")

        self._palavra = palavra
        self._letras_descobertas = set()

        # Revela a primeira letra, se solicitado
        if revelar_primeira_letra:
            self._letras_descobertas.add(self._palavra[0])

    @property
    def palavra(self) -> str:
        # Retorna a palavra secreta completa
        return self._palavra

    def tentar_letra(self, letra: str) -> bool:
        # Normaliza a letra para maiúscula
        letra = letra.strip().upper()

        # Valida entrada
        if len(letra) != 1 or not letra.isalpha():
            raise ValueError("Digite apenas uma letra.")

        # Verifica se a letra existe na palavra
        if letra in self._palavra:
            self._letras_descobertas.add(letra)
            return True

        return False

    def exibir_progresso(self) -> str:
        # Exibe letras descobertas e "_" para ocultas
        progresso = []

        for letra in self._palavra:
            if letra in self._letras_descobertas:
                progresso.append(letra)
            else:
                progresso.append("_")

        return " ".join(progresso)

    def foi_descoberta(self) -> bool:
        # Retorna True se todas as letras foram descobertas
        for letra in self._palavra:
            if letra not in self._letras_descobertas:
                return False

        return True
    
