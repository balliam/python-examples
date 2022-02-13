print("Print 10 numbers and press enter. Once done press q to exit: ")
list1 = []

while True:
    data = input()
    if str.lower(data) == "q":
        break
    list1.append(data)

print(list1.sort())
