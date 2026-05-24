while True:
    print("1-summa")
    print("2-riznica")
    print("3-dobutok")
    print("4-casne")
    print("5-faktorial")
    print("6-1/X")
    print("7-stuninj")
    print("8-exit")
    cabuchinoassasino=(int(input("made your choise")))
    if cabuchinoassasino==1:
        a=(int(input("write first number")))
        b=(int(input("write second number")))
        c=a+b
        print(c)
    if cabuchinoassasino==2:
        a=(int(input("write first number")))
        b=(int(input("write second number")))
        c=a-b
        print(c)
    if cabuchinoassasino==3:
        a=(int(input("write first number")))
        b=(int(input("write second number")))
        c=a*b
        print(c)
    if cabuchinoassasino==4:
        a=(int(input("write first number")))
        b=(int(input("write second number")))
        c = a/b
        print(c)
    if cabuchinoassasino == 5:
        uno=(int(input("write first number")))
        resurtat=1
        for i in range(1,uno+1):
          resurtat=resurtat*i
        print(resurtat)
    if cabuchinoassasino==6:
        a=(int(input("write first number")))
        c=1/a
        print(c)

    if cabuchinoassasino==7:
        a=(int(input("write first number")))
        b=(int(input("write second number")))
        c = a**b
        print(c)
