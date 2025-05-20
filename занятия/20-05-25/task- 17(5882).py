with open ('17_5882.txt') as file:
    data= [int(i) for i in file]

ans = []
for i in range(len(data)-1):
    num1 = data[i]
    num2 = data[i+1]
    u1 = str(num1)[-1] == '3'
    u2 = str(num2)[-1] == '3'
    if u1 + u2 == 1:
        ans.append(min(num1, num2))

ans2 = abs(min(ans))
num = sum([int(i)**2 for i in str(ans2)])

ans3 = []
for i in range(len(data)):
    if '3' in str(data[i]):
        if data[i] >= num:
            ans3.append(data[i])

print(len(ans3), min(ans3))