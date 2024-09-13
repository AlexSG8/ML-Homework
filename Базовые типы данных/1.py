in_digit = input("Enter 5 digit:")

while len(in_digit) != 5:
    in_digit = input("Enter 5 digit:")

out = int(in_digit[0]+in_digit[3]+in_digit[2]+in_digit[1]+in_digit[-1])

print("Output:", out)
