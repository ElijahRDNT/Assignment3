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

print("\nHi, my name is " + name + ". I am " + age +
                " years old and I live in " + address + ".")

