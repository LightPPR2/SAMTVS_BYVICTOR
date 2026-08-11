# SAMTVS BYVICTOR

Biblioteca Python para controlar **Samsung Smart TVs com Tizen** através da rede local usando WebSocket.

[![PyPI](https://img.shields.io/pypi/v/samtvs-byvictor)](https://pypi.org/project/samtvs-byvictor/)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)

## Recursos

* Conexão com Samsung TVs pela rede local
* Comunicação via WebSocket
* Descoberta automática de TVs
* Envio de comandos do controle remoto
* Controle de volume
* Controle de energia
* Abertura de aplicativos
* Envio de comandos Samsung personalizados
* API simples para projetos Python

## Requisitos

* Python 3.9 ou superior
* Samsung Smart TV compatível com Tizen
* Computador e TV na mesma rede local

## Instalação

Instale o SAMTVS BYVICTOR utilizando o `pip`:

```bash
pip install samtvs-byvictor
```

## Uso básico

Para conectar a uma Samsung Smart TV, informe o endereço IP da televisão:

```python
from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.send_key("KEY_HOME")
    tv.volume_up()

finally:
    tv.disconnect()
```

## Descoberta automática

O SAMTVS BYVICTOR também permite descobrir automaticamente uma TV compatível na rede:

```python
from samtvs_byvictor import SamsungTV

tv = SamsungTV.auto()

try:
    tv.connect()

    tv.send_key("KEY_HOME")

finally:
    tv.disconnect()
```

## Comandos

É possível enviar comandos do controle remoto para a televisão utilizando `send_key()`.

### Exemplos

```python
tv.send_key("KEY_HOME")
tv.send_key("KEY_RETURN")
tv.send_key("KEY_ENTER")
tv.send_key("KEY_PLAY")
tv.send_key("KEY_PAUSE")
```

### Controle de volume

```python
tv.volume_up()
tv.volume_down()
tv.volume_mute()
```

### Controle de energia

```python
tv.power()
```

## Abrindo aplicativos

Aplicativos podem ser abertos utilizando seu identificador:

```python
tv.open_app("ID_DO_APP")
```

### Exemplo

```python
tv.open_app("111299001912")
```

## Documentação

A documentação completa da biblioteca está disponível no site oficial:

[Documentação do SAMTVS BYVICTOR](https://lightppr2.github.io/SAMTVS_BYVICTOR/)

## Exemplo de automação

Um exemplo combinando diferentes comandos:

```python
from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.send_key("KEY_HOME")
    tv.volume_up()
    tv.open_app("111299001912")

finally:
    tv.disconnect()
```

## Compatibilidade

O SAMTVS BYVICTOR foi desenvolvido para **Samsung Smart TVs que utilizam Tizen** e permitem controle através da rede.

A disponibilidade de determinados comandos pode variar de acordo com:

* Modelo da televisão
* Versão do Tizen
* Firmware instalado

## Desenvolvimento

Clone o repositório:

```bash
git clone https://github.com/LightPPR2/SAMTVS_BYVICTOR.git
cd SAMTVS_BYVICTOR
```

Instale o projeto em modo de desenvolvimento:

```bash
pip install -e .
```

## Links

* **GitHub:** https://github.com/LightPPR2/SAMTVS_BYVICTOR
* **PyPI:** https://pypi.org/project/samtvs-byvictor/
* **Documentação:** https://lightppr2.github.io/SAMTVS_BYVICTOR/

## Licença

Consulte o repositório do projeto no GitHub para obter informações sobre a licença do SAMTVS BYVICTOR.
