from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Table,
)
from .meta import Base

case_passport_schema = Table(
    'case_passport', Base.metadata,
    Column('case_id', Integer, ForeignKey('Cases.id')),
    Column('current_passport', Integer, ForeignKey('Passport.id')),
)
