import bcrypt

from ..meta import Base
from ..Case.Case import CaseModel
from ..Passport.Passport import PassportModel
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = 'Users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    name = Column(Text, nullable=False)

    def __init__(self, username, password, *args, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        
    # Many to 1 relationship User <--> Cases
    passports = relationship(PassportModel, back_populates="user")
    cases = relationship(CaseModel, back_populates="user")

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

    def get_password(self, password):
        return bcrypt.checkpw(password.encode('utf8'), self.password.encode('utf8'))

Index('index_user_name', UserModel.username, unique=True)
