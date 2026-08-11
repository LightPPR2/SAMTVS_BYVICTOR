Instalação
Requisitos

Antes de instalar o SAMTVS BYVICTOR, certifique-se de que você possui:

Python 3.9 ou superior
Uma Samsung Smart TV compatível com Tizen
Computador e TV conectados à mesma rede local
Instalação pelo PyPI

A forma recomendada de instalar a biblioteca é através do pip:

pip install samtvs-byvictor


Para atualizar para a versão mais recente:

pip install --upgrade samtvs-byvictor

Verificando a instalação

Depois da instalação, abra o Python:

python


E execute:

import samtvs_byvictor

print("SAMTVS BYVICTOR instalado com sucesso!")


Se não ocorrer nenhum erro, a biblioteca foi instalada corretamente.

Também é possível verificar a versão instalada usando:

pip show samtvs-byvictor

Instalação a partir do código-fonte

Para instalar a versão disponível no repositório do GitHub, primeiro clone o projeto:

git clone https://github.com/LightPPR2/SAMTVS_BYVICTOR.git


Entre na pasta do projeto:

cd SAMTVS_BYVICTOR


Depois instale a biblioteca:

pip install .


Para instalar em modo editável, útil durante o desenvolvimento:

pip install -e .


Nesse modo, alterações feitas no código-fonte ficam disponíveis sem precisar reinstalar o pacote a cada mudança.

Dependências

O SAMTVS BYVICTOR utiliza as seguintes dependências principais:

websocket-client
requests

Elas são instaladas automaticamente pelo pip ao instalar o pacote.

Não é necessário instalar essas dependências manualmente em uma instalação normal.

Ambiente virtual

É recomendado utilizar um ambiente virtual para evitar conflitos entre dependências de diferentes projetos.

No Windows:

python -m venv .venv


Ative o ambiente:

.venv\Scripts\activate


Depois instale a biblioteca:

pip install samtvs-byvictor


Para sair do ambiente virtual:

deactivate

Próximos passos

Depois de instalar a biblioteca, consulte o Quickstart para realizar a primeira conexão com uma Samsung TV.

Para consultar os métodos disponíveis, veja a API Reference.

Para exemplos de automação e utilização, consulte Exemplos.