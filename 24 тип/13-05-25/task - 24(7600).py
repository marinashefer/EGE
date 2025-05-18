with open ('24_7600.txt') as file:
    data = file.readline()

data = data.replace('Q', 'S').replace('R', 'S')

while 'SS' in data:
    data = data.replace('SS', 'S S')

data = data.split()
print(len(max(data, key=len)))


#Сборник официальных 24х заданий:
#2022) https://kompege.ru/variant?kim=25099953
#2023) https://kompege.ru/variant?kim=25099956
#2024) https://kompege.ru/variant?kim=25099959
#2025) https://kompege.ru/variant?kim=25099958