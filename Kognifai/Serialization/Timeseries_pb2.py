# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Kognifai.Serialization.Timeseries.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from Kognifai.Serialization import Basetypes_pb2 as Kognifai_dot_Serialization_dot_Basetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'Kognifai.Serialization.Timeseries.proto\x12\x16kognifai.serialization\x1a\x1fgoogle/protobuf/timestamp.proto\x1a&Kognifai.Serialization.Basetypes.proto\"M\n\x0c\x44oublesEvent\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06values\x18\x02 \x03(\x01\"p\n#TimeseriesDoublesReplicationMessage\x12\x13\n\x0b\x65xternal_id\x18\x01 \x01(\t\x12\x34\n\x06\x65vents\x18\x02 \x03(\x0b\x32$.kognifai.serialization.DoublesEvent*D\n\x15TimeseriesMessageType\x12+\n\'TimeseriesDoublesReplicationMessageType\x10\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Kognifai.Serialization.Timeseries_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TIMESERIESMESSAGETYPE']._serialized_start=333
  _globals['_TIMESERIESMESSAGETYPE']._serialized_end=401
  _globals['_DOUBLESEVENT']._serialized_start=140
  _globals['_DOUBLESEVENT']._serialized_end=217
  _globals['_TIMESERIESDOUBLESREPLICATIONMESSAGE']._serialized_start=219
  _globals['_TIMESERIESDOUBLESREPLICATIONMESSAGE']._serialized_end=331
# @@protoc_insertion_point(module_scope)
