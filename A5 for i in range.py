import random
sum = 0
for i in range(0,1000,1):
    r = random.randint(1,6)
    sum = sum + r
print(sum/1000)

