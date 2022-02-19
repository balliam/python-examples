list1 = []
listamm = 10
acc_dec = input("Order numbers up or down:")


for k in range(listamm):
    data = int(input("Enter 10 numbers:"))
    list1.append(data)

def sort(x):
    l=len(x)
    for i in range(l):
        for j in range((i+1),l):
            if x[i]>x[j]:
                l1=x[i]
                x[i]=x[j]
                x[j]=l1

def sort_down(x):
    l=len(x)
    for i in range(l):
        for j in range((i+1),l):
            if x[i]<x[j]:
                l1=x[i]
                x[i]=x[j]
                x[j]=l1

if acc_dec == "up":
    sort(list1)
    print(list1)

if acc_dec == "down":
    sort_down(list1)
    print(list1)