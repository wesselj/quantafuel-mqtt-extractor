# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Kognifai.Serialization.Dataframe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from Kognifai.Serialization import Basetypes_pb2 as Kognifai_dot_Serialization_dot_Basetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&Kognifai.Serialization.Dataframe.proto\x12\x16kognifai.serialization\x1a\x1fgoogle/protobuf/timestamp.proto\x1a&Kognifai.Serialization.Basetypes.proto\"\xa1\x01\n\x0f\x44\x61taframeColumn\x12\x39\n\tdata_type\x18\x01 \x01(\x0e\x32&.kognifai.serialization.CommonDataType\x12\x14\n\x0c\x64ouble_value\x18\x02 \x01(\x01\x12\x13\n\x0bint64_value\x18\x03 \x01(\x03\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\x12\x12\n\nbool_value\x18\x05 \x01(\x08\"\x9e\x02\n\x0e\x44\x61taframeEvent\x12\x31\n\rcreation_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x07\x43olumns\x18\x02 \x03(\x0b\x32\'.kognifai.serialization.DataframeColumn\x12J\n\nproperties\x18\x03 \x03(\x0b\x32\x36.kognifai.serialization.DataframeEvent.PropertiesEntry\x1aS\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .kognifai.serialization.Property:\x02\x38\x01\"j\n\x1b\x44\x61taframeReplicationMessage\x12\x13\n\x0b\x65xternal_id\x18\x01 \x01(\t\x12\x36\n\x06\x65vents\x18\x02 \x03(\x0b\x32&.kognifai.serialization.DataframeEvent*;\n\x14\x44\x61taframeMessageType\x12#\n\x1f\x44\x61taframeReplicationMessageType\x10\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Kognifai.Serialization.Dataframe_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATAFRAMEEVENT_PROPERTIESENTRY._options = None
  _DATAFRAMEEVENT_PROPERTIESENTRY._serialized_options = b'8\001'
  _globals['_DATAFRAMEMESSAGETYPE']._serialized_start=700
  _globals['_DATAFRAMEMESSAGETYPE']._serialized_end=759
  _globals['_DATAFRAMECOLUMN']._serialized_start=140
  _globals['_DATAFRAMECOLUMN']._serialized_end=301
  _globals['_DATAFRAMEEVENT']._serialized_start=304
  _globals['_DATAFRAMEEVENT']._serialized_end=590
  _globals['_DATAFRAMEEVENT_PROPERTIESENTRY']._serialized_start=507
  _globals['_DATAFRAMEEVENT_PROPERTIESENTRY']._serialized_end=590
  _globals['_DATAFRAMEREPLICATIONMESSAGE']._serialized_start=592
  _globals['_DATAFRAMEREPLICATIONMESSAGE']._serialized_end=698
# @@protoc_insertion_point(module_scope)
