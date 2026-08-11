# API Reference

Documentação da API do **SAMTVS BYVICTOR**.

O SAMTVS BYVICTOR permite controlar TVs Samsung Tizen usando Python através de WebSocket.

---

# SamsungTV

A classe principal da biblioteca.

## Importação

```python
from samtvs_byvictor import SamsungTV
```

---

# Criando uma TV

Crie uma instância usando o IP da televisão:

```python
tv = SamsungTV("192.168.1.100")
```

Exemplo:

```python
from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.1.50")
```

---

# Conexão

## connect()

Conecta na televisão:

```python
tv.connect()
```

...