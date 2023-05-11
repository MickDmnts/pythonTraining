class SaberPicker:

    def pickSaber():
        """Displays the saber pick sequence sentences

        Returns:
            int: 0-3 saber colors, -1 invalid answer
        """
        answer = -1

        print("0) Prefer negotiation and meditation, strong force abilities")
        print("1) Always angry and wants to destroy EVERYTHING")
        print("2) Jedi Guardians fighting for the light side and are skillful swordsmen")
        print("3) Using Light and Dark side force, doing everything in order to keep the balance.")
        print("4) Exit pick sequence...")

        case = int(input("Select a number...\n"))

        if case >= 0 and case <= 4:
            match case:
                case 0:
                    answer = 0
                case 1:
                    answer = 1
                case 2:
                    answer = 2
                case 3:
                    answer = 3
                case 4:
                    answer = -1
        else:
            print("Invalid answer passed!")
            return -1

        return answer

    def getSaberColor(saberNum=int):
        """Returns the saber color string

        Args:
            saberNum (int): The int saber representation the user picked.

        Returns:
            str: Green, Red, Blue, Purple, Invalid saber number
        """
        answer = str
        match saberNum:
            case 0:
                answer = "Green"
            case 1:
                answer = "Red"
            case 2:
                answer = "Blue"
            case 3:
                answer = "Purple"
            case default:
                answer = "Invalid saber number!"

        return answer
