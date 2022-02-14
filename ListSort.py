n = int(input("Length of list:"))
up_down = input("Order numbers up or down:")
list1 = []
if up_down == "up":
    for i in range(n):
        data = int(input("Enter numbers:"))
        list1.append(data)
        list1.sort()
elif up_down == "down":
    for i in range(n):
        data = int(input("Enter numbers:"))
        list1.append(data)
        list1.sort(reverse=True)
print(list1)