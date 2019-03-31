def a_power_b():
    x=1
    lel=0
    lil=0
    kua=0
    print("Si digita 0 dejara de pedir numeros")
    a=int(input("Pls digite un numero"))
    b=int(input("Pls digite otro numero"))
    if a%2==0 or b%2==0:
        lel+=1
    else:
        lil+=1
    while a!=0 or b!=0:
        while True:
            try:
                a=int(input("Pls digite un numero"))
                b=int(input("Pls digite otro numero"))
                z=(a**b)
                print("a:",a,"b:",b,"R:",z)
                x+=2
                if a%2==0 or b%2==0:
                    lel+=1
                else:
                    lil+=1
                break
            except ValueError:
                print("Pls asegurece de digitar un numero")
                kua+=1
    print("Numeros digitados:",x,"Numeros pares:",lel,"Numeros impares:",lil,"Errores de digitación:",kua)
a_power_b()