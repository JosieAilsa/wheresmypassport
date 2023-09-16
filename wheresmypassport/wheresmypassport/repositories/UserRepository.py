from sqlalchemy.orm import session
from sqlalchemy.exc import (
    SQLAlchemyError, NoResultFound, MultipleResultsFound, StatementError, OperationalError
)
from sqlalchemy.orm.session  import Session as sa_Session
from ..models import UserModel
from sqlalchemy.dialects.postgresql import UUID


class UserRepository:
    """Performs CRUD operations for the User entity."""


    def __init__(self, dbsession):
        self.dbsession = dbsession
            
    def get_users(self) -> [UserModel]: 
        """Get all users"""
        try:
            self.dbsession.query(UserModel).all()
        except NoResultFound:
            print("No result found")
        except OperationalError:
            print("Database connection issue or query execution failure") 
            

    def get_user_by_id(self, user_id) -> UserModel:
        """Find a user by id"""
        try: 
            user = self.dbsession.query(UserModel).filter_by(id=user_id).one()
            return user
        except NoResultFound:
            print("No result found")
        except MultipleResultsFound:
            print("Multiple results found, data integrity issue")
        except OperationalError:
            print("Database connection issue or query execution failure")
        raise SQLAlchemyError
                  
            
    def get_user_by_username(self, user_username):
        """Find a user by username"""
        try: 
            self.session.query(UserModel).filter_by(username=user_username).one()
        except SQLAlchemyError as saerror: 
            raise saerror

    def create_user(self, user) -> UUID:
        """Adds a single user to the database"""
        try:
            self.dbsession.add(user)
            self.dbsession.flush()
            return user.id
        except SQLAlchemyError as error:
            self.dbsession.rollback()
            raise error
    
    def update_user(self, user=UserModel, username=None, password=None, name=None) -> None: 
        """ Updates a users username, password, name."""
        if username: 
            user.username = username
        if password: 
            user.password = password
        if name: 
            user.name = name 
        try: 
            self.dbsession.add(user)
            self.dbsession.commit()
        except SQLAlchemyError as saerror
            print(f'Something went wrong updating the user {saerror}')
            raise saerror

    def delete_user(self, user=UserModel):
        """Deletes a user"""
        self.dbsession.delete(user)
        self.dbsession.commit()   
