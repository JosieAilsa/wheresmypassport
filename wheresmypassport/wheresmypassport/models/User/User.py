import bcrypt
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from ..meta import Base


class UserModel(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

    def get_password(self, password):
        return bcrypt.checkpw(password.encode('utf8'), self.password.encode('utf8'))

Index('index_user_name', UserModel.username, unique=True)
