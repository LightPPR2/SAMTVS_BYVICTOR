"""
=========================================
 SAMTVS_BYVICTOR
 Biblioteca para TVs Samsung

 Desenvolvido por:
 Victor Fernando
=========================================
"""

import threading
import time

from .constants import KEEP_ALIVE_INTERVAL, KEEP_ALIVE_KEY


class KeepAlive:

    def __init__(self, tv):
        self.tv = tv
        self.running = False
        self.thread = None

    # ==========================================
    # LOOP
    # ==========================================

    def _loop(self):

        while self.running:

            try:
                self.tv.sender.key(KEEP_ALIVE_KEY)

            except Exception:
                pass

            time.sleep(KEEP_ALIVE_INTERVAL)

    # ==========================================
    # START
    # ==========================================

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._loop,
            daemon=True,
        )

        self.thread.start()

    # ==========================================
    # STOP
    # ==========================================

    def stop(self):
        self.running = False

    # ==========================================
    # STATUS
    # ==========================================

    @property
    def alive(self):
        return self.running