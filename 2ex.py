stack = []
array2 = []
array = ["A", "B", "C", "D", "E", "F"]
print(array)

while array:
    array2.append(array.pop())
print(array2)

while array2:
    stack.append(array2.pop(0))