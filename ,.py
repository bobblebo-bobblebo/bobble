oleh=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
oleh1=0
oleh2=0
for i in oleh:
    if i>0:
        oleh2 -= 1
        print(oleh2)
        print("this number is for big ")
    if i<0:
        print("number is correct ")
        oleh1-=i
    print(oleh1)
print(oleh1,oleh2)


