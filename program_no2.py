apple_price = 20
orange_price = 25

def get_apples():
    apple_input = int(input("Please enter the number of apples you want to buy: "))
    return apple_input

def get_oranges():    
    orange_input = int(input("Please enter the number of oranges you want to buy: "))
    return orange_input

def finalOutput(applesF, orangesF):
    amount = ((applesF*apple_price) +
                  (orangesF*orange_price))
    print("The total amount is Php" + str(amount) + ".00.")

apples = int(get_apples())
oranges = int(get_oranges())
finalOutput(apples, oranges)