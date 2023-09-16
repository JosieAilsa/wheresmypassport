import bcrypt
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Boolean,
)

from sqlalchemy import DateTime
from ..meta import Base
from sqlalchemy.orm import relationship


class PassportModel(Base):
    """Base passport entity"""
    __tablename__ = 'Passports'
    id = Column(Integer, primary_key=True, nullable=False)
    is_stolen = Column(Boolean, nullable=False)
    issue_date = Column(DateTime, nullable=True)
    expiry_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship("UserModel", back_populates="passports")

