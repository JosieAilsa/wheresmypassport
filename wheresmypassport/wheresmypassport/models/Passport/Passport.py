import bcrypt
import uuid

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Boolean,
)

from sqlalchemy import DateTime
from ..meta import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class PassportModel(Base):
    """Base passport entity"""

    __tablename__ = "Passports"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    is_stolen = Column(Boolean, nullable=False)
    issue_date = Column(DateTime, nullable=True)
    expiry_date = Column(DateTime, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("Users.id"))
    user = relationship("UserModel", back_populates="passports")
