def a_power_b():
    print("Si digita 0 dejara de pedir numeros")
    a=int(input("Pls digite un numero"))
    b=int(input("Pls digite otro numero"))
    while a!=0 or b!=0:
        while True:
            try:
                a=int(input("Pls digite un numero"))
                b=int(input("Pls digite otro numero"))
                z=(a**b)
                print("a:",a,"b:",b,"R:",z)
                break
            except ValueError:
                print("Pls asegurece de digitar un numero")
a_power_b()