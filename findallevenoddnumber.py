# Python program to print Even Numbers in given range
a=eval(input("enter the range"))
b=eval(input("enter the range"))

start, end = a,b
print(" number")#
# iterating each number in list
for num in range(start, end + 1):    # checking condition
    if num % 2 == 0:
        print("even number",num, '\n',end=" ")
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print("prime number",num, '\n', end=" ")
for num in range(start, end + 1):
    if  num % 2 != 0:
        print("odd number", num, '\n', end=" ")
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print("prime number", num, '\n', end=" ")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("prime number", num, '\n', end=" ")
            if num % 2 != 0:
                print("odd number", num, '\n', end=" ")
            elif num % 2 == 0:
                print("even number",num, '\n',end=" ")




