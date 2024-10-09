from mqtt_extractor import viridor


def test_parse():
    payload = open("tests/cdf.json").read()
    dps = list(viridor.parse(payload, "/PolymerP2/U/HVAC/TT52105/T"))
    assert len(dps) > 0


def test_get_timeseries_to_update():
    payload = open("tests/cdf.json").read()
    dps = list(viridor.parse(payload, "/PolymerP2/U/HVAC/TT52105/T"))
    ts = viridor.get_timeseries_to_update()
    assert len(ts) == 1


def get_viridor_message():
    payload = {"topic": "/PolymerP2/U/HVAC/TT52105/T",
               "payload": {"measurement": "FltMeas",
                           "fields": {"DatVal": 38,
                                      "DatSta": false},
                           "tags": {"PlantId": "U_HVAC_TT52105_T",
                                    "LegendID": "U_HVAC_TT52105_T (Clean area tmp 5)",
                                    "LegendIDU": "U_HVAC_TT52105_T (Clean area tmp 5) (degC)",
                                    "LegendIU": "U_HVAC_TT52105_T (degC)",
                                    "AreaMaj": "U",
                                    "AreaSub": "HVAC",
                                    "EquipID": "TT52105",
                                    "PlantDsc": "Clean area tmp 5",
                                    "EquipTyp": "T",
                                    "DataMin": "0",
                                    "DataMax": "44",
                                    "Units": "degC"},
                           "timestamp": "2024-09-06T09:37:31.244Z"},
               "qos": 0,
               "retain": false,
               "_msgid": "59f207ca0e349e75"}


