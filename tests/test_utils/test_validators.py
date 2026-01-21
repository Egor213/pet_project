import pytest
from uuid import uuid4

from src.services.validators import validate_uuid, validate_found_entity
from src.exceptions.base import ValidationError
from src.exceptions.contract import NotFoundContract


def test_validate_uuid_ok():
    validate_uuid(str(uuid4()))


def test_validate_uuid_fail():
    import pytest

    with pytest.raises(ValidationError):
        validate_uuid("invalid-uuid")


def test_validate_found_entity_ok():
    validate_found_entity({"id": "123"})


def test_validate_found_entity_fail():
    import pytest

    with pytest.raises(NotFoundContract):
        validate_found_entity(None)
