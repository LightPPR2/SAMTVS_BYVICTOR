"""
automation.py

Exemplo de automação usando Arduino.
"""

import serial

from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.0.102")#Troque pelo seu ip

tv.connect()

arduino = serial.Serial(
    "COM3", #Troque pela sua com
    9600,
    timeout=1
)

print("Aguardando comandos...")

while True:

    cmd = (
        arduino
        .readline()
        .decode(errors="ignore")
        .strip()
        .lower()
    )

    if cmd == "up":

        tv.volume_up()

    elif cmd == "down":

        tv.volume_down()

    elif cmd == "power":

        tv.power()

    elif cmd == "home":

        tv.home()

    elif cmd == "youtube":

        tv.youtube()

    elif cmd == "netflix":

        tv.netflix()