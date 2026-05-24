import random

bombordilocrokodilo=random.randint(1,6)
print(bombordilocrokodilo)
if bombordilocrokodilo==1:
    print("⬛⬜⬜⬜⬜⬜")
elif bombordilocrokodilo==2:
    print("⬛⬛⬜⬜⬜⬜")
elif bombordilocrokodilo==3:
    print("⬛⬛⬛⬜⬜⬜")
elif bombordilocrokodilo==4:
    print("⬛⬛⬛⬛⬜⬜")
elif bombordilocrokodilo==5:
    print("⬛⬛⬛⬛⬛⬜")
elif bombordilocrokodilo==6:
    print("⬛⬛⬛⬛⬛⬛")
oleg=0
oleg2=0
while True:
    bombordinicrokodili=input("will you toss cube")
    if bombordinicrokodili=="ok":
        bombordilocrokodilo = random.randint(1, 6)
        print(bombordilocrokodilo)
        if bombordilocrokodilo == 1:
            print("⬛⬜⬜⬜⬜⬜")
        elif bombordilocrokodilo == 2:
            print("⬛⬛⬜⬜⬜⬜")
        elif bombordilocrokodilo == 3:
            print("⬛⬛⬛⬜⬜⬜")
        elif bombordilocrokodilo == 4:
            print("⬛⬛⬛⬛⬜⬜")
        elif bombordilocrokodilo == 5:
            print("⬛⬛⬛⬛⬛⬜")
        elif bombordilocrokodilo == 6:
            print("⬛⬛⬛⬛⬛⬛")
        oleg=oleg+bombordilocrokodilo
        print("you are in",oleg,"sport")
    if oleg>50:
        print("you win")
        break

    if oleg==20:
        oleg=oleg-3
        print("you lost 3 sports")
        oleg = oleg - 3
    elif oleg==35:
        print("you lost 3 sports")
        oleg = oleg - 3
    elif oleg==40:
        print("you lost 3 sports")
        oleg = oleg - 3
    elif oleg==45:
        print("you lost 3 sports")
        oleg = oleg - 3
    b=input("will you toss cube")
    if b=="ok":
        print()
        bombordilocrokodilo = random.randint(1, 6)
        print(bombordilocrokodilo)
        if bombordilocrokodilo == 1:
            print("⬛⬜⬜⬜⬜⬜")
        elif bombordilocrokodilo == 2:
            print("⬛⬛⬜⬜⬜⬜")
        elif bombordilocrokodilo == 3:
            print("⬛⬛⬛⬜⬜⬜")
        elif bombordilocrokodilo == 4:
            print("⬛⬛⬛⬛⬜⬜")
        elif bombordilocrokodilo == 5:
            print("⬛⬛⬛⬛⬛⬜")
        elif bombordilocrokodilo == 6:
            print("⬛⬛⬛⬛⬛⬛")
        oleg2=oleg2+bombordilocrokodilo
        print("oleg2 are on the sport",oleg2)
        if oleg2>50:
            print("he win")
        if oleg2==20:
            oleg2=oleg2-3
            print("you lost 3 sports")
            oleg2 = oleg2 - 3
        elif oleg2==35:
            print("you lost 3 sports")
            oleg2 = oleg2 - 3
        elif oleg2==40:
            print("you lost 3 sports")
            oleg2 = oleg2 - 3
        elif oleg2==45:
            print("you lost 3 sports")
            oleg2 = oleg2 - 3

