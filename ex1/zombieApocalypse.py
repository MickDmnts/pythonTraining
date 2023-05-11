class ZombieCalc:

    dailyMutations = -1
    maxDays = -1
    antidotesPerDay = -1

    def __init__(self, dailyMutations=25000, maxDays=100, antidotesPerDay=20000) -> None:
        self.dailyMutations = dailyMutations
        self.maxDays = maxDays
        self.antidotesPerDay = antidotesPerDay

    def getDailyMutations(self):
        """Returns the daily number of mutated people

        Returns:
            int: Daily number of mutated people
        """
        return self.dailyMutations

    def getMaxDays(self):
        """Returns the max days until the city is fully mutated

        Returns:
            int: Max days until the city is fully mutated
        """
        return self.maxDays

    def totalPop(self):
        """Returns the total city population.

        Returns:
            int: Total city population
        """
        return self.dailyMutations * self.maxDays

    def getMutatedUntilDay(self, day=int):
        """Returns the total mutated population until the passed day

        Args:
            day (int): Days to calculate infected people for

        Returns:
            int: Total mutated population
        """
        return self.getDailyMutations() * day

    def doHumansWin(self, fightDay=int):
        """Will the remaining humans win in the passed fightDay?

        Args:
            fightDay (int): The day of the fight in int (0-100). Defaults to int.

        Returns:
            bool: True if humans win, false otherwise.
        """
        mutated = self.getMutatedUntilDay(fightDay)
        healthy = self.totalPop() - mutated
        return healthy > mutated

    def daysUntilVirusEradication(self, antidoteStartingDay=int):
        """How many days would the virus have been eradicated?

        Args:
            antidoteStartingDay (int): Starting day of antidote distribution. Defaults to int.

        Returns:
            int: Days until the virus gets eradicated.
        """
        return self.getMutatedUntilDay(antidoteStartingDay) / self.antidotesPerDay
