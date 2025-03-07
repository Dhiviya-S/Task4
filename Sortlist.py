a=[]
i=int(input("Enter the total numbers of elements in list:"))
for lis in range(i):
    lis=int(input("Enter a list of numbers:"))
    a.append(lis)
print(a)
a.sort()
print("The minimum element in the given list:",a[0])