num = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338

count = 0
while num:
    if num % 9 != 0:
        count += 1
    num //= 9

print(count)
