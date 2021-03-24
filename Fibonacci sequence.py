def to_the_n():
    maximum_number = "n"
    while maximum_number.isnumeric() != True:
        if maximum_number.isnumeric() == False:
            maximum_number = input("Please enter the maximum number: ")
            continue
        else:
            break
    if maximum_number.isnumeric() == True:
        sequence_storage = [1, 1]
        while maximum_number.isnumeric() == True:
            sequence_storage.append(sequence_storage[-2] + sequence_storage[-1])
            if len(sequence_storage) >= int(maximum_number):
                break
            else:
                continue
        print(sequence_storage)
    else:
        pass

def check_integer():
    maximum_number = "Wrong"
    while maximum_number.isnumeric() != True:
        if maximum_number.isnumeric()== False:
            maximum_number = input("In order to generate the Fibonacci sequence to that number enter a number, if to the Nth number enter n: ")
            if maximum_number == "n" or maximum_number == "N":
                to_the_n()
                break
            continue
        else:
            break
    if maximum_number.isnumeric() == True:
        sequence_storage = [1, 1]
        while maximum_number.isnumeric() == True:
            sequence_storage.append(sequence_storage[-2] + sequence_storage[-1])
            if sequence_storage[-1] >= int(maximum_number):
                break
            else:
                continue
        print(sequence_storage)
    else:
        pass

def main_program():
    check_integer()
    user_ask = "Wrong"
    while user_ask not in ["y", "Y", "n", "N"]:
        if user_ask not in ["y", "Y", "n", "N"]:
            user_ask = input("\n\nWould you like to use it again?\nN for no, Y for yes: ")
            continue
    if user_ask == "y" or user_ask == "Y":
        main_program()
    elif user_ask == "N" or user_ask == "n":
        print("Thanks for using my program!")
    else:
        print("Unknown error!")
main_program()