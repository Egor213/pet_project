from uuid import UUID

from src.exceptions.contract import NotFoundContract
from src.exceptions.base import ValidationError

def validate_uuid(uuid_str, version=4):
    try:
        UUID(uuid_str, version=version)
    except ValueError:
        raise ValidationError(f"Некорректный UUID: {uuid_str}")

def validate_found_entity(contract):
    if not contract:
        raise NotFoundContract
