# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graph.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='graph.proto',
  package='protobuf',
  syntax='proto2',
  serialized_options=b'\n$uk.ac.cam.acr31.features.javac.protoB\013GraphProtos',
  serialized_pb=b'\n\x0bgraph.proto\x12\x08protobuf\"\xaf\x03\n\x0b\x46\x65\x61tureNode\x12\n\n\x02id\x18\x01 \x01(\x03\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.protobuf.FeatureNode.NodeType\x12\x10\n\x08\x63ontents\x18\x03 \x01(\t\x12\x15\n\rstartPosition\x18\x04 \x01(\x05\x12\x13\n\x0b\x65ndPosition\x18\x05 \x01(\x05\x12\x17\n\x0fstartLineNumber\x18\x06 \x01(\x05\x12\x15\n\rendLineNumber\x18\x07 \x01(\x05\"\xf7\x01\n\x08NodeType\x12\t\n\x05TOKEN\x10\x01\x12\x0f\n\x0b\x41ST_ELEMENT\x10\x02\x12\x10\n\x0c\x43OMMENT_LINE\x10\x03\x12\x11\n\rCOMMENT_BLOCK\x10\x04\x12\x13\n\x0f\x43OMMENT_JAVADOC\x10\x05\x12\x14\n\x10IDENTIFIER_TOKEN\x10\x07\x12\x0c\n\x08\x46\x41KE_AST\x10\x08\x12\n\n\x06SYMBOL\x10\t\x12\x0e\n\nSYMBOL_TYP\x10\n\x12\x0e\n\nSYMBOL_VAR\x10\x0b\x12\x0e\n\nSYMBOL_MTH\x10\x0c\x12\x08\n\x04TYPE\x10\r\x12\x14\n\x10METHOD_SIGNATURE\x10\x0e\x12\x0c\n\x08\x41ST_LEAF\x10\x0f\x12\x07\n\x03LOG\x10\x11\"\xa0\x03\n\x0b\x46\x65\x61tureEdge\x12\x10\n\x08sourceId\x18\x01 \x01(\x03\x12\x15\n\rdestinationId\x18\x02 \x01(\x03\x12,\n\x04type\x18\x03 \x01(\x0e\x32\x1e.protobuf.FeatureEdge.EdgeType\"\xb9\x02\n\x08\x45\x64geType\x12\x14\n\x10\x41SSOCIATED_TOKEN\x10\x01\x12\x0e\n\nNEXT_TOKEN\x10\x02\x12\r\n\tAST_CHILD\x10\x03\x12\x08\n\x04NONE\x10\x04\x12\x0e\n\nLAST_WRITE\x10\x05\x12\x0c\n\x08LAST_USE\x10\x06\x12\x11\n\rCOMPUTED_FROM\x10\x07\x12\x0e\n\nRETURNS_TO\x10\x08\x12\x13\n\x0f\x46ORMAL_ARG_NAME\x10\t\x12\x0e\n\nGUARDED_BY\x10\n\x12\x17\n\x13GUARDED_BY_NEGATION\x10\x0b\x12\x14\n\x10LAST_LEXICAL_USE\x10\x0c\x12\x0b\n\x07\x43OMMENT\x10\r\x12\x15\n\x11\x41SSOCIATED_SYMBOL\x10\x0e\x12\x0c\n\x08HAS_TYPE\x10\x0f\x12\x11\n\rASSIGNABLE_TO\x10\x10\x12\x14\n\x10METHOD_SIGNATURE\x10\x11\"\xba\x01\n\x05Graph\x12#\n\x04node\x18\x01 \x03(\x0b\x32\x15.protobuf.FeatureNode\x12#\n\x04\x65\x64ge\x18\x02 \x03(\x0b\x32\x15.protobuf.FeatureEdge\x12\x12\n\nsourceFile\x18\x03 \x01(\t\x12*\n\x0b\x66irst_token\x18\x04 \x01(\x0b\x32\x15.protobuf.FeatureNode\x12\'\n\x08\x61st_root\x18\x05 \x01(\x0b\x32\x15.protobuf.FeatureNodeB3\n$uk.ac.cam.acr31.features.javac.protoB\x0bGraphProtos'
)



