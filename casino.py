import random
nums_jugador = []
rondas = []

for i in range(7):
    while True:
        try:
            ingreso_jugador = int(input("Ingrese sus numeros de la suerte: "))
            if 1 <= ingreso_jugador <= 49:
                nums_jugador.append(ingreso_jugador)
                break
            else:
                print("Error! El numero ingresado debe ser un numero entero positivo entre 1 y 49")
        except(ValueError):
            print("Solo puede ingresar numeros enteros positivos")

print(f"Usted ingreso los siguientes numeros: {nums_jugador}")

while len(rondas) < 3:
    nums_rondas = [random.randint(1, 49) for _ in range(7)]
    rondas.append(nums_rondas)

ganaste = False
for e in range(3):
    print(f"Los numeros ganadores de la ronda {e + 1} Son: ")
    for u in range (7):
        print(rondas[e][u])
    
    if sorted(nums_jugador) == sorted(rondas[e]):
        ganaste = True
        print("Felicidades has acertado los numeros del gran premio!")
        break
    else:
        print("No has tenido suerte en esta ronda")

if not ganaste:
    print("No hubo suerte esta vez")
print("Muchas gracias por participar")
