Exemplos

Exemplos práticos de utilização do SAMTVS BYVICTOR.

Conexão básica

O exemplo mais simples cria uma instância da TV, conecta, envia um comando e encerra a conexão:

from samtvs_byvictor import SamsungTV

TV_IP = "192.168.1.50"

tv = SamsungTV(TV_IP)

try:
    tv.connect()

    print("TV conectada!")

    tv.send_key("KEY_HOME")

finally:
    tv.disconnect()


Substitua 192.168.1.50 pelo endereço IP da sua TV.

Controle de volume

É possível controlar o volume usando os métodos fornecidos pela biblioteca:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.volume_up()
    tv.volume_up()

    tv.volume_down()

    tv.volume_mute()

finally:
    tv.disconnect()

Comandos do controle remoto

O método send_key() permite enviar comandos diretamente:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.send_key("KEY_HOME")
    tv.send_key("KEY_RETURN")
    tv.send_key("KEY_ENTER")
    tv.send_key("KEY_PLAY")
    tv.send_key("KEY_PAUSE")

finally:
    tv.disconnect()


Isso é útil quando você deseja enviar um comando específico que não possui um método próprio na API.

Controle de energia
from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.power()

finally:
    tv.disconnect()


O comportamento do comando pode variar de acordo com o modelo e o estado atual da TV.

Abrindo um aplicativo

Para abrir um aplicativo compatível, utilize seu ID:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.open_app("111299001912")

finally:
    tv.disconnect()


Substitua o ID pelo identificador do aplicativo desejado.

Descoberta automática

Quando você não quiser informar manualmente o IP da TV, pode utilizar a descoberta automática:

from samtvs_byvictor import SamsungTV

tv = SamsungTV.auto()

try:
    tv.connect()

    tv.send_key("KEY_HOME")

finally:
    tv.disconnect()


Isso permite que a biblioteca procure uma TV disponível na rede local.

Controle usando uma função

Se você pretende criar uma aplicação maior, pode encapsular a conexão em funções:

from samtvs_byvictor import SamsungTV


def abrir_home(ip):
    tv = SamsungTV(ip)

    try:
        tv.connect()
        tv.send_key("KEY_HOME")

    finally:
        tv.disconnect()


abrir_home("192.168.1.50")

Controle por menu

Você também pode criar um pequeno controle remoto no terminal:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    while True:
        command = input("Comando (home/up/down/volume+/volume-/mute/exit): ")

        if command == "home":
            tv.send_key("KEY_HOME")

        elif command == "up":
            tv.send_key("KEY_UP")

        elif command == "down":
            tv.send_key("KEY_DOWN")

        elif command == "volume+":
            tv.volume_up()

        elif command == "volume-":
            tv.volume_down()

        elif command == "mute":
            tv.volume_mute()

        elif command == "exit":
            break

        else:
            print("Comando desconhecido.")

finally:
    tv.disconnect()


Esse exemplo mostra como a biblioteca pode ser utilizada como base para construir um controle remoto personalizado.

Automação

A biblioteca também pode ser utilizada em projetos de automação.

Por exemplo, uma função pode executar uma sequência de comandos:

from samtvs_byvictor import SamsungTV


def configurar_tv(ip):
    tv = SamsungTV(ip)

    try:
        tv.connect()

        tv.send_key("KEY_HOME")
        tv.volume_down()
        tv.volume_down()
        tv.volume_up()

    finally:
        tv.disconnect()


configurar_tv("192.168.1.50")

Integração com outros projetos

Como o SAMTVS BYVICTOR é uma biblioteca Python, ele pode ser utilizado junto com outras bibliotecas e projetos.

Por exemplo, uma aplicação pode receber um comando de outra fonte e transformá-lo em uma ação na TV:

from samtvs_byvictor import SamsungTV


def executar_comando(tv, comando):
    if comando == "home":
        tv.send_key("KEY_HOME")

    elif comando == "volume_up":
        tv.volume_up()

    elif comando == "volume_down":
        tv.volume_down()

    elif comando == "mute":
        tv.volume_mute()

    elif comando == "power":
        tv.power()


tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    executar_comando(tv, "home")
    executar_comando(tv, "volume_up")

finally:
    tv.disconnect()


Essa estrutura pode ser adaptada para interfaces gráficas, bots, servidores, automações residenciais, Arduino, Raspberry Pi e outros projetos Python.

Mantendo a conexão

Quando vários comandos serão enviados em sequência, é preferível estabelecer uma conexão e reutilizá-la:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.send_key("KEY_HOME")
    tv.volume_up()
    tv.volume_up()
    tv.send_key("KEY_RETURN")
    tv.volume_down()

finally:
    tv.disconnect()


Isso evita criar uma nova conexão para cada comando.

Tratamento básico de erros

Ao trabalhar com dispositivos de rede, é recomendado tratar possíveis erros de conexão:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.send_key("KEY_HOME")

except Exception as error:
    print(f"Erro ao controlar a TV: {error}")

finally:
    tv.disconnect()


Para aplicações maiores, recomenda-se tratar especificamente as exceções fornecidas pela biblioteca quando aplicável.

Próximos passos

Depois de testar os exemplos, consulte:

Quickstart para começar rapidamente.
API Reference para conhecer os métodos disponíveis.
Changelog para acompanhar novas versões.