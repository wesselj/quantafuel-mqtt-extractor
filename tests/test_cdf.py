from mqtt_extractor import cdf
from kchief_parser import test_parse_kchief

def test_parse():
    payload = open("tests/cdf.json").read()
    dps = list(cdf.parse(payload, "a-topic"))
    assert dps == [('external-id', 1001, 1), ('external-id', 1002, 2)]


def test_kchief():
    test_parse_kchief()
