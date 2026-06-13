tpl = ["Hijbullah", "Rony", "Jabir", "Sazid", "Udoy"]
print(f"1: {tuple(tpl)}")

num = [2,4,3,54,5]
add = sum(num)

print(f"2: Sum- {add}")

t2 = [1,2,3,4,5]
print(f"3:Last Item: {t2[-1]}")

t3 = [1,2,3,4,5,6,7,8,9,10]
print(f"4: Slice to get middle three items: {t3[3:6]}")


T4 = [1,2,3,3,4,5,6,7,8,9,10]
print(f"5: 3 appears in the tuple: {T4.count(3)}")

#Unpacking a tuple into 4 variables

t5 = [1,2,3,4]
a,b,c,d = t5
print(f"6: Unpacked values: {a}, {b}, {c}, {d}")

# A function that returns min and max value without using built-in functions

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
def min_max(lst):
    min_val = lst[0]
    max_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val
min_value, max_value = min_max(lst)
print(f"7: Min value: {min_value}, Max value: {max_value}")

#Store multiple student records using a list of tuples and print only names

students = [("Hijbullah", 20 ), ("Jabir", 21), ("Rony", 22)]
print("8: Student Names:")
for student in students:    
    print(student[0])   
    

#Modify the value:
tpl6 = [1,2,3,4]

tpl6[2] = 4

print(f"9: New Tuple: {tpl6}")

#Dictionary of 5 students:

st = {
    "Hijbullah": 5,
    "Javir" : 6, 
    "Rony" :7
}
print(f"1: {st}")

print(f"2: ")
for key, values in st.items():
    print(f" {key} , {values}")

print(f"3: ")
st["Javir"] = 69
print(st)


print(f"4: Updated Dictionary: ")
st.update({"Udoy" : 33, "Abir" : 34})
print(st)

print(f"5: After Pop and Delete: ")
print(st.pop("Rony"))

ns_ds = {
    "CSE" : {
        "Fisrt": 22,
        "Sec" : 21,
    },
    "BBA" : {
            "First" : 10,
            "Second" : 23,
    }
}

print(f"6: Nestd Dictionary: ")
print(ns_ds)






ch_c = 0

for key in st:
        for ch in key:
             if ch in key:
              ch_c = ch_c + 1
print(f"7: Total Character in the DIctionary: {ch_c}")





