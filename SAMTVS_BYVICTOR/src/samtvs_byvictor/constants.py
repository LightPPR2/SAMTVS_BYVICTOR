"""
=========================================
 SAMTVS_BYVICTOR
 Biblioteca para TVs Samsung

 Desenvolvido por:
 Victor Fernando
=========================================
"""

# Porta padrão do WebSocket
DEFAULT_PORT = 8002

# Porta HTTP (algumas APIs)
DEFAULT_HTTP_PORT = 8001

# Caminho do WebSocket
WS_PATH = "/api/v2/channels/samsung.remote.control"

# Nome padrão da conexão
DEFAULT_NAME = "Python"

# Arquivo padrão do token
DEFAULT_TOKEN_FILE = "tv_token.txt"

# Intervalo do keep-alive (segundos)
KEEP_ALIVE_INTERVAL = 0.5

# Timeout da conexão
CONNECT_TIMEOUT = 5

# SSL
SSL_OPTIONS = {
    "cert_reqs": 0
}

# Key usada para manter a conexão ativa
KEEP_ALIVE_KEY = "KEY_PANNEL_CHDOWN"

# URLs

HTTP_URL = "http://{ip}:{port}"

WS_URL = (
    "wss://{ip}:{port}"
    "/api/v2/channels/"
    "samsung.remote.control"
    "?name={name}"
)

TOKEN_URL = (
    "wss://{ip}:{port}"
    "/api/v2/channels/"
    "samsung.remote.control"
    "?name={name}&token={token}"
)