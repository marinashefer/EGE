from string import digits, ascii_lowercase
alph = digits + ascii_lowercase

ans = []
for x in alph[:25]:
    num1 = int(f'A4{x}7F2', 25)
    num2 = int(f'N{x}G5{x}H', 25)
    num3 = int(f'74{x}M26', 25)
    num = num1 + num2 + num3
    if num % 24 == 0:
        ans.append([x, num // 24])

print(max(ans))