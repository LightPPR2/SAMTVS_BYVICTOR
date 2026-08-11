"""
Classe principal da SAMTVS_BYVICTOR
"""

from .auth import AuthManager
from .commands import CommandSender
from .keepalive import KeepAlive


class SamsungTV:

    def __init__(
        self,
        ip,
        name="Python",
        port=8002,
        token_file="tv_token.txt",
        auto_reconnect=True,
        keep_alive=True,
    ):

        self.ip = ip
        self.port = port
        self.name = name

        self.auto_reconnect = auto_reconnect
        self.keep_alive_enabled = keep_alive

        self.auth = AuthManager(
            ip=ip,
            port=port,
            name=name,
            token_file=token_file,
        )

        self.sender = CommandSender(self.auth)
        self.keepalive = KeepAlive(self)

    # ==========================
    # Conexão
    # ==========================

    def connect(self):
        self.auth.connect()

        if self.keep_alive_enabled:
            self.keepalive.start()

        return self

    def disconnect(self):
        self.keepalive.stop()
        self.auth.disconnect()

    @property
    def connected(self):
        return self.auth.connected

    # ==========================
    # Comandos
    # ==========================

    def key(self, key):
        self.sender.key(key)

    def app(self, appid):
        self.sender.app(appid)

    # ==========================
    # Atalhos
    # ==========================

    def power(self):
        self.key("KEY_POWER")

    def home(self):
        self.key("KEY_HOME")

    def back(self):
        self.key("KEY_RETURN")

    def enter(self):
        self.key("KEY_ENTER")

    def volume_up(self):
        self.key("KEY_VOLUP")

    def volume_down(self):
        self.key("KEY_VOLDOWN")

    def mute(self):
        self.key("KEY_MUTE")

    # ==========================
    # Apps
    # ==========================

    def youtube(self):
        self.app("111299001912")

    def netflix(self):
        self.app("11101200001")

    def browser(self):
        self.app("org.tizen.browser")