num= input('Enter number:')

try:
    float(num)
    if num.find(".") != -1 and num[-1] != ".":
        print("True")
    else:
        print("False")
except ValueError:
    print('False')
