import bisect

# Límite inferior de cada rango de puntaje
rangos_puntaje = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 100]
# Notas asociadas a cada rango de puntaje
notas = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0]

while True:
    print('*** Conversión de Puntaje a Nota en IACC ***')
    puntaje = float(input('Ingrese su puntaje de IACC: '))

    # Encontrar el índice del rango correspondiente
    if 1 <= puntaje <= 100:
        indice = bisect.bisect_left(rangos_puntaje, puntaje)
        nota = notas[indice]
        print(f'Tu puntaje: {puntaje} te otorga una nota de: {nota}')
    else:
        print('Puntaje fuera de rango, ingresa un puntaje del 1 al 100')

    respuesta = input("\n¿Deseas comprobar otro puntaje? (s/n): ").lower()
    if respuesta != 's':
        print("Gracias por usar el conversor de puntajes. ¡Hasta luego!")
        break
    print()
