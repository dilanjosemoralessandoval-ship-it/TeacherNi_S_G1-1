"""
Calculadora Simple - Diklan Jose Morales
Programa que realiza operaciones matemáticas básicas
"""

def suma(a, b):
    """Realiza la suma de dos números"""
    return a + b

def resta(a, b):
    """Realiza la resta de dos números"""
    return a - b

def multiplicacion(a, b):
    """Realiza la multiplicación de dos números"""
    return a * b

def division(a, b):
    """Realiza la división de dos números"""
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

def main():
    """Función principal de la calculadora"""
    print("=" * 40)
    print("   CALCULADORA DE DIKLAN JOSE MORALES")
    print("=" * 40)
    
    while True:
        print("\nOpciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("\nElige una opción (1-5): ").strip()
        
        if opcion == '5':
            print("¡Gracias por usar la calculadora!")
            break
        
        if opcion not in ['1', '2', '3', '4']:
            print("Opción inválida. Intenta de nuevo.")
            continue
        
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                resultado = suma(num1, num2)
                print(f"\n{num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = resta(num1, num2)
                print(f"\n{num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                print(f"\n{num1} × {num2} = {resultado}")
            elif opcion == '4':
                resultado = division(num1, num2)
                print(f"\n{num1} ÷ {num2} = {resultado}")
        
        except ValueError:
            print("Error: Por favor ingresa números válidos.")

if __name__ == "__main__":
    main()
