#A1 (1) Fakultät

x = int(input("Zahl eingeben"))
list = []
while x != 1:
    list.append(x)
    x -= 1
list.append(1)

product = 1
for x in list:
    product *= x
print(product)