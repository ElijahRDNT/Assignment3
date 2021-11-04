apple_price = 20
orange_price = 25

try:
    def get_apples():
        apple_input = int(
            input("Please enter the number of apples you want to buy: "))
        return apple_input

    def get_oranges():
        orange_input = int(
            input("Please enter the number of oranges you want to buy: "))
        return orange_input

    def finalOutput(applesF, orangesF):
        amount = ((applesF*apple_price) +
                  (orangesF*orange_price))
        print("The total amount is Php" + str(amount) + ".00.")

    apples = int(get_apples())
    oranges = int(get_oranges())

    if(apples < 0 or oranges < 0):
        print("Invalid order. Less than 0 inputs are not accepted.")
    else:
        finalOutput(apples, oranges)

except ValueError:
    print("Error. Please enter whole numbers.")
