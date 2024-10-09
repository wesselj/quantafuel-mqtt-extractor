import json
import logging
import time

from paho.mqtt.client import Client as MqttClient

logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    logger.info("Connection to MQTT server open")


def on_disconnect(client, userdata, flags):
    logger.warning("Connection to MQTT server closed")


def mqtt_client(hostname: str, port: int):
    client = MqttClient()
    client.enable_logger(logger)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect_async(hostname, port)
    client.loop_start()
    return client


def now() -> int:
    return int(1000 * time.time())


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Starting CDF payload publisher")
    client = mqtt_client("localhost", 1883)
    time.sleep(1)
    topic = "/PolymerP2/U/HVAC/TT52105/T"
    message = {"payload": {"measurement": "FltMeas",
                 "fields": {"DatVal": 38,
                            "DatSta": "false"},
                 "tags": {"PlantId": "U_HVAC_TT52105_T",
                          "LegendID": "U_HVAC_TT52105_T (Clean area tmp 5)",
                          "LegendIDU": "U_HVAC_TT52105_T (Clean area tmp 5) (degC)",
                          "LegendIU": "U_HVAC_TT52105_T (degC)",
                          "AreaMaj": "U",
                          "AreaSub": "HVAC",
                          "EquipID": "TT52105_2",
                          "PlantDsc": "Clean area tmp 5",
                          "EquipTyp": "T",
                          "DataMin": "0",
                          "DataMax": "44",
                          "Units": "degC"},
                 "timestamp": "2024-10-09T09:30:00.100Z"}
               }
    client.publish(topic, json.dumps(message))
    time.sleep(1)
    client.disconnect()


if __name__ == "__main__":
    main()
