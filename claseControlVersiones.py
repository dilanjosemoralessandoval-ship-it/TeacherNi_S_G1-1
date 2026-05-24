print("╔══════════════════════════════════════╗")
print("║      CALCULADORA LEGENDARIA 2.0     ║")
print("║           By Dilan Jose             ║")
print("╚══════════════════════════════════════╝")

while True:

    print("\nSeleccione una operación:")
    print("1 ➜ Suma")
    print("2 ➜ Resta")
    print("3 ➜ Multiplicación")
    print("4 ➜ División")
    print("5 ➜ Potencia")
    print("6 ➜ Raíz cuadrada")
    print("7 ➜ Salir")

    opcion = input("\nIngrese una opción: ")

    if opcion == "7":
        print("\nGracias por utilizar la Calculadora Legendaria ✨")
        break

    if opcion == "6":

        numero = float(input("Ingrese un número: "))

        if numero >= 0:
            print("Resultado:", numero ** 0.5)
        else:
            print("No existe raíz cuadrada de números negativos")

        continue

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print("Resultado:", num1 + num2)

    elif opcion == "2":
        print("Resultado:", num1 - num2)

    elif opcion == "3":
        print("Resultado:", num1 * num2)

    elif opcion == "4":

        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Error: División entre cero")

    elif opcion == "5":
        print("Resultado:", num1 ** num2)

    else:
        print("Opción inválida")