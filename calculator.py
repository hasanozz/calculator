import time
import os
import math
from math import exp, log

while True:
    
    ch = input("""
    [1] Addition        [5] Exponentiation      [9]  Percentage
    [2] Substraction    [6] Root                [10] Degree <-> Radians
    [3] Multiply        [7] Factorial           [11] Trigonometric expressions
    [4] Division        [8] Logarithm           [Q]  Quit
    
    """)

    if ch == "Q" or ch == "q":
        print("Exiting...")
        time.sleep(1.4)
        break
    elif ch == "1":
        total = 0
        ctrl = 1
        while ctrl:
            nmbr = input("(Q) Exit || Add: ")
            if nmbr == "Q" or nmbr == "q":
                print(total)
                os.system("pause")
                os.system("cls")
                ctrl = 0
            else:
                nmbr = float(nmbr)
                total += nmbr
                print(total, "\n")


    elif ch == "2":
        total = float(input("Number: "))
        ctrl = 1
        while ctrl:
            nmbr = input("(Q) Exit || Subtract: ")
            if nmbr == "Q" or nmbr == "q":
                print(total)
                os.system("pause")
                os.system("cls")
                ctrl = 0
            else:
                nmbr = float(nmbr)
                total -= nmbr
                print(total, "\n")


    elif ch == "3":
        total = 1
        ctrl = 1
        while ctrl:
            nmbr = input("(Q) Exit || Multiply: ")
            if nmbr == "Q" or nmbr == "q":
                print(total)
                os.system("pause")
                os.system("cls")
                ctrl = 0
            else:
                nmbr = float(nmbr)
                total *= nmbr
                print(total, "\n")


    elif ch == "4":
        total = float(input("Number: "))
        ctrl = 1
        while ctrl:
            nmbr = input("(Q) Exit || Division: ")
            if nmbr == "Q" or nmbr == "q":
                print(total)
                os.system("pause")
                os.system("cls")
                ctrl = 0
            else:
                nmbr = float(nmbr)
                total /= nmbr
                print(total, "\n")

    elif ch == "5":
        base = float(input("Base number: "))
        exponent = float(input("Exponent number: "))
        print("Result = {}".format(base**exponent))
        os.system("pause")
        os.system("cls")

    elif ch == "6":
        radicand = float(input("Radicand number: "))
        index = float(input("Index: "))
        result = exp(log(radicand)/index)
        print("Result = {}".format(result))
        os.system("pause")
        os.system("cls")

    elif ch == "7":
        nmbr = int(input("Number: "))
        result = math.factorial(nmbr)
        print("Result = {}".format(result))
        os.system("pause")
        os.system("cls")

    elif ch == "8":
        ch2 = input("[1] Natural Logarithm(ln)\n[2] Another Value(log)\nChoice: ")
        if ch2 == "1":
            nmbr = float(input("Value: "))
            result = log(nmbr)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")
        elif ch2 == "2":
            base = float(input("Base: "))
            nmbr = float(input("Value: "))
            result = log(nmbr, base)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")
        else:
            print("Wrong Choice.\nPress 'Enter' for back to main menu")
            os.system("pause")
            os.system("cls")

    elif ch == "9":
        nmbr = float(input("Value: "))
        prcnt = float(input("Percent: %"))
        result = (nmbr*prcnt)/100
        print("Result = {}".format(result))
        os.system("pause")
        os.system("cls")

    elif ch == "10":
        ch2 = input("[1] Degree --> Radians\n[2] Radians --> Degree\nChoice: ")
        if ch2 == "1":
            dgr = float(input("Degree: "))
            result = dgr*(3.14159265359/180)
            print("Result = {} radians".format(result))
            os.system("pause")
            os.system("cls")
        elif ch2 == "2":
            rdn = float(input("Radians: "))
            result = rdn*(180/3.14159265359)
            print("Result = {} degree".format(result))
            os.system("pause")
            os.system("cls")
        else:
            print("Wrong Choice.\nPress 'Enter' for back to main menu")
            os.system("pause")
            os.system("cls")

    elif ch == "11":
        os.system("cls")
        ch2 = input("""
        [1] sinus       [6] arcsin
        [2] cosinus     [7] arccos
        [3] tanjant     [8] arctan
        [4] cotanjant   [9] arccot
        [5] sec         [10] cosec
        
        Choice: 
        """)

        if ch2 == "1":
            dgr = float(input("Degree: "))
            dgr = dgr * (math.pi / 180)
            result = math.sin(dgr)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")


        elif ch2 == "2":
            dgr = float(input("Degree: "))
            dgr = dgr * (math.pi / 180)
            result = math.cos(dgr)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        elif ch2 == "3":
            dgr = float(input("Degree: "))
            dgr = dgr * (math.pi / 180)
            result = math.tan(dgr)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        elif ch2 == "4":
            dgr = float(input("Degree: "))
            dgr = dgr * (math.pi / 180)
            result = 1/math.tan(dgr)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        elif ch2 == "5":
            dgr = float(input("Degree: "))
            dgr = dgr * (math.pi / 180)
            result = 1 / math.cos(dgr)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        elif ch2 == "6":
            dgr = float(input("Value: "))
            result = math.asin(dgr)
            result = result*(180/3.14159265359)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        elif ch2 == "7":
            dgr = float(input("Value: "))
            result = math.acos(dgr)
            result = result * (180 / 3.14159265359)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        elif ch2 == "8":
            dgr = float(input("Value: "))
            result = math.atan(dgr)
            result = result * (180 / 3.14159265359)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        elif ch2 == "9":
            dgr = float(input("Value: "))
            result = math.atan(1/dgr)
            result = result * (180 / math.pi)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")


        elif ch2 == "10":
            dgr = float(input("Degree: "))
            dgr = dgr * (math.pi / 180)
            result = 1 / math.sin(dgr)
            print("Result = {}".format(result))
            os.system("pause")
            os.system("cls")

        else:
            print("Wrong Choice.\nPress 'Enter' for back to main menu")
            os.system("pause")
            os.system("cls")

    else:
        print("Wrong Choice.\nPress 'Enter' for back to main menu")
        os.system("pause")
        os.system("cls")