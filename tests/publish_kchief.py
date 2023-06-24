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
    logger.info("Starting kchief payload simulator")
    client = mqtt_client("localhost", 1883)

    topic = "CloudBoundContainer"
    f = open("kchief_message_CloudBoundContainer.proto", "rb")
    message = f.read()

    logger.debug("Publish %r", message)
    #client.publish(topic, message)
    time.sleep(2)
    client.publish(topic, message)


if __name__ == "__main__":
    main()
