"""
=========================================
 SAMTVS_BYVICTOR
 Biblioteca para TVs Samsung

 Desenvolvido por:
 Victor Fernando
=========================================
"""

import json
import threading


class CommandSender:

    def __init__(self, auth):
        self.auth = auth
        self.lock = threading.Lock()

    # ==========================================
    # ENVIO BRUTO
    # ==========================================

    def send(self, payload):

        with self.lock:

            try:
                self.auth.ws.send(json.dumps(payload))

            except Exception:

                self.auth.reconnect()

                self.auth.ws.send(json.dumps(payload))

    # ==========================================
    # REMOTE KEY
    # ==========================================

    def key(self, key):

        self.send({

            "method": "ms.remote.control",

            "params": {

                "Cmd": "Click",
                "DataOfCmd": key,
                "Option": "false",
                "TypeOfRemote": "SendRemoteKey"

            }

        })

    # ==========================================
    # LONG PRESS
    # ==========================================

    def hold(self, key):

        self.send({

            "method": "ms.remote.control",

            "params": {

                "Cmd": "Press",
                "DataOfCmd": key,
                "Option": "false",
                "TypeOfRemote": "SendRemoteKey"

            }

        })

    def release(self, key):

        self.send({

            "method": "ms.remote.control",

            "params": {

                "Cmd": "Release",
                "DataOfCmd": key,
                "Option": "false",
                "TypeOfRemote": "SendRemoteKey"

            }

        })

    # ==========================================
    # ABRIR APP
    # ==========================================

    def app(self, appid):

        self.send({

            "method": "ms.channel.emit",

            "params": {

                "event": "ed.apps.launch",
                "to": "host",

                "data": {

                    "appId": appid,
                    "action_type": "DEEP_LINK"

                }

            }

        })

    # ==========================================
    # TEXTO
    # ==========================================

    def text(self, text):

        self.send({

            "method": "ms.remote.control",

            "params": {

                "Cmd": text,
                "TypeOfRemote": "SendInputString"

            }

        })

    # ==========================================
    # PAYLOAD CUSTOMIZADO
    # ==========================================

    def raw(self, payload):

        self.send(payload)