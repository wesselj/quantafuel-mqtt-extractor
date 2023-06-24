import logging
#import time
from Kognifai import Serialization_pb2
from Kognifai.Serialization import Timeseries_pb2
import gzip

logger = logging.getLogger(__name__)


def parse(payload: bytes, topic: str):
    message_container = Serialization_pb2.MessageArrayContainer()
    message_container.ParseFromString(payload)
    # print(message_container)
    if message_container.compressed:
        data = gzip.decompress(message_container.message_array_bytes)
    else:
        data = message_container.message_array_bytes
    message_array = Serialization_pb2.MessageArray()
    message_array.ParseFromString(data)
    logger.debug(message_array)
    for message in message_array.messages:
        ts = Timeseries_pb2.TimeseriesDoublesReplicationMessage()
        ts.ParseFromString(message.message_bytes)
        extid = ts.external_id
        for event in ts.events:
            timestamp_str = f"{event.timestamp.seconds}{event.timestamp.nanos}"[0:13:1]
            timestamp = float(timestamp_str)
            for value in event.values:
                yield extid, timestamp, value
