# Quickstart

Comece a usar o **SAMTVS BYVICTOR** rapidamente.

O SAMTVS BYVICTOR é uma biblioteca Python para controlar TVs Samsung com sistema Tizen através de WebSocket.

---

## Instalação

Instale pelo PyPI:

```bash
pip install samtvs-byvictor

Confira a instalação:

pip show samtvs-byvictor
Primeiro programa

Importe a biblioteca:

from samtvs_byvictor import SamsungTV

Crie uma conexão com sua TV:

tv = SamsungTV("192.168.1.100")

Troque 192.168.1.100 pelo IP da sua TV.

Conectando

Conecte na televisão:

tv.connect()

Na primeira conexão, a TV pode pedir autorização.

Aceite a solicitação usando o controle da televisão.

Enviando comandos

Depois de conectado, você pode controlar a TV.

Botão Home
tv.send_key("KEY_HOME")
Volume

Aumentar volume:

tv.volume_up()

Diminuir volume:

tv.volume_down()

Silenciar:

tv.volume_mute()
Energia

Liga/desliga a TV:

tv.power()
Exemplo completo
from samtvs_byvictor import SamsungTV

IP_DA_TV = "192.168.1.100"

tv = SamsungTV(IP_DA_TV)

tv.connect()

print("TV conectada!")

tv.send_key("KEY_HOME")

tv.volume_up()
Encontrando o IP da TV

Na televisão:

Configurações
→ Geral
→ Rede
→ Status da rede

Procure pelo endereço IP.

Exemplo:

192.168.1.50

Use esse endereço no código:

tv = SamsungTV("192.168.1.50")
Problemas comuns
A TV não conecta

Verifique:

A TV está ligada
Computador e TV estão na mesma rede
O IP está correto
A TV permite controle remoto pela rede
A TV pede autorização toda hora

Execute o programa novamente e aceite a permissão na tela da TV.

Erro de conexão

Teste se a TV responde na rede:

import socket

socket.gethostbyname("192.168.1.100")
Próximos passos

Confira:

API - api.md
Exemplos - /exampls
Changelog - n tem ou n achei
Links;

GitHub:

https://github.com/LightPPR2/SAMTVS_BYVICTOR

PyPI:

https://pypi.org/project/samtvs-byvictor/