with  open('17.txt') as file:
    data = [int(i) for i in file]

ans = []
for i in range(len(data)-2):
    num1 = data[i]
    num2 = data[i+1]
    num3 = data[i+2]
    u1 = (num1 % 10 == 3) and 100 <= num1 <= 999
    u2 = (num2 % 10 == 3) and 100 <= num2 <= 999
    u3 = (num3 % 10 == 3) and 100 <= num3 <= 999
    if u1 + u2 + u3 >= 1:
        if (num1 + num2 + num3) < max(data):
            ans.append(num1+num2+num3)

print(len(ans), max(ans))

#https://kompege.ru/variant?kim=25089715
