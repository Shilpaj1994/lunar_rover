# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugin.proto

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
  name='plugin.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x0cplugin.proto\x12\x0bgazebo.msgs\"<\n\x06Plugin\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x66ilename\x18\x02 \x02(\t\x12\x12\n\x08innerxml\x18\x03 \x01(\t:\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLUGIN = _descriptor.Descriptor(
  name='Plugin',
  full_name='gazebo.msgs.Plugin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Plugin.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='gazebo.msgs.Plugin.filename', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='innerxml', full_name='gazebo.msgs.Plugin.innerxml', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  serialized_start=29,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['Plugin'] = _PLUGIN

Plugin = _reflection.GeneratedProtocolMessageType('Plugin', (_message.Message,), dict(
  DESCRIPTOR = _PLUGIN,
  __module__ = 'plugin_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Plugin)
  ))
_sym_db.RegisterMessage(Plugin)


# @@protoc_insertion_point(module_scope)
