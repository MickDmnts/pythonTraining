import zombieApocalypse

if __name__ == "__main__":
    calc = zombieApocalypse.ZombieCalc()

    # Class info
    print(calc.getDailyMutations().__str__())
    print(calc.getMaxDays().__str__())

    # task 1
    print(calc.totalPop().__str__())

    # task 2
    print(calc.getMutatedUntilDay(28).__str__())

    # task 3
    print(calc.doHumansWin(28).__str__())

    # task 4
    print(calc.daysUntilVirusEradication(28).__str__())
