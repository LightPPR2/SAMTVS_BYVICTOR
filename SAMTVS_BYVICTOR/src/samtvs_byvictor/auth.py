"""
Autenticação e conexão com TVs Samsung
"""

import base64
import json
import os
import ssl

import websocket


class AuthManager:

    def __init__(
        self,
        ip,
        port=8002,
        name="Python",
        token_file="tv_token.txt",
    ):

        self.ip = ip
        self.port = port
        self.name = name
        self.token_file = token_file

        self.ws = None
        self.token = ""

        self.load_token()

    @property
    def connected(self):
        return self.ws is not None

    def load_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, "r", encoding="utf-8") as f:
                self.token = f.read().strip()

    def save_token(self, token):
        self.token = token

        with open(self.token_file, "w", encoding="utf-8") as f:
            f.write(token)

    def build_url(self):

        nome = base64.b64encode(
            self.name.encode()
        ).decode()

        url = (
            f"wss://{self.ip}:{self.port}"
            "/api/v2/channels/"
            "samsung.remote.control"
            f"?name={nome}"
        )

        if self.token:
            url += f"&token={self.token}"

        return url

    def connect(self):

        self.ws = websocket.create_connection(
            self.build_url(),
            sslopt={
                "cert_reqs": ssl.CERT_NONE
            }
        )

        resposta = self.ws.recv()

        try:

            dados = json.loads(resposta)

            token = (
                dados.get("data", {})
                     .get("token")
            )

            if not token:

                token = (
                    dados.get("data", {})
                         .get("clients", [{}])[0]
                         .get("attributes", {})
                         .get("token")
                )

            if token:
                self.save_token(token)

        except Exception:
            pass

        return self

    def disconnect(self):

        if self.ws:

            try:
                self.ws.close()
            except Exception:
                pass

            self.ws = None

    def send(self, payload):

        if not self.connected:
            raise RuntimeError("TV não conectada.")

        self.ws.send(json.dumps(payload))