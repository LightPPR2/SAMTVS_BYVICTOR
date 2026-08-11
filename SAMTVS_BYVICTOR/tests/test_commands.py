from samtvs_byvictor import SamsungTV


def test_home():

    tv = SamsungTV("192.168.0.102")

    tv.connect()

    tv.home()

    tv.disconnect()