"""
Programa: Cálculo del área de un rectángulo
Descripción:
Este programa solicita al usuario el ancho y el alto de un rectángulo,
calcula el área y muestra el resultado.

Se usan tipos de datos:
- float (ancho, alto, área)
- string (nombre_usuario)
- boolean (datos_validos)
- int (intentos)
"""

def calcular_area_rectangulo(ancho: float, alto: float) -> float:
    """
    Calcula el área de un rectángulo.
    Fórmula: área = ancho * alto
    """
    return ancho * alto


def main():
    # String: nombre del usuario
    nombre_usuario: str = input("Ingresa tu nombre: ")

    print(f"\nHola {nombre_usuario}, vamos a calcular el área de un rectángulo 📐")

    # Boolean: para validar datos
    datos_validos: bool = False

    # Int: contador de intentos
    intentos: int = 0
    max_intentos: int = 3

    while not datos_validos and intentos < max_intentos:
        try:
            # Float: medidas del rectángulo
            ancho: float = float(input("\nIngresa el ancho del rectángulo: "))
            alto: float = float(input("Ingresa el alto del rectángulo: "))

            # Validación simple
            if ancho <= 0 or alto <= 0:
                print("❌ Error: El ancho y el alto deben ser mayores que 0.")
                intentos += 1
                continue

            # Si todo está bien, marcamos como válido
            datos_validos = True

            # Calculamos el área
            area: float = calcular_area_rectangulo(ancho, alto)

            # Mostramos el resultado
            print("\n✅ Resultado:")
            print(f"Ancho: {ancho}")
            print(f"Alto: {alto}")
            print(f"Área del rectángulo: {area}")

        except ValueError:
            print("❌ Error: Debes ingresar números válidos (ejemplo: 5 o 2.5).")
            intentos += 1

    if not datos_validos:
        print("\n⚠️ Se agotaron los intentos. Vuelve a ejecutar el programa.")


# Punto de inicio del programa
if __name__ == "__main__":
    main()
