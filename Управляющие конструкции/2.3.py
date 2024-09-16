in_str = input("Введите строку: ")

out_str = ''
p_letter = ''
count = 1

for letter in in_str:
    if letter != p_letter:
        if p_letter:
            out_str += str(count) + p_letter
        count = 1
        p_letter = letter
    else:
        count += 1

out_str += str(count) + p_letter

print(out_str)
