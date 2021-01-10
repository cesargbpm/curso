def palindromo(palabra):
    validacion = palabra.replace(' ','').upper()[::-1]
    
    if (validacion == palabra.upper()):
        return True
    else:
        False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if(es_palindromo == True):
        print('Es Palindromo')
    else:
        print('No es palindromo')


if __name__ == "__main__":
    run()