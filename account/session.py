from model import User
from datetime import datetime

class Session:
    logout_time: datetime

    def __init__(self, user: User):
        self.user = user
        self.logout_time = datetime.now()

    def update_logout_time(self) -> None:
        self.logout_time = datetime.now()