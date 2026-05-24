# a=[1,2,-3,4,-5,-6]
# b=[]
# for i in a:
#     i*=-1
#     print(i)
#     b.append(i)
# print(b)


# a=[1,1,2,4,4,3]
# b=[]
# c=0
# for i in a:
#     if i not in b:
#         b.append(i)
#         print(b)
# for i in b:
#     c+=i
#     print(i)




# a=[-1,2,3,-4,-5,-6]
# b=[]
# c=0
# for i in a:
#     if i<0:
#         c+=1
# print(c)

# a=[-1,2,3,-4,-5,-6]
# b=[]
# c=0
# for i in a:
#     if i%2==0:
#         print(i)
#         c+=i
# print(c)

a=[1,2,-3,-4,5,-6]
b=0
c=[]
for i in a:
    if i>-7:
        print(i)
        b+=i
print(b)
c=len(a)
print(b/c)