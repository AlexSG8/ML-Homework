s, step = input(), int(input())


result = ""
for char in s:
    if char.isalpha():
        step_base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) + step - step_base) % 26 + step_base)
    else:
        result += char
print(result)
