"""
Programa: Generador de Contraseñas Seguras
Materia: Lógica de Programación - UIDE
Estudiante: Briana Abigail Dueñas Granda
Paso 1: Estructura inicial, menú y validación de entradas mediante bucles
"""
#Respuestas que cuentan como "sí" en las preguntas s/n
AFIRMATIVO = ("s", "si", "sí")

def mostrar_menu():
    print("\n🔐 Generador de Contraseñas Seguras")
    print("-----------------------------------")
    print(" 1. Generar nueva contraseña")
    print(" 2. Evaluar fortaleza")
    print(" 3. Salir")
    print("-----------------------------------")

# Valida la respuesta con un bucle while hasta recibir s/si/sí o n/no
def preguntar_si_no(pregunta):
    while True:
        respuesta = input(pregunta).strip().lower()

        if respuesta in AFIRMATIVO:
            return True
        elif respuesta in ("n", "no"):
            return False
        else:
            print("Respuesta inválida. Ingresa s o n.")

def solicitar_parametros():
    # Bucle while para validar que la longitud esté entre 8 y 64 caracteres
    while True:
        entrada = input("\nIngresa la longitud deseada (8 a 64): ").strip()
        # isdecimal() solo acepta dígitos 0-9; 
        if entrada.isdecimal():
            longitud = int(entrada)
            if 8 <= longitud <= 64:
                break
            else:
                print("Error: longitud inválida. Debe estar entre 8 y 64.")
        else:
            print("Error: debes ingresar un número entero.")

    # Bucle while para asegurar que al menos un tipo de carácter sea seleccionado
    while True:
        mayus = preguntar_si_no("¿Incluir mayúsculas? (s/n): ")
        minus = preguntar_si_no("¿Incluir minúsculas? (s/n): ")
        num = preguntar_si_no("¿Incluir números? (s/n): ")
        simb = preguntar_si_no("¿Incluir símbolos? (s/n): ")

        if mayus or minus or num or simb:
            return longitud, mayus, minus, num, simb
        else:
            print("Error: seleccione al menos un tipo de carácter.")


# Función principal (Avance Paso 1)
if __name__ == "__main__":
    # Bucle del menú: se repite hasta que el usuario elige "3. Salir"
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            params = solicitar_parametros()
            print("Parámetros validados correctamente:", params)
        elif opcion == "2":
            print("Evaluación de fortaleza: próximamente.")
        elif opcion == "3":
            print("\nGracias por usar el generador :) \nHasta pronto.")
            break
        else:
            print("Opción inválida. Elige 1, 2 o 3.")
