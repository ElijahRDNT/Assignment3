#constant values are placed at the top so it won't be disrupted while editting the whole program
apple_price = 20
orange_price = 25

try: #the system will try the set of codes under "try". If can't be executed, it will proceed to "except"
    def get_apples(): #function for storing the input for the number of apples
        apple_input = int(
            input("Please enter the number of apples you want to buy: "))
        return apple_input

    def get_oranges(): #function for storing the input for the number of oranges
        orange_input = int(
            input("Please enter the number of oranges you want to buy: "))
        return orange_input

    def final_output(applesF, orangesF): #function for computation and printing of target final output
        amount = ((applesF*apple_price) + #no. of apples and oranges are multiplied by their respective prices, then add together to get the total amount
                  (orangesF*orange_price))
        print("The total amount is Php" + str(amount) + ".00.") #this is the target final output

    #signals to execute the functions
    apples = int(get_apples()) #the value that this function holds is converted into an integer type, then stored to apples variable
    oranges = int(get_oranges()) #the value that this function holds is converted into an integer type, then stored to oranges variable

    if(apples < 0 or oranges < 0): #restricts the user to enter less than 0 inputs
        print("Invalid order. Less than 0 inputs are not accepted.")
    else:
        final_output(apples, oranges) #if the input is correct, this prompts the final_output function to be executed

except ValueError: #this is executed if the data type of the input is unacceptable
    print("Error. Please enter whole numbers.")
