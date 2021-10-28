class User:
    __instance = None

    @staticmethod
    def getInstance():
        if User.__instance is None:
            User.__instance = User(
                "usernamexxx", "useremail@gmail.com", "password")
            return User.__instance
        else:
            return User.__instance


    def __init__(self, name, username=None, password=None):
        if User.__instance is not None:
            raise Exception("Class is singleton!")
        else:
            User.__instance = self
            self.username = username
            self.password = password
            self.name = name

