import random

#Variables principales
lista_de_palabras = ["humanidad","humano","persona","gente","hombre","mujer","niño","adolescente",
                     "adulto","anciano","don", "doña","señor","caballero","dama","individuo"]
vidas = 6
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ",
       "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
seleccionadas = []
incorrectas = []

#Escoger Palabra
def escoger_palabra(lista):
    return random.choice(lista)

palabra_escogida = escoger_palabra(lista_de_palabras)

#Empezar guiones
def palabra_dividida(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra)
    return lista

def determinar_cantidad_de_letras(lista):
    guion = []
    for letra in lista:
        guion.append("_")
    return guion

palabra_dividida_escogida = palabra_dividida(palabra_escogida)
guiones = determinar_cantidad_de_letras(palabra_dividida_escogida)
print(f"La palabra escogida tiene {len(guiones)} letras")

#Adivina
def pedir_letra():
    print(guiones)
    print(f"Lista de incorrectas: {incorrectas}")
    a = "si"
    while a not in abc:
        a = input("Ingresar solo una letra: ").lower()
    return a

def verificar(letra):
    global vidas
    if letra in palabra_dividida_escogida:
        for n in range(len(palabra_dividida_escogida)):
             if palabra_dividida_escogida[n] == letra:
                guiones[n] = letra
        print("La letra sí está en la palabra!")
        seleccionadas.append(letra)
    else:
        print("Esta letra no está en la palabra")
        incorrectas.append(letra)
        seleccionadas.append(letra)
        vidas = vidas - 1
        print(f"Le quedan {vidas} intentos")

while vidas > 0:
    nueva_letra = pedir_letra()
    if nueva_letra in seleccionadas:
        print("Esta letra ya fue seleccionada")
    else:
        verificar(nueva_letra)
    if guiones == palabra_dividida_escogida:
        break
    pass

if vidas > 0:
    print("Ganaste!")
    print(f"La palabra era {palabra_escogida}!!")
else:
    print("Perdiste...")
    print(f"La palabra correcta era {palabra_escogida}")