empty = []
lst = [1,2,3,4,5,6,6]
for i in lst:
    if i not in empty:
        empty.append(i)
lst.clear()
print(empty)
        