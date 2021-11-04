def get_name():
    name = input("Please enter you name: ")
    return name

def get_age(): 
    age = input("Please enter your age in years: ")
    return age

def get_address():
    address = input("Please enter your address: ")
    return address

name = get_name()
age = get_age()
address = get_address()

def age_validation():
    try:
        age_int = int(age)

        if(age_int <= 0):
            print("\nInvalid age.")
        else:
            print("\nHi, my name is " + name + ". I am " + age +
                            " years old and I live in " + address + ".")
    
    except ValueError:
        print("\nError. Only whole numbers are accepted for age.")

if(name == "" or age == "" or address == ""):
    print("\nEmpty input is invalid.")
else:
    age_validation()