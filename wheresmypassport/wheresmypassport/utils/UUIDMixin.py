import uuid

class UUIDMixin():
    """A mixin for checking the validity of UUIDs"""

    @staticmethod
    def validate_uuids(kwargs, keys):
        """Can check if multiple keys in a kwargs objs are valid uuids"""
        for key in keys:
            value = kwargs.get(key)
            if value:
                try:
                    UUIDMixin.is_valid_uuid(value)
                except ValueError as exc:
                    raise ValueError(f"Invalid UUID for {key}.") from exc

    @staticmethod
    def is_valid_uuid(value):
        """Check if a UUID is valid or not"""
        try:
            uuid.UUID(str(value))
        except ValueError:
            return False
        return True
