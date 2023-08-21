


class UserService(): 
    """A service for managing user business logic"""

    def __init__(self, user_repository, log_repository, session):
        self.user_repository = user_repository
        self.log_repository = log_repository
        self.session = session

    def create_user(self, username, password):
        new_user = UserModel(username=username, password=password)
        
        # Using repositories to interact with the database
        self.user_repository.create_user(new_user)
        
        log_event = LogEvent(message=f"User {username} created.")
        self.log_repository.add(log_event)
        
        # Committing the transaction
        self.session.commit()