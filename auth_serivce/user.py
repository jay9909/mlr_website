from web import db


class User():
    player_id = 0
    logged_in = False

    def __init__(self, id=0, logged_in=False):
        self.player_id = id
        self.logged_in = logged_in

    def is_umpire(self, session_id):
        return False
