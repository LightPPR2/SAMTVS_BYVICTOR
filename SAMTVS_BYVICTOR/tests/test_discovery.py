from samtvs_byvictor.discovery import discover


def test_discover():

    tvs = discover()

    assert isinstance(tvs, list)