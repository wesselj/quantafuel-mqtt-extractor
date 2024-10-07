from json import loads
import logging

logger = logging.getLogger(__name__)


class TimeseriesHolder:
    timeseries = {}

    @staticmethod
    def add(extid: str, message: dict, topic: str):
        if not TimeseriesHolder.timeseries.get(extid):
            message["topic"] = topic
            TimeseriesHolder.timeseries[extid] = message


def parse(payload: bytes, topic: str):
    msg = loads(payload)
    logger.debug("Message: %r %r", topic, msg)
    extid, timestamp, value = parse_ts_value(msg, topic)
    TimeseriesHolder.add(extid, msg, topic)
    yield extid, timestamp, value


def parse_ts_value(message: dict, topic: str):
    item = message["payload"]
    measurement = item["measurement"]
    tags = item["tags"]
    equipment_id = tags["EquipID"]
    extid = equipment_id + ":" + measurement
    timestamp = item["timestamp"]
    value = item["fields"]["DatVal"]
    return extid, timestamp, value

