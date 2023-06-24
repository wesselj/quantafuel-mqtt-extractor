import pytest
from Kognifai import Serialization_pb2
from Kognifai.Serialization import Timeseries_pb2
import gzip


def test_parse_message():
    f = open("kchief_message_CloudBoundContainer.proto", "rb")
    message = f.read()
    parse_message(message)


def parse_message(message):
    message_container = Serialization_pb2.MessageArrayContainer()
    message_container.ParseFromString(message)
    # print(message_container)
    if message_container.compressed:
        data = gzip.decompress(message_container.message_array_bytes)
    else:
        data = message_container.message_array_bytes
    message_array = Serialization_pb2.MessageArray()
    message_array.ParseFromString(data)
    # print(message_array)
    for message in message_array.messages:
        ts = Timeseries_pb2.TimeseriesDoublesReplicationMessage()
        ts.ParseFromString(message.message_bytes)
        ext_id = ts.external_id
        for event in ts.events:
            timestamp = f"{event.timestamp.seconds}{event.timestamp.nanos}"[0:13:1]
            #1687462678958
            #1554415390000
            for value in event.values:
                print(f"Event: {ext_id}: TS: {timestamp} Value: {value}")


