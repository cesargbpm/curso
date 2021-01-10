menu = """
Welcome to the exchange tool!
Plese choose an option 
1. COP
2. ARG
3. MXN
"""
option = int(input(menu))

if option == 1:
    pesos = input("How much COP do you have? ")
    pesos = float(pesos)
    dolar = 3875
    dolares = pesos/dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("You have $"+dolares+" USD")
elif option == 2:
    pesos = input("How much ARG do you have? ")
    pesos = float(pesos)
    dolar = 65
    dolares = pesos/dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("You have $"+dolares+" USD")
elif option == 3:
    pesos = input("How much MXN do you have? ")
    pesos = float(pesos)
    dolar = 24
    dolares = pesos/dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("You have $"+dolares+" USD")
else:
    print("Choose a valid option!")

