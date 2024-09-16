#zal = [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]]
zal = [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]]
tickets = int(input("Введите количество билетов:"))

for nrow, row in enumerate(zal):
    tmp = 0
    for place in row:
        if place == 0:
            tmp += 1
        else:
            tmp = 0
        if tmp >= tickets:
            break
    if tmp >= tickets:
        print("Ряд", nrow)
        break
if tmp < tickets:
    print("False")
