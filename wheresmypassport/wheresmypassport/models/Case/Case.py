import uuid
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Enum,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from ..meta import Base


class CaseModel(Base):
    """Case model class. Has a one to many relationship with User. Many to many with passports"""
    __tablename__ = 'Cases'
    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    requested = Column(DateTime, nullable=False)
    received = Column(DateTime, nullable=True)
    current_status = Column(
        Enum(
            'initial request',
            'documents sent',
            'reviewing',
            'approved',
            'posted',
            'complete',
            name='case_status_enum'
        ),
        nullable=False)
    old_passport = Column(UUID(as_uuid=True), ForeignKey('Passports.id'))
    new_passport = Column(UUID(as_uuid=True), ForeignKey('Passports.id'))

    # One to many relationship with user
    user = relationship("UserModel", back_populates="cases")
    user_id = Column(UUID(as_uuid=True), ForeignKey('Users.id'))
