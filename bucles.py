def run():
    resultado = 0
    LIMITE = int(input('Ingrese el límite: '))
    potencia = 0 
    while resultado < LIMITE:
        resultado = 2**potencia
        print("Dos elevelado a "+str(potencia)+" es igual a "+str(resultado))
        potencia = potencia+1

    


if __name__ == "__main__":
    run()