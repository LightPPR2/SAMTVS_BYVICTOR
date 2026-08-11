# Examples

Exemplos de uso do **SAMTVS BYVICTOR**.

Esta página mostra exemplos práticos para controlar uma TV Samsung Tizen usando Python.

---

# Conexão básica

O exemplo mais simples conecta na TV e envia um comando.

```python
from samtvs_byvictor import SamsungTV

TV_IP = "192.168.1.50"

tv = SamsungTV(TV_IP)

tv.connect()

tv.send_key("KEY_HOME")

tv.disconnect()