_FEATURENODE_NODETYPE = _descriptor.EnumDescriptor(
  name='NodeType',
  full_name='protobuf.FeatureNode.NodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TOKEN', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AST_ELEMENT', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMENT_LINE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMENT_BLOCK', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMENT_JAVADOC', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDENTIFIER_TOKEN', index=5, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAKE_AST', index=6, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYMBOL', index=7, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYMBOL_TYP', index=8, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYMBOL_VAR', index=9, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYMBOL_MTH', index=10, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE', index=11, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METHOD_SIGNATURE', index=12, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AST_LEAF', index=13, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=14, number=17,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=210,
  serialized_end=457,
)
_sym_db.RegisterEnumDescriptor(_FEATURENODE_NODETYPE)

_FEATUREEDGE_EDGETYPE = _descriptor.EnumDescriptor(
  name='EdgeType',
  full_name='protobuf.FeatureEdge.EdgeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ASSOCIATED_TOKEN', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEXT_TOKEN', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AST_CHILD', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_WRITE', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_USE', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPUTED_FROM', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETURNS_TO', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMAL_ARG_NAME', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUARDED_BY', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUARDED_BY_NEGATION', index=10, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_LEXICAL_USE', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMENT', index=12, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSOCIATED_SYMBOL', index=13, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAS_TYPE', index=14, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSIGNABLE_TO', index=15, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METHOD_SIGNATURE', index=16, number=17,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=563,
  serialized_end=876,
)
_sym_db.RegisterEnumDescriptor(_FEATUREEDGE_EDGETYPE)


_FEATURENODE = _descriptor.Descriptor(
  name='FeatureNode',
  full_name='protobuf.FeatureNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.FeatureNode.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='protobuf.FeatureNode.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='protobuf.FeatureNode.contents', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startPosition', full_name='protobuf.FeatureNode.startPosition', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endPosition', full_name='protobuf.FeatureNode.endPosition', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startLineNumber', full_name='protobuf.FeatureNode.startLineNumber', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endLineNumber', full_name='protobuf.FeatureNode.endLineNumber', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEATURENODE_NODETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=457,
)


_FEATUREEDGE = _descriptor.Descriptor(
  name='FeatureEdge',
  full_name='protobuf.FeatureEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sourceId', full_name='protobuf.FeatureEdge.sourceId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destinationId', full_name='protobuf.FeatureEdge.destinationId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='protobuf.FeatureEdge.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEATUREEDGE_EDGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=876,
)


_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='protobuf.Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='protobuf.Graph.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge', full_name='protobuf.Graph.edge', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sourceFile', full_name='protobuf.Graph.sourceFile', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_token', full_name='protobuf.Graph.first_token', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ast_root', full_name='protobuf.Graph.ast_root', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=879,
  serialized_end=1065,
)

_FEATURENODE.fields_by_name['type'].enum_type = _FEATURENODE_NODETYPE
_FEATURENODE_NODETYPE.containing_type = _FEATURENODE
_FEATUREEDGE.fields_by_name['type'].enum_type = _FEATUREEDGE_EDGETYPE
_FEATUREEDGE_EDGETYPE.containing_type = _FEATUREEDGE
_GRAPH.fields_by_name['node'].message_type = _FEATURENODE
_GRAPH.fields_by_name['edge'].message_type = _FEATUREEDGE
_GRAPH.fields_by_name['first_token'].message_type = _FEATURENODE
_GRAPH.fields_by_name['ast_root'].message_type = _FEATURENODE
DESCRIPTOR.message_types_by_name['FeatureNode'] = _FEATURENODE
DESCRIPTOR.message_types_by_name['FeatureEdge'] = _FEATUREEDGE
DESCRIPTOR.message_types_by_name['Graph'] = _GRAPH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureNode = _reflection.GeneratedProtocolMessageType('FeatureNode', (_message.Message,), {
  'DESCRIPTOR' : _FEATURENODE,
  '__module__' : 'graph_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.FeatureNode)
  })
_sym_db.RegisterMessage(FeatureNode)

FeatureEdge = _reflection.GeneratedProtocolMessageType('FeatureEdge', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREEDGE,
  '__module__' : 'graph_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.FeatureEdge)
  })
_sym_db.RegisterMessage(FeatureEdge)

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), {
  'DESCRIPTOR' : _GRAPH,
  '__module__' : 'graph_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Graph)
  })
_sym_db.RegisterMessage(Graph)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
