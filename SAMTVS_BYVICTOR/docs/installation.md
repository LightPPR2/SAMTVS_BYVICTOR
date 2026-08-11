# Getting Started

Guia inicial para começar a usar o **SAMTVS BYVICTOR**.

Esta biblioteca permite controlar TVs Samsung Tizen através de Python usando comunicação WebSocket.

---

# Instalação

Instale a biblioteca usando o pip:

```bash
pip install samtvs-byvictor

Após instalar, importe a biblioteca:

from samtvs_byvictor import SamsungTV

Preparando a TV

Antes de usar:

A TV deve estar ligada.
A TV e o computador precisam estar na mesma rede.
O controle remoto pela rede deve estar permitido.
Encontrando o IP da TV

Na sua TV Samsung:

Configurações
→ Geral
→ Rede
→ Status da rede

Procure pelo endereço IP.

Exemplo:

192.168.1.50
Criando a conexão

Crie uma instância da TV:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")

Substitua o IP pelo endereço da sua televisão.

Conectando

Conecte usando:

tv.connect()

Na primeira conexão:

Execute o programa.
Olhe a tela da TV.
Aceite a solicitação de controle remoto.
Primeiro comando

Depois de conectado:

tv.send_key("KEY_HOME")

A tela inicial da TV será aberta.

Controle de volume

Aumentar volume:

tv.volume_up()

Diminuir volume:

tv.volume_down()

Silenciar:

tv.volume_mute()

Exemplo completo
from samtvs_byvictor import SamsungTV

IP_DA_TV = "192.168.1.50"

tv = SamsungTV(IP_DA_TV)

try:
    tv.connect()

    print("TV conectada!")

    tv.send_key("KEY_HOME")

    tv.volume_up()

finally:
    tv.disconnect()
Enviando comandos personalizados

A biblioteca permite enviar comandos Samsung diretamente:

tv.send_key("KEY_COMANDO")

Exemplos:

tv.send_key("KEY_RETURN")

tv.send_key("KEY_ENTER")

tv.send_key("KEY_PLAY")

tv.send_key("KEY_PAUSE")
Abrindo aplicativos

Caso o aplicativo seja compatível:

tv.open_app("ID_DO_APP")

Exemplo:

tv.open_app("111299001912")
Desconectando

Quando terminar:

tv.disconnect()

Isso encerra a conexão com a televisão.
