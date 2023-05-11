class User:

    username = str
    userSaber = str

    def __init__(self, username=str, userSaber=str):
        self.username = username
        self.userSaber = userSaber

    def getUsername(self):
        """Returns the user name of this User instance

        Returns:
            string: The User instance username
        """
        return self.username

    def getUserSaberAnswer(self):
        """Get the user's saber answer

        Returns:
            int: The saber number
        """
        return self.userSaber
