# with open ('26_17643.txt') as file:
#     n = int(file.readline())
#     data = [list(map(int, i.split())) for i  in file]
#
# price = sum(data[i][1] for i in range(0, len(data))) // n
#
# ans = []
# cnt = 0
# for i in range(0, len(data)):
#     if data[i][1] > price:
#         if data[i][2] == 1:
#             cnt += 1
#     ans.append([cnt, data[i][0]])
#
# ans = sorted(ans, key=lambda x: ())

with open ('26_17643.txt') as file:
    n = int(file.readline())
    goods = {}
    midd = 0
    length = 0
    for i in file:
        art, price, stat = map(int, i.split())
        midd += price
        length += 1
        if art not in goods:
            goods[art] = [price, 0, 0]
            if stat:
                goods[art][1] += 1
            else:
                goods[art][2] += 1

midd /= length
goods2 = []
for art, info in goods.items():
    if info[0] > midd:
        goods2.append([art, goods[art], True])
    else:
        goods2.append([art, goods[art], False])

goods = sorted(goods2, key=lambda x: (-x[4], -x[3], -x[1], x[2]))
print(goods[0], goods[0][1] * goods[0][3])