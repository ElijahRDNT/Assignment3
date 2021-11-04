def get_money():
    money_input = float(
        input("Please enter the amount of money you have: "))
    return money_input

def get_apple():
    apple_input = float(
        input("Please enter the price of an apple that you would like to buy: "))
    return apple_input

def final_output(moneyF, appleF):
    max_apple = int(moneyF//appleF)
    change = moneyF % appleF

    print(f"You can buy {max_apple} apples and your change is {change:.2f} pesos.")

money = get_money()
apple = get_apple()
final_output(money, apple)