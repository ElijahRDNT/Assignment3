apple_price = 20
orange_price = 25

apples = int(input("Please enter the number of apples you want to buy: "))
oranges = int(input("Please enter the number of oranges you want to buy: "))

total_amount = str((apples*apple_price) +
                           (oranges*orange_price))

print("The total amount is " + total_amount + ".")