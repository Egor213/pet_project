from datetime import datetime
from typing import Any, Optional

import grpc.aio
from google.protobuf.timestamp_pb2 import Timestamp

from src.api.grpc.v1 import log_service_pb2 as pb2
from src.api.grpc.v1 import log_service_pb2_grpc as stub_module
from src.services.grpc_service.base import BaseGrpcService


class LogGrpcService(BaseGrpcService):
    def get_stub_class(self):
        return stub_module.LogServiceStub

    def _get_log_level_enum(self, level: str) -> int:
        level_upper = level.upper()
        if level_upper == "INFO":
            return pb2.INFO
        elif level_upper == "WARN":
            return pb2.WARN
        elif level_upper == "ERROR":
            return pb2.ERROR
        else:
            return pb2.LOG_LEVEL_UNSPECIFIED

    async def send_log(
        self,
        service: str,
        level: str,
        message: str,
        timestamp: Optional[datetime] = None,
    ) -> dict[str, Any]:
        await self.connect()

        log_level_enum = self._get_log_level_enum(level)

        if timestamp is None:
            timestamp = datetime.now()

        timestamp_pb = self._datetime_to_timestamp(timestamp)

        request = pb2.SendLogRequest(
            service=service,
            level=log_level_enum,
            message=message,
            timestamp=timestamp_pb,
        )

        try:
            response = await self.stub.SendLog(request)

            return {
                "log_id": response.log_id,
                "status": pb2.SendStatus.Name(response.status),
                "success": response.status == pb2.STATUS_OK,
            }
        except grpc.aio.AioRpcError as e:
            return {
                "log_id": None,
                "status": "RPC_ERROR",
                "success": False,
                "error": f"{e.code()}: {e.details()}",
            }
