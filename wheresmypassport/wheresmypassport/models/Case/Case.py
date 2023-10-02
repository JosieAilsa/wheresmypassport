from wheresmypassport.utils import UUIDMixin
import uuid
from sqlalchemy import Column, ForeignKey, Integer, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..meta import Base
from ...enums.CaseStatus import CaseStatus


class CaseModel(Base, UUIDMixin):
    """Case model class. Has a one to many relationship with User. Many to many with passports"""

    __tablename__ = "Cases"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    requested = Column(DateTime, nullable=False)
    received = Column(DateTime, nullable=True)
    current_status = Column(Enum(CaseStatus), nullable=False)
    old_passport = Column(UUID(as_uuid=True), ForeignKey("Passports.id"))
    new_passport = Column(UUID(as_uuid=True), ForeignKey("Passports.id"))

    # One to many relationship with user -> one user could have multiple cases
    user = relationship("UserModel", back_populates="cases")
    user_id = Column(UUID(as_uuid=True), ForeignKey("Users.id"))

    def __init__(
        self, requested_time=DateTime, user_id=UUID, current_status=CaseStatus, **kwargs
    ):
        self.requested = requested_time  # When was the request opened
        # Assumes if just created at initial stage
        self.current_status = current_status or CaseStatus.INITIAL_REQUEST
        self.user_id = user_id
        self._validate_uuids(["old_passport", "new_passport"])
        self.received = kwargs.get("received", None)
        # The previous passport before this one
        self.old_passport = kwargs.get("old_passport", None)
        # The new passport requested
        self.new_passport = kwargs.get("new_passport", None)


def _validate_uuids(kwargs, keys):
    for key in keys:
        value = kwargs.get(key)
        if value:
            try:
                uuid.UUID(str(value))
            except ValueError:
                raise ValueError(f"Invalid UUID for {key}.")
