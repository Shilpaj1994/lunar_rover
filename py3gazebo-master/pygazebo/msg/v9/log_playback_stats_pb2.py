# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log_playback_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import time_pb2 as time__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='log_playback_stats.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x18log_playback_stats.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\"c\n\x15LogPlaybackStatistics\x12%\n\nstart_time\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Time\x12#\n\x08\x65nd_time\x18\x02 \x02(\x0b\x32\x11.gazebo.msgs.Time')
  ,
  dependencies=[time__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOGPLAYBACKSTATISTICS = _descriptor.Descriptor(
  name='LogPlaybackStatistics',
  full_name='gazebo.msgs.LogPlaybackStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='gazebo.msgs.LogPlaybackStatistics.start_time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='gazebo.msgs.LogPlaybackStatistics.end_time', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=152,
)

_LOGPLAYBACKSTATISTICS.fields_by_name['start_time'].message_type = time__pb2._TIME
_LOGPLAYBACKSTATISTICS.fields_by_name['end_time'].message_type = time__pb2._TIME
DESCRIPTOR.message_types_by_name['LogPlaybackStatistics'] = _LOGPLAYBACKSTATISTICS

LogPlaybackStatistics = _reflection.GeneratedProtocolMessageType('LogPlaybackStatistics', (_message.Message,), dict(
  DESCRIPTOR = _LOGPLAYBACKSTATISTICS,
  __module__ = 'log_playback_stats_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.LogPlaybackStatistics)
  ))
_sym_db.RegisterMessage(LogPlaybackStatistics)


# @@protoc_insertion_point(module_scope)
