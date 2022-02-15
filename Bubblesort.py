list1 = []
listamm = 5

for k in range(listamm):
    data = int(input("Enter 5 numbers:"))
    list1.append(data)

def sort(x):
    l=len(x)
    for i in range(l):
        for j in range((i+1),l):
            if x[i]>x[j]:
                l1=x[i]
                x[i]=x[j]
                x[j]=l1

sort(list1)
print(list1)