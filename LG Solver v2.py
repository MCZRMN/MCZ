import numpy as np


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")


def print_matrices(A, B):
    print("Koeffizientenmatrix A:")
    print(A)
    print("Ergebnismatrix B:")
    print(B)


def modify_entry(A, B, n):
    while True:
        choice = input("Möchtest du eine Eingabe ändern? (ja/nein): ").strip().lower()
        if choice == 'ja':
            while True:
                entry_type = input("Was möchtest du ändern? (koeffizient/ergebnis): ").strip().lower()
                if entry_type in ['koeffizient', 'ergebnis']:
                    break
                else:
                    print("Ungültige Eingabe. Bitte antworte mit 'koeffizient' oder 'ergebnis'.")

            if entry_type == 'koeffizient':
                while True:
                    row = input_int(f"Welche Zeile möchtest du ändern? (1-{n}): ") - 1
                    if 0 <= row < n:
                        break
                    else:
                        print(f"Ungültige Zeile. Bitte gib eine Zahl zwischen 1 und {n} ein.")

                while True:
                    col = input_int(f"Welche Spalte möchtest du ändern? (1-{n}): ") - 1
                    if 0 <= col < n:
                        A[row, col] = input_float(f"Neuer Wert für A[{row + 1}][{col + 1}] = ")
                        break
                    else:
                        print(f"Ungültige Spalte. Bitte gib eine Zahl zwischen 1 und {n} ein.")
            elif entry_type == 'ergebnis':
                while True:
                    row = input_int(f"Welches Ergebnis möchtest du ändern? (1-{n}): ") - 1
                    if 0 <= row < n:
                        B[row] = input_float(f"Neuer Wert für B[{row + 1}] = ")
                        break
                    else:
                        print(f"Ungültige Zeile. Bitte gib eine Zahl zwischen 1 und {n} ein.")
        elif choice == 'nein':
            break
        else:
            print("Ungültige Eingabe. Bitte antworte mit 'ja' oder 'nein'.")
        print_matrices(A, B)


def main():
    # Frage nach der Anzahl der Unbekannten
    n = input_int("Wie viele Unbekannte hat das Gleichungssystem? ")

    # Initialisiere die Koeffizientenmatrix A und die Ergebnismatrix B
    A = np.zeros((n, n))
    B = np.zeros(n)

    # Frage die Koeffizienten der Gleichungen ab
    print(f"Gib die Koeffizienten der {n} Gleichungen ein:")
    for i in range(n):
        for j in range(n):
            A[i, j] = input_float(f"A[{i + 1}][{j + 1}] = ")

    # Frage die Ergebnisse der Gleichungen ab
    print("Gib die Ergebnisse der Gleichungen ein:")
    for i in range(n):
        B[i] = input_float(f"B[{i + 1}] = ")

    # Drucke die Matrizen und frage, ob der Benutzer etwas ändern möchte
    print_matrices(A, B)
    modify_entry(A, B, n)

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

