from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Enum, 
    DateTime
)
from sqlalchemy.orm import relationship

from ..meta import Base
from ..schemas import case_passport_schema

class CaseModel(Base):
    """Case model class. Has a one to many relationship with User. Many to many with passports"""
    __tablename__ = 'Cases'
    id = Column(Integer, primary_key=True, nullable=False)
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
        ),
        nullable=False)
    current_passport = Column(Integer, ForeignKey('Passport.id'))
    new_passport = Column(Integer, ForeignKey('Passport.id'))
    passports = relationship(
        "PassportModel",
        secondary=case_passport_schema,
        back_populates="cases"
    )

    # One to many relationship with user 
    user_id = Column(Integer, ForeignKey('UserModel.id'))
    user = relationship("UserModel", back_populates="cases")

