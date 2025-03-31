with open ('17.txt') as file:
    data = [int(i) for i in file]

ans = []
max_nechet = max(i for i in data if ('0' not in str(i)) and ('2' not in str(i)) and ('4' not in str(i)) and ('6' not in str(i)) and ('8' not in str(i)))
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i+1]
    if num1 + num2 > max_nechet:
        u1 = ('1' not in str(num1)) and ('3' not in str(num1)) and ('5' not in str(num1)) and ('7' not in str(num1)) and ('9' not in str(num1))
        u2 = ('1' not in str(num2)) and ('3' not in str(num2)) and ('5' not in str(num2)) and ('7' not in str(num2)) and ('9' not in str(num2))
        if u1 + u2 >= 1:
            ans.append(num1+num2)

print(len(ans), max(ans))
