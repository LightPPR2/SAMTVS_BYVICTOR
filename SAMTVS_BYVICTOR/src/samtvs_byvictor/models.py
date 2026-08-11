"""
=========================================
 SAMTVS_BYVICTOR
 Biblioteca para TVs Samsung

 Desenvolvido por:
 Victor Fernando
=========================================
"""

import socket
import requests
from concurrent.futures import ThreadPoolExecutor


def _scan(ip, timeout=0.5):
    """
    Verifica se existe uma TV Samsung nesse IP.
    """

    try:

        r = requests.get(
            f"http://{ip}:8001/api/v2/",
            timeout=timeout
        )

        if r.status_code != 200:
            return None

        data = r.json()

        device = data.get("device", {})

        return {
            "ip": ip,
            "name": device.get("name"),
            "model": device.get("modelName"),
            "os": device.get("OS"),
            "wifiMac": device.get("wifiMac"),
            "id": device.get("id"),
        }

    except Exception:
        return None


def discover(
    subnet=None,
    start=1,
    end=254,
    workers=50
):
    """
    Procura TVs Samsung na rede.
    """

    if subnet is None:

        hostname = socket.gethostname()

        ip = socket.gethostbyname(hostname)

        subnet = ".".join(ip.split(".")[:3])

    ips = [
        f"{subnet}.{i}"
        for i in range(start, end + 1)
    ]

    encontrados = []

    with ThreadPoolExecutor(max_workers=workers) as executor:

        resultados = executor.map(
            _scan,
            ips
        )

        for tv in resultados:

            if tv:
                encontrados.append(tv)

    return encontrados