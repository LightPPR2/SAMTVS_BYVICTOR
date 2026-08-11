from samtvs_byvictor import SamsungTV


def test_connect():

    tv = SamsungTV("192.168.0.102")

    tv.connect()

    assert tv.connected

    tv.disconnect()