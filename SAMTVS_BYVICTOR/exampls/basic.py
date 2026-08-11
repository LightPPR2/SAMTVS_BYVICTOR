from samtvs_byvictor import SamsungTV

tv = SamsungTV("192.168.0.102")

tv.connect()

tv.home()

tv.volume_up()

tv.disconnect()