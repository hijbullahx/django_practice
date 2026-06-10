arr = ["A", "B", 2,3,4,4,4,4,4,5,"C", "A", "A"]

x = arr[2]
print(arr)
print(arr[1])
print(x)

arr.append(2)
print(arr)

arr_ex = [1,8,9]

arr_c = arr.copy()

arr.clear()
print(arr)
print(f"Copy of the previous array: {arr_c}")
 
print(arr_c.count("A"))
print(arr_c.count(4))
arr_c.extend(arr_ex) 
print((arr_c))

#reverse() Reverse the order of the list.
arr_c.reverse()
print(arr_c)


print(arr_c.index(9))

arr_c.insert(3, 69)
print(arr_c)

#pop() Remove the element at the specified position
arr_c.pop(1)
print(arr_c)

#remove() Removes the first item with the specified value
arr_c.remove("A")
print(arr_c)

#sort() Sorts the list

arr_int = [1,2,3,44,5,0,2]
arr_int.sort()
print(arr_int)

arr_ch = ["B", "A", "C"]
arr_ch.sort()
print(arr_ch)