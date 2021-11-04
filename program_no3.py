money = float(input("Please enter the amount of money you have: "))
apple = float(
        input("Please enter the price of an apple that you would like to buy: "))

max_apple = str(int(money//apple))
change = str(money % apple)

print("You can buy " + max_apple +
              " apples and your change is " + change + " pesos.")