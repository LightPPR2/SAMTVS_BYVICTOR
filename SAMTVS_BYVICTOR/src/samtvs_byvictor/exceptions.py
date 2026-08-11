"""
Exceções da SAMTVS_BYVICTOR
"""


class SamsungTVError(Exception):
    """Exceção base da biblioteca."""
    pass


class ConnectionError(SamsungTVError):
    """Falha ao conectar à TV."""
    pass


class AuthenticationError(SamsungTVError):
    """Falha na autenticação/token."""
    pass


class CommandError(SamsungTVError):
    """Erro ao enviar comando."""
    pass


class AppLaunchError(SamsungTVError):
    """Erro ao abrir um aplicativo."""
    pass


class TVOfflineError(ConnectionError):
    """A TV está desligada ou inacessível."""
    pass


class InvalidKeyError(CommandError):
    """KEY_ inexistente ou inválida."""
    pass


class InvalidAppError(AppLaunchError):
    """AppId inválido."""
    pass