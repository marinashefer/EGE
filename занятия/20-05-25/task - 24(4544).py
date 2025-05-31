with open ('24_4544.txt') as file:
    data = file.readline()

data = data.replace('101', '10 01') #!

data = data.split()

print(len(max(data, key=len)))

#тема!