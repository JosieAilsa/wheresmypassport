class UserService:
    """A service for managing user business logic"""

    def __init__(self, user_repository, log_repository, session):
        self.user_repository = user_repository
        self.log_repository = log_repository
        self.session = session
