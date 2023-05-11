from saberPicker import SaberPicker
from user import User


def pickSequence():
    # task 1
    name = str
    while name == str:
        name = input("What's your name?\n")

    # task 2
    answer = -1
    while answer == -1:
        answer = SaberPicker.pickSaber()

    # task 3
    user = User(name, answer)
    print("You " + user.username + " picked the " +
          SaberPicker.getSaberColor(user.userSaber) + " saber!")


if __name__ == "__main__":
    pickSequence()
