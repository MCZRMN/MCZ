# Input numbers from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Find the maximum of the two numbers
max_num = max(x, y)

# Start with the greater of the two numbers as the potential LCM
lcm = max_num

# Keep incrementing the potential LCM until it is divisible by both numbers
while lcm % x != 0 or lcm % y != 0:
    lcm += max_num

# Print the least common multiple
print("The least common multiple of", x, "and", y, "is:", lcm)
