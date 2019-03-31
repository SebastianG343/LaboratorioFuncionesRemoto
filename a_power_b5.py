def is_prime():
    n=int(input("Digite un numero"))
    if n%n==0 and n%1==0:
        if n==4:
            print("Is NOT a prime number")
        if n>3 and n%2==0 or n%3==0 and n!=4:
            print("Is Not a prime number")
        else:
            print("Is a prime number")
is_prime()