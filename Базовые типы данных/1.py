print("Enter 5 digit:")
in_digit = input()

while len(in_digit) != 5:
    print("Enter 5 digit:")
    in_digit = input()

out = int(in_digit[0]+in_digit[3]+in_digit[2]+in_digit[1]+in_digit[-1])

print("Output:", out)
