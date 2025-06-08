from string import digits, ascii_uppercase

with open ('24_9791.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase

for i in alph[16:]:
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))