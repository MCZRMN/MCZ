def inteingabe(a, b):
    interger = int(input(f"Input Number between {a} and {b}"))

    return interger, a > interger or b < interger, a, b






interger, error, n1, n2 = inteingabe(50, 100)

print("Number is:", interger)
print(f"The Number should be between {n1} and {n2}")
print("Error:", error)
