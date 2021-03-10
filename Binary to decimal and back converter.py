def binary_calculate():
    binary_number = input("Please enter a binary value to convert to decimal: ")
    for i in binary_number:
        if i == "0":
            continue
        elif i == "1":
            continue
        elif i == "-":
            continue
        else:
            print("You can only enter 0 and 1!")
            check = False
            break
    result = 0
    if int(binary_number)>=0:
        binary_number = list(binary_number)
        binary_number = list(reversed(binary_number))
        for enum, number in enumerate(binary_number):
            result += (int(number) * 2) ** int(enum)
        result -= 1
        decimal_list = []
        decimal_list.append(result)
        reversed(decimal_list)
        for i in decimal_list:
            print(i)
    else:
        binary_number = abs(int(binary_number))
        binary_number = list(str(binary_number))
        binary_number = list(reversed(binary_number))
        for enum, number in enumerate(binary_number):
            result += (int(number) * 2) ** int(enum)
        result -= 1
        decimal_list = []
        decimal_list.append(result)
        reversed(decimal_list)
        for i in decimal_list:
            print("{}{}".format("-", i))
            
        

def decimal_to_binary(num):
    binary_list = []
    if num == 0:
        return num
    elif int(num) > 0:
        while int(num) > 0:
            binary_list.append(int(num) % 2)
            num /= 2
        for i in range(len(binary_list)):
            binary_list[i] = str(binary_list[i])
        return ''.join(reversed(binary_list))
    else:
        while int(abs(num)) > 0:
            binary_list.append(int(abs(num) % 2))
            num = abs(num) / 2
        for i in range(len(binary_list)):
            binary_list[i] = str(binary_list[i])
        return '-' + ''.join(reversed(binary_list))
    

def main():
    ask_user = input("Please enter d to convert decimal to binary or enter b to convert binary to decimal:  ")
    if ask_user == "d" or ask_user == "D":
        binary_calculate()
    elif ask_user == "B" or ask_user == "b":
        decimal_calculate = int(input("Please enter a decimal value to convert to binary: "))
        print(decimal_to_binary(decimal_calculate))
    
    
    
    
main()
    