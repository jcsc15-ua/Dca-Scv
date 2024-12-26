# main.py (introducir fallo)
def suma(a, b):
    return a - b  # ERROR: Lógica incorrecta

if __name__ == "__main__":
    print(suma(2, 3))  # Esto imprimirá -1, no 5
