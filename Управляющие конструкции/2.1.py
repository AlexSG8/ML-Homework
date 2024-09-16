num=input()

while len(num) > 1:
    num_=0
    for i in range(len(num)):
        num_+=int(num[i])
    num=str(num_)
print(num)
