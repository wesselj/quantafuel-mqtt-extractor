from mqtt_extractor.viridor import ViridorTimeSeries

topic = "/PolymerP2/U/HVAC/TT52105/T"
message = {"measurement": "FltMeas",
           "fields": {"DatVal": 38,
                      "DatSta": False},
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
           "timestamp": "2024-09-06T09:37:31.244Z"}


def test_parse():
    viridor_message = ViridorTimeSeries(message)
    assert viridor_message
