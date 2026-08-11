"""
=========================================
 SAMTVS_BYVICTOR
 Biblioteca para TVs Samsung

 Desenvolvido por:
 Victor Fernando
=========================================
"""

import base64
import json


def encode_name(name: str) -> str:
    """
    Codifica o nome da conexão em Base64.
    """

    return base64.b64encode(
        name.encode("utf-8")
    ).decode("utf-8")


def decode_name(name: str) -> str:
    """
    Decodifica um nome em Base64.
    """

    return base64.b64decode(
        name
    ).decode("utf-8")


def pretty_json(data) -> str:
    """
    Formata um JSON para leitura.
    """

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )


def is_key(command: str) -> bool:
    """
    Verifica se é uma KEY_ válida.
    """

    return command.upper().startswith("KEY_")


def is_app(command: str) -> bool:
    """
    Verifica se é um APP.
    """

    return command.upper().startswith("APP_")


def clamp(value, minimum, maximum):
    """
    Limita um valor entre mínimo e máximo.
    """

    return max(minimum, min(value, maximum))


def chunks(lista, tamanho):
    """
    Divide uma lista em pedaços.
    """

    for i in range(0, len(lista), tamanho):
        yield lista[i:i + tamanho]
