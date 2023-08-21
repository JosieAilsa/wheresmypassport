from sqlalchemy.orm import session
from sqlalchemy.exc import SQLAlchemyError
from ..models import UserModel

class UserRepository:
    """Performs CRUD operations for the User entity"""


    def __init__(self):
        self.session = session()

    def create_user(self, user) -> int:
        """Adds a single user to the database"""
        try:
            self.session.add(user)
            self.session.flush()
            return user.id
        except SQLAlchemyError as error:
            self.session.rollback()
            raise error

    def get_user_by_id(self, user_id):
        """Find a user by id"""
        try: 
            self.session.query(UserModel).filter_by(id=user_id).one()
        except SQLAlchemyError as saerror: 
            raise saerror
    
    def get_user_by_username(self, user_username):
        """Find a user by username"""
        try: 
            self.session.query(UserModel).filter_by(username=username).one()
        except SQLAlchemyError as saerror: 
            raise saerror

    
    # def update_user(self,user=UserModel) -> UserModel: 
    #  try:
    #         # GET THE USER BY ID 
    #         # REPLACE THE USER 
    #         return user.id
    #     except SQLAlchemyError as error:
    #         self.session.rollback()
    #         raise error
                


