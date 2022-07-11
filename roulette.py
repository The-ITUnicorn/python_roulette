import random
totalspins = 0
class Spots:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.hits = 0
#        self.numerator = 1
#        self.denominator = 38
        self.odds = 1/38


    colorRed = ['32', '19', '21', '25', '34', '27', '36', '30', '23', '5', '16', '1', '14', '9', '18', '7', '12', '3']
    colorGreen = ['0', '00']
    colorBlack = ['15', '4', '2', '17', '6', '13', '11', '8', '10', '24', '33', '20', '31', '22', '29', '28', '35', '26']

class Table:
    def __init__(self):
        self.spots = []
        self.spinnumber = 0
        self.greenhits = 0
        self.redhits = 0
        self.blackhits = 0
        self.oddhits = 0
        self.evenhits = 0
        self.zerohits = 0

        for spot in Spots.colorRed:
            color = "red"
            self.spots.append(Spots(spot, color))

        for spot in Spots.colorGreen:
            color = "green"
            self.spots.append(Spots(spot, color))

        for spot in Spots.colorBlack:
            color = "black"
            self.spots.append(Spots(spot, color))



    def spin(self):
        global totalspins
        totalspins += 1
        print("*********************************")
        self.spinnumber += 1
        print("This is spin number: " + str(self.spinnumber))
        self.currentspot = random.choice(self.spots)
        print(self.currentspot.number + " " + self.currentspot.color)
        self.currentspot.hits += 1
        if self.currentspot.color == "red":
            self.redhits += 1
        if self.currentspot.color == "black":
            self.blackhits += 1
        if self.currentspot.number == "0" or self.currentspot.number == "00":
            self.zerohits += 1
        if self.currentspot.number == '1' or self.currentspot.number == '3' or self.currentspot.number == '5' or self.currentspot.number == '7' or self.currentspot.number == '9' or self.currentspot.number == '11' or self.currentspot.number == '13' or self.currentspot.number == '15' or self.currentspot.number == '17' or self.currentspot.number == '19' or self.currentspot.number == '21' or self.currentspot.number == '23' or self.currentspot.number == '25' or self.currentspot.number == '27' or self.currentspot.number == '29' or self.currentspot.number == '31' or self.currentspot.number == '33' or self.currentspot.number == '35':
            self.oddhits += 1
        if self.currentspot.number == '2' or self.currentspot.number == '4' or self.currentspot.number == '6' or self.currentspot.number == '8' or self.currentspot.number == '10' or self.currentspot.number == '12' or self.currentspot.number == '14' or self.currentspot.number == '16' or self.currentspot.number == '18' or self.currentspot.number == '20' or self.currentspot.number == '22' or self.currentspot.number == '24' or self.currentspot.number == '26' or self.currentspot.number == '28' or self.currentspot.number == '30' or self.currentspot.number == '32' or self.currentspot.number == '34' or self.currentspot.number == '36':
            self.evenhits += 1


        self.currentspot.odds -= 1
        #self.currentspot.denominator += 38
        print(self.currentspot.number + " " + self.currentspot.color + " has now hit " + str(self.currentspot.hits) + " times.")
        print("*********************************")
        print("  \n")
        x = 0
        length = len(self.spots)
        for x in range(length):
            self.spots[x].odds += 1/38
            x += 1





###WHERE WE RUN THINGS#####

table = Table()

def ev(oddsToWin, amountTowin, oddsToLose):
    print("This play has an EV of " + str((oddsToWin * amountTowin) + oddsToLose *(-1)))

