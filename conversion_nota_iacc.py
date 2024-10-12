print('*** Conversión de Puntaje a Nota en IACC ***')
puntaje = float(input('Ingrese su puntaje de IACC' ))
nota = ''
if puntaje == 100: # Puntaje máximo
    nota = 7.0
    print('¡Felicidades por sacar la mejor nota!')
elif 98 <= puntaje < 100:
    nota = 6.9
elif 97 <= puntaje < 98:
    nota = 6.8
elif 96 <= puntaje < 97:
    nota = 6.7
elif 94 <= puntaje < 96:
    nota = 6.6
elif 93 <= puntaje < 94:
    nota = 6.5
elif 92 <= puntaje < 93:
    nota = 6.4
elif 90 <= puntaje < 92:
    nota = 6.3
elif 89 <= puntaje < 90:
    nota = 6.2
elif 88 <= puntaje < 89:
    nota = 6.1
elif 86 <= puntaje < 88:
    nota = 6.0
elif 85 <= puntaje < 86:
    nota = 5.9
elif 84 <= puntaje < 85:
    nota = 5.8
elif 82 <= puntaje < 84:
    nota = 5.7
elif 81 <= puntaje < 82:
    nota = 5.6
elif 80 <= puntaje < 81:
    nota = 5.5
elif 78 <= puntaje < 80:
    nota = 5.4
elif 77 <= puntaje < 78:
    nota = 5.3
elif 76 <= puntaje < 77:
    nota = 5.2
elif 74 <= puntaje < 76:
    nota = 5.1
elif 73 <= puntaje < 74:
    nota = 5.0
elif 72 <= puntaje < 73:
    nota = 4.9
elif 70 <= puntaje < 72:
    nota = 4.8
elif 69 <= puntaje < 70:
    nota = 4.7
elif 68 <= puntaje < 69:
    nota = 4.6
elif 66 <= puntaje < 68:
    nota = 4.5
elif 65 <= puntaje < 66:
    nota = 4.4
elif 64 <= puntaje < 65:
    nota = 4.3
elif 62 <= puntaje < 64:
    nota = 4.2
elif 61 <= puntaje < 62: # Eximido
    nota = 4.1
    print('Si estás en la semana 8 o antes, ¡felicidades por eximirte!')
elif 59 <= puntaje < 61: # Aprobado
    nota = 4.0
    print('¡Felicidades por aprobar! Pero puedes hacerlo mejor la próxima vez')
elif 57 <= puntaje < 59:
    nota = 3.9
elif 55 <= puntaje < 57:
    nota = 3.8
elif 53 <= puntaje < 55:
    nota = 3.7
elif 51 <= puntaje < 53:
    nota = 3.6
elif 49 <= puntaje < 51:
    nota = 3.5
elif 47 <= puntaje < 49:
    nota = 3.4
elif 45 <= puntaje < 47:
    nota = 3.3
elif 43 <= puntaje < 45:
    nota = 3.2
elif 41 <= puntaje < 43:
    nota = 3.1
elif 39 <= puntaje < 41:
    nota = 3.0
elif 37 <= puntaje < 39:
    nota = 2.9
elif 35 <= puntaje < 37:
    nota = 2.8
elif 33 <= puntaje < 35:
    nota = 2.7
elif 31 <= puntaje < 33:
    nota = 2.6
elif 29 <= puntaje < 31:
    nota = 2.5
elif 27 <= puntaje < 29:
    nota = 2.4
elif 25 <= puntaje < 27:
    nota = 2.3
elif 23 <= puntaje < 25:
    nota = 2.2
elif 21 <= puntaje < 23:
    nota = 2.1
elif 19 <= puntaje < 21:
    nota = 2.0
elif 17 <= puntaje < 19:
    nota = 1.9
elif 15 <= puntaje < 17:
    nota = 1.8
elif 13 <= puntaje < 15:
    nota = 1.7
elif 11 <= puntaje < 13:
    nota = 1.6
elif 9 <= puntaje < 11:
    nota = 1.5
elif 7 <= puntaje < 9:
    nota = 1.4
elif 5 <= puntaje < 7:
    nota = 1.3
elif 3 <= puntaje < 5:
    nota = 1.2
elif 1 <= puntaje < 3:
    nota = 1.1
else: # Puntaje fuera de rango
    nota = 'Puntaje fuera de rango, ingresa un puntaje del 1 al 100'

# Entregamos la nota final
print(f'Tu puntaje:{puntaje} te otorga una nota de: {nota}')