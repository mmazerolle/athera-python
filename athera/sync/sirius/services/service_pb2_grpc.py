# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from athera.sync.sirius.services import service_pb2 as sirius_dot_services_dot_service__pb2


class SiriusStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Mounts = channel.unary_unary(
        '/sirius.services.Sirius/Mounts',
        request_serializer=sirius_dot_services_dot_service__pb2.MountsRequest.SerializeToString,
        response_deserializer=sirius_dot_services_dot_service__pb2.MountsResult.FromString,
        )
    self.FilesList = channel.unary_stream(
        '/sirius.services.Sirius/FilesList',
        request_serializer=sirius_dot_services_dot_service__pb2.FilesListRequest.SerializeToString,
        response_deserializer=sirius_dot_services_dot_service__pb2.FilesListResponse.FromString,
        )
    self.FileContents = channel.unary_stream(
        '/sirius.services.Sirius/FileContents',
        request_serializer=sirius_dot_services_dot_service__pb2.FileContentsRequest.SerializeToString,
        response_deserializer=sirius_dot_services_dot_service__pb2.FileContentsResult.FromString,
        )
    self.FileUpload = channel.stream_unary(
        '/sirius.services.Sirius/FileUpload',
        request_serializer=sirius_dot_services_dot_service__pb2.FileUploadRequest.SerializeToString,
        response_deserializer=sirius_dot_services_dot_service__pb2.FileUploadResponse.FromString,
        )


class SiriusServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Mounts(self, request, context):
    """Context is used to get the mounts which are required and returns a lineage result
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FilesList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FileContents(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FileUpload(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SiriusServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Mounts': grpc.unary_unary_rpc_method_handler(
          servicer.Mounts,
          request_deserializer=sirius_dot_services_dot_service__pb2.MountsRequest.FromString,
          response_serializer=sirius_dot_services_dot_service__pb2.MountsResult.SerializeToString,
      ),
      'FilesList': grpc.unary_stream_rpc_method_handler(
          servicer.FilesList,
          request_deserializer=sirius_dot_services_dot_service__pb2.FilesListRequest.FromString,
          response_serializer=sirius_dot_services_dot_service__pb2.FilesListResponse.SerializeToString,
      ),
      'FileContents': grpc.unary_stream_rpc_method_handler(
          servicer.FileContents,
          request_deserializer=sirius_dot_services_dot_service__pb2.FileContentsRequest.FromString,
          response_serializer=sirius_dot_services_dot_service__pb2.FileContentsResult.SerializeToString,
      ),
      'FileUpload': grpc.stream_unary_rpc_method_handler(
          servicer.FileUpload,
          request_deserializer=sirius_dot_services_dot_service__pb2.FileUploadRequest.FromString,
          response_serializer=sirius_dot_services_dot_service__pb2.FileUploadResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sirius.services.Sirius', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
