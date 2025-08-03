from dataclasses import dataclass, field
import datetime
from enum import Enum
from uuid import UUID
from abc import ABC



class StatusEnum(Enum):
    IN_PROGRESS = 'in_progress'
    SUCCESS = 'success'
    FAILED = 'failed'


@dataclass
class BaseContract(ABC):
    id: str = field(
        default_factory=lambda: str(UUID.uuid4()),
        kw_only=True
    )
    created_at: datetime = field(
        default_factory=datetime.utcnow,
        kw_only=True
    )
    updated_at: datetime = field(
        default_factory=datetime.utcnow,
        kw_only=True
    )
    status: StatusEnum = field(
        kw_only=True
    )
    