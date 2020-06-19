def factorial(n):
    i = 2
    temp = 1
    while i <= n:
        temp = temp *i
        i = i+1
    return temp

if __name__ == "__main__":    
    a= int(input("ingresa un numero\n"))
    print(factorial(a))
