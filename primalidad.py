def isPrimeNumber(number, i):
    if (i == 1):
        return True
    else:
        if ((number % i) == 0):
            return False
        else:
            return isPrimeNumber(number,i-1)
            
                    
def run():
    number = int(input('Write a number: '))
    isPrime = isPrimeNumber(number,number-1)
    if(isPrime):
        print('The number '+str(number)+ ' is prime')
    else:
        print('The number '+str(number)+ ' is not prime')

if __name__ == "__main__":
    run()