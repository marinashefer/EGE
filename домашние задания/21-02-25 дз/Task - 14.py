from string import digits, ascii_lowercase

def convert(num, sys):
    alph = digits + ascii_lowercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

num = 3*3125**9 + 2*625**8 - 4*625**7 + 3*125**6 - 2*25**5 - 2024
num_25 = convert(num, 25)

cnt = 0
for i in range(0, len(num_25)):
    while num_25[i] == 0:
        cnt += 1
        i += 1
    break

print(num_25.count('0') - i)