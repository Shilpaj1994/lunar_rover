# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: publish.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='publish.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\rpublish.proto\x12\x0bgazebo.msgs\"F\n\x07Publish\x12\r\n\x05topic\x18\x01 \x02(\t\x12\x10\n\x08msg_type\x18\x02 \x02(\t\x12\x0c\n\x04host\x18\x03 \x02(\t\x12\x0c\n\x04port\x18\x04 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PUBLISH = _descriptor.Descriptor(
  name='Publish',
  full_name='gazebo.msgs.Publish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='gazebo.msgs.Publish.topic', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='gazebo.msgs.Publish.msg_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='gazebo.msgs.Publish.host', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='gazebo.msgs.Publish.port', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=30,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['Publish'] = _PUBLISH

Publish = _reflection.GeneratedProtocolMessageType('Publish', (_message.Message,), dict(
  DESCRIPTOR = _PUBLISH,
  __module__ = 'publish_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Publish)
  ))
_sym_db.RegisterMessage(Publish)


# @@protoc_insertion_point(module_scope)
