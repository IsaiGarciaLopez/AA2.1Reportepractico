import random

pregunta = input('pregunta:     ')

numero_aleatorio = random.randint(1, 9)

if numero_aleatorio == 1:
    respuesta = 'si - definiticamente'
elif numero_aleatorio == 2:
    respuesta = 'esta decidido'
elif numero_aleatorio == 3:
    respuesta = 'sin duda'
elif numero_aleatorio == 4:
    respuesta = 'respuesta confunsa. intenta de nuevo'
elif numero_aleatorio == 5:
    respuesta = 'pregunta mas tarde'
elif numero_aleatorio == 6:
    respuesta = 'mejor no te lo digo'
elif numero_aleatorio == 7:
    respuesta = 'mis fuentes dicen que no'
elif numero_aleatorio == 8:
    respuesta = 'no me parece bueno'
elif numero_aleatorio == 9:
    respuesta = 'muy dudoso'
else:
    respuesta = 'error'

print('bola magica:   ' + respuesta)