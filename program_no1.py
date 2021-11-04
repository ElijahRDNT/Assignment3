def get_name(): #function for storing the name input
    name = input("Please enter you name: ")
    return name

def get_age(): #function for storing the age input
    age = input("Please enter your age in years: ")
    return age

def get_address(): #function for storing the address input
    address = input("Please enter your address: ")
    return address

#this will execute the codes inside the functions that were called in order
name = get_name()
age = get_age()
address = get_address()

def age_validation(): #this function contains validation for age input such as the data type or value
    try: #the system will try the set of codes under "try". If can't be executed, it will proceed to "except"
        age_int = int(age)

        if(age_int <= 0): #age input that is less than or equal to zero is invalid
            print("\nInvalid age.")
        else:
            print("\nHi, my name is " + name + ". I am " + age + #this is the final output if the inputs are acceptable
                            " years old and I live in " + address + ".")
    
    except ValueError: #this will most likely be executed if the age can't be converted into an integer type (ex. if the input is in letters)
        print("\nError. Only whole numbers are accepted for age.")

if(name == "" or age == "" or address == ""): #empty inputs are also restricted
    print("\nEmpty input is invalid.")
else:
    age_validation() #this prompts the system to execute the codes under age_validation function