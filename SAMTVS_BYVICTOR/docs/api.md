API Reference

Referência da API pública do SAMTVS BYVICTOR.

O SAMTVS BYVICTOR fornece uma API Python para controlar TVs Samsung Tizen através da rede local.

Importação

A classe principal pode ser importada diretamente do pacote:

from samtvs_byvictor import SamsungTV

SamsungTV

Classe principal utilizada para criar e controlar uma conexão com uma Samsung TV.

Criando uma instância

Para conectar diretamente a uma TV pelo endereço IP:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

Parâmetros
Parâmetro	Tipo	Descrição
ip	str	Endereço IP da Samsung TV

Exemplo:

tv = SamsungTV("192.168.1.50")

auto()

Tenta descobrir automaticamente uma Samsung TV disponível na rede local.

tv = SamsungTV.auto()


Depois da descoberta, a instância pode ser conectada normalmente:

tv = SamsungTV.auto()

tv.connect()


A descoberta automática é útil quando você não deseja informar manualmente o endereço IP da TV.

Conexão
connect()

Estabelece a conexão com a televisão.

tv.connect()


Exemplo:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

tv.connect()

print("TV conectada!")


Na primeira conexão, a televisão pode solicitar autorização para o dispositivo.

Aceite a solicitação usando o controle remoto da TV.

disconnect()

Encerra a conexão com a televisão.

tv.disconnect()


É recomendado desconectar quando a aplicação terminar de utilizar a TV.

Exemplo:

tv.connect()

tv.send_key("KEY_HOME")

tv.disconnect()

Comandos do controle remoto
send_key()

Envia diretamente uma tecla para a televisão.

tv.send_key("KEY_HOME")


O método permite utilizar comandos Samsung diretamente, sem precisar de um método específico para cada tecla.

Exemplos

Abrir a tela inicial:

tv.send_key("KEY_HOME")


Voltar:

tv.send_key("KEY_RETURN")


Confirmar:

tv.send_key("KEY_ENTER")


Reproduzir:

tv.send_key("KEY_PLAY")


Pausar:

tv.send_key("KEY_PAUSE")

Parâmetros
Parâmetro	Tipo	Descrição
key	str	Nome do comando enviado à TV

Exemplo:

tv.send_key("KEY_VOLUMEUP")


Os comandos aceitos dependem dos comandos disponíveis no sistema da Samsung TV.

Volume
volume_up()

Aumenta o volume da televisão.

tv.volume_up()

volume_down()

Diminui o volume da televisão.

tv.volume_down()

volume_mute()

Alterna o estado de mudo da televisão.

tv.volume_mute()

Energia
power()

Envia o comando de energia para a televisão.

tv.power()


O comportamento desse comando pode depender do modelo da TV e do estado atual da televisão.

Aplicativos
open_app()

Abre um aplicativo usando seu identificador.

tv.open_app("ID_DO_APP")

Parâmetros
Parâmetro	Tipo	Descrição
app_id	str	Identificador do aplicativo

Exemplo:

tv.open_app("111299001912")


O ID utilizado deve corresponder a um aplicativo compatível com o método de abertura utilizado pela televisão.

Exemplo de utilização

Um exemplo básico utilizando vários recursos:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.send_key("KEY_HOME")

    tv.volume_up()
    tv.volume_down()

    tv.send_key("KEY_RETURN")

finally:
    tv.disconnect()

Exemplo usando descoberta automática
from samtvs_byvictor import SamsungTV

tv = SamsungTV.auto()

try:
    tv.connect()

    tv.send_key("KEY_HOME")
    tv.volume_up()

finally:
    tv.disconnect()

Fluxo recomendado

Uma utilização típica da biblioteca segue este fluxo:

Criar SamsungTV
       ↓
   connect()
       ↓
Enviar comandos
       ↓
   disconnect()


Exemplo:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

try:
    tv.connect()

    tv.send_key("KEY_HOME")
    tv.volume_up()

finally:
    tv.disconnect()

Compatibilidade

O SAMTVS BYVICTOR foi desenvolvido para comunicação com Samsung Smart TVs que utilizam Tizen e disponibilizam controle pela rede.

O comportamento e a disponibilidade de determinados comandos podem variar de acordo com:

Modelo da televisão
Versão do Tizen
Configurações da TV
Aplicativo utilizado
Comandos suportados pelo firmware
Observação sobre a API

A API pública pode receber novos métodos e recursos em versões futuras.

Para acompanhar alterações, consulte o Changelog.