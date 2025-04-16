def f1(arr):
    return max(arr) < sum(arr) - max(arr)

def f2(arr):
    u1 = arr[0] == arr[1]
    u2 = arr[0] == arr[2]
    u3 = arr[0] == arr[3]
    u4 = arr[1] == arr[2]
    u5 = arr[1] == arr[3]
    u6 = arr[2] == arr[3]
    if u1 + u2 + u3 + u4 + u5 + u6 == 1:
        return True
    return False

#def f2(arr):
#    return len(set(arr)) + 1 == len(arr)

#def f2(arr):
#    cnt = [arr.count(i) for i in arr]
#    return cnt.count(2) == 2 and cnt.count(1) == 2

with open('9_4614.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)