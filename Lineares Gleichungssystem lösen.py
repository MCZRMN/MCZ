import numpy as np


def main():
    # Frage nach der Anzahl der Unbekannten
    n = int(input("Wie viele Unbekannte hat das Gleichungssystem? "))

    # Initialisiere die Koeffizientenmatrix A und die Ergebnismatrix B
    A = np.zeros((n, n))
    B = np.zeros(n)

    # Frage die Koeffizienten der Gleichungen ab
    print(f"Gib die Koeffizienten der {n} Gleichungen ein:")
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"A[{i + 1}][{j + 1}] = "))

    # Frage die Ergebnisse der Gleichungen ab
    print("Gib die Ergebnisse der Gleichungen ein:")
    for i in range(n):
        B[i] = float(input(f"B[{i + 1}] = "))

    # Löse das lineare Gleichungssystem
    try:
        X = np.linalg.solve(A, B)
        # Drucke die Lösung
        print("Die Lösung des linearen Gleichungssystems ist:")
        for i in range(n):
            print(f"x{i + 1} = {X[i]}")
    except np.linalg.LinAlgError as e:
        print(f"Fehler beim Lösen des Gleichungssystems: {e}")


if __name__ == "__main__":
    main()
