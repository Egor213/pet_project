# base.py
import grpc.aio
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from typing import Any


class BaseGrpcService(ABC):
    """Базовый асинхронный gRPC сервис"""

    def __init__(self, host: str = "localhost", port: int = 50051):
        self.host = host
        self.port = port
        self._channel = None
        self._stub = None

    @abstractmethod
    def get_stub_class(self) -> Any:
        pass

    async def connect(self):
        if self._channel is None or self._channel._close:
            self._channel = grpc.aio.insecure_channel(f"{self.host}:{self.port}")
            stub_class = self.get_stub_class()
            self._stub = stub_class(self._channel)

    @property
    def stub(self):
        if self._stub is None:
            raise RuntimeError("Service not connected. Call await connect() first.")
        return self._stub

    async def close(self):
        if self._channel is not None:
            try:
                await self._channel.close()
            finally:
                self._channel = None
                self._stub = None

    @staticmethod
    def _datetime_to_timestamp(dt: datetime) -> Timestamp:
        timestamp = Timestamp()
        timestamp.FromDatetime(dt)
        return timestamp

    @staticmethod
    def _timestamp_to_datetime(timestamp: Timestamp) -> datetime:
        return timestamp.ToDatetime()
