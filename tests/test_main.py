from mqtt_extractor import main

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


def test_get_handler():
    topic_standard = "/topic/one/two"
    topic_hash_wildcard = "/topic/one/#/wherever"
    topic_hash_wildcard_2 = "topic/one/#"
    topic_plus_wildcard = "/topic/two/+/wherever"
    topic_plus_wildcard_2 = "topic/two/+"
    topic_multiple_wildcard = "/topic/three/#/wherever/+/test"
    topic_multiple_wildcard_2 = "topic/three/+/two/#"
    topic = "/PolymerP2/#"

    main._handlers = {topic_standard: "handler_standard",
                      topic_hash_wildcard: "handler_hash_1",
                      topic_hash_wildcard_2: "handler_hash_2",
                      topic_plus_wildcard: "handler_plus_1",
                      topic_plus_wildcard_2: "handler_plus_2",
                      topic_multiple_wildcard: "handler_multiple_1",
                      topic_multiple_wildcard_2: "handler_multiple_2",
                      topic: "topic_handler"
                      }

    assert main.get_handler(topic_standard) == "handler_standard"
    assert main.get_handler("/topic/one/two/three/wherever") == "handler_hash_1"
    assert main.get_handler("topic/one/two/three") == "handler_hash_2"
    assert main.get_handler("/topic/two/three/wherever") == "handler_plus_1"
    assert main.get_handler("topic/two/four") == "handler_plus_2"
    assert main.get_handler("/topic/three/four/wherever/here/test") == "handler_multiple_1"
    assert main.get_handler("topic/three/four/two/over/there") == "handler_multiple_2"
    assert main.get_handler("/PolymerP2/U/HVAC/TT52105/T") == "topic_handler"
