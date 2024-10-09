from json import loads
from datetime import datetime
from cognite.client.data_classes import time_series
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


def get_timeseries_to_update():
    timeseries = []
    for key in TimeseriesHolder.timeseries.keys():
        value = TimeseriesHolder.timeseries.get(key)
        ts = time_series.TimeSeries(external_id=key)
        if "payload" in value:
            tags = value["payload"]["tags"]
        else:
            tags = value["tags"]
        ts.name = tags["PlantId"]
        ts.description = tags["LegendIDU"]
        ts.unit = tags["Units"]
        ts.metadata = tags
        timeseries.append(ts)
    TimeseriesHolder.timeseries.clear()
    return timeseries


def parse_ts_value(message: dict, topic: str):
    if "payload" in message:
        item = message["payload"]
    else:
        item = message
    measurement = item["measurement"]
    tags = item["tags"]
    equipment_id = tags["EquipID"]
    extid = "P2_" + equipment_id + ":" + measurement
    timestamp_str = item["timestamp"]
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp_long = timestamp.timestamp() * 1000
    value = item["fields"]["DatVal"]
    return extid, timestamp_long, value

