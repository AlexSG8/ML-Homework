import re

def converter(in_str):
    if in_str.find("_") == -1:
        return (re.sub('([a-z])([A-Z])', r'\1_\2', in_str)).lower()
    else:
        words = in_str.split('_')
        return ''.join(x.title() for x in words[0:])

sss = input("Введите строку: ")
print(converter(sss))
