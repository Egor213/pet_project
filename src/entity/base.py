from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class StatusEnum(Enum):
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"


@dataclass
class BaseContract(ABC):
    id: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    status: StatusEnum = field(
        default=StatusEnum.IN_PROGRESS,
        kw_only=True,
    )
