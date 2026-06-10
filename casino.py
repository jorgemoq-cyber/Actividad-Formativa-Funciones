import random
nums_jugador = []
rondas = []

for i in range(7):
    ingreso_jugador = int(input("Ingrese sus numeros de la suerte: "))
    nums_jugador.append(ingreso_jugador)
    print(f"Usted ingreso los siguientes numeros: {nums_jugador}")


while len(rondas) < 3:
    nums_rondas = [random.randint(1, 49) for _ in range(7)]
    rondas.append(nums_rondas)

ganaste = False
for e in range(3):
    print(f"Los numeros ganadores de la ronda {e + 1} Son: ")
    for u in range (7):
        print(rondas[e][u])
    
    if nums_jugador == rondas[e]:
        ganaste = True
        print("Felicidades has acertado los numeros del gran premio!")
        break
    else:
        print("No has tenido suerte en esta ronda")

if not ganaste:
    print("No hubo suerte esta vez")
print("Muchas gracias por participar")
