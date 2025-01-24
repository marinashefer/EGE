from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

ans = []
for x in alph[:22]:
    num1 = int(f'A23{x}ACO', 22)
    num2 = int(f'GB{x}21670', 22)
    num = num1 + num2
    if num % 21:
        ans.append(x)
        print(max(ans))

