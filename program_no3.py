try: #the system will try the set of codes under "try". If can't be executed, it will proceed to "except"

    def get_money(): #function for storing the input for the amount of money the user has
        money_input = float( #float is used to enable decimal points because money is the subject
            input("Please enter the amount of money you have: "))
        return money_input

    def get_apple(): #function for storing the input for the price of an apple the user wants to buy
        apple_input = float( #float is used to enable decimal points because money is the subject if talking about price
            input("Please enter the price of an apple that you would like to buy: "))
       
        if(apple_input == 0.0): #restricts user to enter 0.00 priced apples
            print("Sorry, we don't have apples that cost 0.00 pesos.")
            quit() #prompt to terminate the program
        else:
            return apple_input

    def final_output(moneyF, appleF): #function for computation
        max_apple = int(moneyF//appleF) #this is converted to integer data type to avoid decimal places while flashing no. of apples
        change = moneyF % appleF

        print(
            f"You can buy {max_apple} apples and your change is {change:.2f} pesos.") #target final output

    #this will execute the codes inside the functions that were called in order
    money = get_money()
    apple = get_apple()

    if(money < 0 or apple < 0): #restricts the user to enter less than 0 inputs
        print("Error. Less than 0 inputs are invalid.")
    else:
        final_output(money, apple) #prompts the system to execute the final_output function

except ValueError: #this will be executed if the input datatype is incorrect or the input is empty
    print("Invalid input. Please input a number.")
