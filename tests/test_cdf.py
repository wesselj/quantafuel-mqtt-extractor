from mqtt_extractor import cdf


def test_parse():
    payload = open("tests/cdf.json").read()
    dps = list(cdf.parse(payload, "/PolymerP2/U/HVAC/TT52105/T"))
    dps2 = list(cdf.parse(payload, "/PolymerP2/U/HVAC/TT52105/T"))
    print(dps)


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


