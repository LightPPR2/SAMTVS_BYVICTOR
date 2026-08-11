SAMTVS BYVICTOR

SAMTVS BYVICTOR é uma biblioteca Python para controlar TVs Samsung com sistema Tizen através da rede local usando WebSocket.

Com ela, você pode conectar a uma Samsung TV e enviar comandos como controle remoto, controlar o volume, abrir aplicativos e utilizar outros recursos disponíveis pela biblioteca.

Recursos
Conexão com Samsung TVs pela rede local
Comunicação através de WebSocket
Descoberta automática de TVs
Envio de comandos do controle remoto
Controle de volume
Controle de energia
Abertura de aplicativos
Envio de comandos Samsung personalizados
API Python simples
Instalação

Instale a versão mais recente diretamente pelo PyPI:

pip install samtvs-byvictor

Primeiro exemplo
from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.100")

tv.connect()

tv.send_key("KEY_HOME")
tv.volume_up()

tv.disconnect()


Substitua 192.168.1.100 pelo endereço IP da sua TV.

Na primeira conexão, a televisão pode solicitar autorização para o dispositivo. Nesse caso, aceite a solicitação usando o controle remoto da TV.

Documentação
Instalação
Quickstart
API Reference
Exemplos
Changelog
Requisitos

Antes de utilizar a biblioteca, certifique-se de que:

Você possui Python 3.9 ou superior.
Sua televisão é uma Samsung Smart TV compatível com Tizen.
O computador e a TV estão conectados à mesma rede local.
O controle remoto pela rede está permitido na televisão.
Projeto

O código-fonte do projeto está disponível no GitHub:

https://github.com/LightPPR2/SAMTVS_BYVICTOR

A biblioteca também está disponível no PyPI:

https://pypi.org/project/samtvs-byvictor/

Licença

Consulte o arquivo LICENSE do projeto para obter informações sobre a licença.