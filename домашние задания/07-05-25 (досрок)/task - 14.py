from string import ascii_lowercase, digits

alph = digits + ascii_lowercase

ans = []
for x in alph[:21]:
    num1 = int(f'82934{x}2', 21)
    num2 = int(f'2924{x}{x}7', 21)
    num3 = int(f'67564{x}8', 21)
    num = num1 + num2 + num3
    if int(num) % 20 == 0:
        ans.append([x, int(num)//20])

print(min(ans))