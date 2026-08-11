Quickstart

Este guia mostra como conectar uma Samsung Smart TV ao Python usando o SAMTVS BYVICTOR e executar os primeiros comandos.

1. Instale a biblioteca

Instale pelo PyPI:

pip install samtvs-byvictor

2. Prepare a TV

Antes de executar o código, verifique se:

A TV está ligada.
A TV e o computador estão conectados à mesma rede local.
O controle remoto pela rede está permitido na TV.
3. Descubra o IP da TV

Na sua Samsung TV, procure as informações da rede.

O caminho pode variar de acordo com o modelo e a versão do Tizen. Normalmente, as informações podem ser encontradas em:

Configurações → Geral → Rede → Status da rede

Localize o endereço IP da televisão.

Exemplo:

192.168.1.50

4. Crie a conexão

Crie uma instância de SamsungTV usando o endereço IP da televisão:

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")


Substitua 192.168.1.50 pelo IP da sua TV.

5. Conecte à TV

Depois de criar a instância, conecte:

tv.connect()


Na primeira conexão, a TV pode exibir uma solicitação de autorização.

Use o controle remoto da TV para aceitar a conexão.

Depois que a conexão for autorizada, o computador poderá enviar comandos para a televisão.

6. Envie seu primeiro comando

Depois de conectar, você pode enviar comandos usando send_key().

Por exemplo, para abrir a tela inicial:

tv.send_key("KEY_HOME")

7. Controle o volume

A biblioteca possui métodos específicos para controle de volume:

tv.volume_up()


Aumenta o volume.

tv.volume_down()


Diminui o volume.

tv.volume_mute()


Alterna o estado de mudo.

8. Controle de energia

Para enviar o comando de energia:

tv.power()


O comportamento do comando de energia pode variar de acordo com o modelo da TV e seu estado atual.

9. Envie comandos Samsung diretamente

Também é possível enviar uma tecla Samsung diretamente:

tv.send_key("KEY_RETURN")


Outros exemplos:

tv.send_key("KEY_HOME")
tv.send_key("KEY_ENTER")
tv.send_key("KEY_PLAY")
tv.send_key("KEY_PAUSE")


Isso permite utilizar comandos que não possuem necessariamente um método específico na API.

10. Abra um aplicativo

Se o aplicativo for compatível com o método utilizado pela biblioteca, você pode abri-lo usando seu ID:

tv.open_app("ID_DO_APP")


Exemplo:

tv.open_app("111299001912")


O ID deve ser substituído pelo identificador do aplicativo que você deseja abrir.

11. Desconecte

Quando terminar de utilizar a TV:

tv.disconnect()


Isso encerra a conexão WebSocket.

Exemplo completo

Um programa simples pode ser escrito assim:

from samtvs_byvictor import SamsungTV

TV_IP = "192.168.1.50"

tv = SamsungTV(TV_IP)

try:
    tv.connect()

    print("TV conectada!")

    tv.send_key("KEY_HOME")
    tv.volume_up()

finally:
    tv.disconnect()


O try/finally garante que disconnect() seja chamado quando o programa terminar, inclusive se ocorrer um erro durante a execução.

Descoberta automática

Quando disponível na versão instalada da biblioteca, também é possível utilizar a descoberta automática:

from samtvs_byvictor import SamsungTV

tv = SamsungTV.auto()

tv.connect()

tv.send_key("KEY_HOME")

tv.disconnect()


Isso permite criar a instância sem informar manualmente o endereço IP.

Problemas de conexão
A TV não conecta

Verifique:

Se a TV está ligada.
Se o computador e a TV estão na mesma rede.
Se o endereço IP está correto.
Se o controle remoto pela rede está permitido.
Se a TV exibiu uma solicitação de autorização.
Se o firewall ou a configuração da rede não está bloqueando a comunicação.
A TV pede autorização novamente

Na primeira conexão, a TV pode solicitar autorização para o dispositivo.

Aceite a solicitação usando o controle remoto.

Se a autorização continuar sendo solicitada, verifique as configurações de controle remoto e rede da TV.

Próximos passos

Depois de concluir este guia, consulte:

API Reference — métodos e recursos disponíveis.
Exemplos — exemplos de utilização.
Changelog — histórico de versões.