def manaulAdd(color,number):
    global  totalspins
    print("$$$$$$$$$$$$$$$$$$$MANUAL ADD$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    totalspins += 1
    length = len(table.spots)
    for x in range(length):
        if table.spots[x].color == color and table.spots[x].number == number:
            table.spots[x].hits += 1
    if color == "red":
        table.redhits += 1
    if color == "black":
        table.blackhits += 1
    if number == "0" or number == "00":
        table.zerohits += 1
    if number == '1' or number == '3' or number == '5' or number == '7' or number == '9' or number == '11' or number == '13' or number == '15' or number == '17' or number == '19' or number == '21' or number == '23' or number == '25' or number == '27' or number == '29' or number == '31' or number == '33' or number == '35':
        table.oddhits += 1
    if number == '2' or number == '4' or number == '6' or number == '8' or number == '10' or number == '12' or number == '14' or number == '16' or number == '18' or number == '20' or number == '22' or number == '24' or number == '26' or number == '28' or number == '30' or number == '32' or number == '34' or number == '36':
        table.evenhits += 1

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("  \n")

def straightUpStatus():
    table.spots.sort(key=lambda x: x.odds, reverse=True)
    average = totalspins * 1/38
    average = int(average)
    print("$$$$$$$$$$$$$$$$$$$$ STRAIGHT UP STATUS $$$$$$$$$$$$$$$$$$$$$$$$\n"
          "$$$ With the current number of spins, we would expect to $$$$$$$\n"
          "$$$ see an approximate average of " + str(average) + " hits per number $$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(" ")
    length = len(table.spots)
    for x in range(length):
        print(str(table.spots[x].number) + " " + table.spots[x].color  + " hit a total of " + str(table.spots[x].hits) + " out of " + str(totalspins) + " times.  . We should expect to see this one hit approximately " + str(totalspins/38*2 - table.spots[x].hits)  + " times in the next " +  str(totalspins) + " spins.")
        print("That's a " + str((totalspins/38*2 - table.spots[x].hits) / totalspins * 100) + " percent chance of hitting " + str(table.spots[x].number) + " " + table.spots[x].color)
        currentodds = ((totalspins/38*2 - table.spots[x].hits) / totalspins)
        ev(currentodds, 35, 37/38)
        print("  \n")

def colorStatus():
    average = totalspins * 18/38
    average = int(average)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
          "$$$ With the current number of spins, we would expect to $$$$$$$\n"
          "$$$ see an approximate average of " + str(average) + " hits for red and black $$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$ RED STATUS $$$$$$$$$$$$$$$$$$$$$$$$")
    print("Red has hit " + str(table.redhits) + " times out of " + str(totalspins) + ". We expected to see it hit " + str(totalspins * (18/38)))
    print("We should expect to see Red hit " + str((totalspins*2) * (18/38) - table.redhits) + " times in the next " + str(totalspins) + " spins.")
    print("That's a " + str((((totalspins*2) * (18/38) - table.redhits) / totalspins)*100) + " Percent chance that we hit RED.")
    currentodds = (((totalspins * 2) * (18 / 38) - table.redhits) / totalspins)
    ev(currentodds, 1, 20/38)
    print("$$$$$$$$$$$$$$$$$$$$ BLACK STATUS $$$$$$$$$$$$$$$$$$$$$$$$")
    print("Black has hit " + str(table.blackhits) + " times out of " + str(totalspins) + ". We expected to see it hit " + str(totalspins * (18 / 38)))
    print("We should expect to see Black hit " + str((totalspins*2) * (18/38) - table.blackhits) + " times in the next " + str(totalspins) + " spins.")
    print("That's a " + str((((totalspins * 2) * (18 / 38) - table.blackhits) / totalspins) *100) + " Percent chance that we hit BLACK.")
    currentodds = (((totalspins * 2) * (18 / 38) - table.blackhits) / totalspins)
    ev(currentodds, 1, 20/38)
    print("  \n")

def oddEvenStatus():
    average = totalspins * 18/38
    average = int(average)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
          "$$$ With the current number of spins, we would expect to $$$$$$$\n"
          "$$$ see an approximate average of " + str(average) + " hits for odd and even $$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$ ODD STATUS $$$$$$$$$$$$$$$$$$$$$$$$")
    print("Red has hit " + str(table.oddhits) + " times out of " + str(totalspins) + ". We expected to see odd hit " + str(totalspins * (18/38)))
    print("We should expect to see ODD hit " + str((totalspins*2) * (18/38) - table.oddhits) + " times in the next " + str(totalspins) + " spins.")
    print("That's a " + str((((totalspins*2) * (18/38) - table.oddhits) / totalspins)*100) + " Percent chance that we hit ODD.")
    currentodds = (((totalspins * 2) * (18 / 38) - table.oddhits) / totalspins)
    ev(currentodds, 1, 20/38)
    print("$$$$$$$$$$$$$$$$$$$$ EVEN STATUS $$$$$$$$$$$$$$$$$$$$$$$$")
    print("EVEN has hit " + str(table.evenhits) + " times out of " + str(totalspins) + ". We expected to see it hit " + str(totalspins * (18 / 38)))
    print("We should expect to see EVEN hit " + str((totalspins*2) * (18/38) - table.evenhits) + " times in the next " + str(totalspins) + " spins.")
    print("That's a " + str((((totalspins * 2) * (18 / 38) - table.evenhits) / totalspins) *100) + " Percent chance that we hit EVEN.")
    currentodds = (((totalspins * 2) * (18 / 38) - table.evenhits) / totalspins)
    ev(currentodds, 1, 20/38)
    print("  \n")


option = 0
print(' \n')
print(' \n')
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
      "WELCOME TO THE ROULETTE WHEEL CALCULATOR \n"
      "THIS APP USES MATHEMATICS AND PROBABILITY \n"
      "TO HELP PREDICT THE LIKELIHOOD OF FUTURE \n"
      "OUTCOMES ON THE WHEEL. SOME DEBATE THAT \n"
      "PREVIOUS SPINS HAVE NO IMPACT ON FUTURE \n"
      "SPINS.  HOWEVER, SOME ARGUE THAT THE LAWS \n"
      "OF CUMULATIVE PROBABILITY ARE THE EXACT \n"
      "FORCES THAT ALLOW CA$INO$ TO PREDICT THE \n"
      "ODDS OVER TIME AND MAKE A FORTUNE, WHILE \n"
      "KEEPING THE GAME ATTRACTIVE ENOUGH TO THE \n"
      "GENERAL PUBLIC TO KEEP THEM COMING BACK. \n"
      "EITHER WAY, LET$ MAKE SOME CA$H MOENY! \n"
      "\n"
      "       --APP BY DAMIEN - THE IT-UNICORN\n"
      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
        "___________________________________\n"
        "|#######====================#######|\n"
        "|#(M)*UNITED STATES OF AMERICA*(M)#|\n"
        "|#**          /===\   ********  **#|\n"
        "|*# {G}      | ($) |             #*|\n"
        "|#*  ******  | /v\ |   A MILLI   *#|\n"
        "|#(M)         \===/            (M)#|\n"
        "|##=====ONE MILLION DOLLARS======##|\n"
        "------------------------------------\n"
      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

while option != '9':
    option = input("What would you like to do: \n"
                   "1 = manually add an entry \n"
                   "2 = generate x amount of random spins \n"
                   "3 = get the status of Color Odds \n"
                   "4 = get the status of individual number Odds \n"
                   "5 = get the status of Odd/Even Odds \n"
                   "9 = QUIT the program \n")

    if option == '1':
        color = input("red or black \n")
        color = str(color)
        number = input('what number \n')
        number = str(number)
        manaulAdd(color, number)

    if option == '2':
        spinint = input("how many spins would you like to generate? \n")
        spinint = int(spinint)
        for x in range(spinint):
            table.spin()

    if option == '3':
        colorStatus()

    if option == '4':
        straightUpStatus()

    if option == '5':
        oddEvenStatus()
