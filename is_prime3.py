def is_prime():
    x=0
    n=int(input("Digite un numero"))
    try:
        while n!=0 and n>0:
            n=int(input("Digite un numero"))
            if n%n==0 and n%1==0:
                if n==4:
                    print("Is NOT a prime number")
                if n>3 and n%2==0 or n%3==0 and n!=4:
                    print("Is Not a prime number")
                    print(0)
                    x+=1
                else:
                    print("Is a prime number")
                    print(1)
    except ValueError:
        print(-1)
        return(-1)
is_prime()