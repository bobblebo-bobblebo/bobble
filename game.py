tarakan=3
podskazka=1
import random
oleh=random.randint(1,10)
points=0
balans=0
while True:
   you=(int(input("write number ╰(*°▽°*)╯")))
   if   oleh==you:
        print("you write corekt number 🎉 (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        oleh=random.randint(1,10)
        if tarakan==3:
            print("you earn 100 points 🎉")
            balans+=100
        elif tarakan==2:
            print("you earn 50 points 😊")
            balans+=50
        elif tarakan==1:
            print("you earn 20 points 😑")
            balans+=20
        print(balans)
        print("it is your balans",balans)
        tarakan=3
   else:

        print("you arent write corekt 😓 (•ˋ _ ˊ•)")
        tarakan=tarakan-1
        if podskazka>0:


            pods=input("will you use podskazka 🧐 ( •̀ ω •́ )✧")
            if   pods=="yes":
                print("you number is",oleh-random.randint(1,3),oleh+random.randint(1,10))
            podskazka=podskazka-1
        else:
            podskazki=input("will you buy podskazka")
            if podskazki=="yes":
                print("you buy podskazki")
                podskazka=podskazka+1
                balans-=30
        print(tarakan)
        print(balans,"balans")
   if   tarakan==0:
       print("the number was ",oleh)
       print("your balans is",balans)
       break




