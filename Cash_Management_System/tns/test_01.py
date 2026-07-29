# # print("Multiplication table")
# # n = 8
# # for i in range(1,11):
# #     print(f"{i} x {n} = {i*n}")
        

# print("Grade Calculator: ")

# num = int(input("Enter Your Number: "))

# if num >= 80:
#     print("Congrates, You got A+")
# elif num >=70 and num <=79:
#     print("You got A")
# elif num >= 60  and num <= 69:
#     print("You got A-")
# elif num >= 50 and num <= 59:
#     print("You got B+")
# elif num >= 40 and num <= 49:
#     print("You got B")
# else:
#     print("F")

print("CGPA:")

s1 = float(input("Enter First SM GPA: "))
c1 = float(input("Enter First SM Credit: "))
s2 = float(input("Enter Second SM GPA: "))
c2 = float(input("Enter Second SM Credit: "))
s3 = float(input("Enter Third SM GPA: "))
c3 = float(input("Enter Third SM Credit: "))

cg = ((s1*c1)+(s2*c2)+(s3*c3))/c1+c2+c3

print(cg/3)


# print("Studetn info using Dictionary: ")
# st_ds = {
#     "student_1": {
#         "Name" : "Hijbullah",
#         "Id" : 22303142,
#         "Dept" : "CSE",
#         "CGPA" : 3.67
#     },
#     "student_2": {
#         "Name" : "Hasan",
#         "Id" : 22303140,
#         "Dept" : "CSE",
#         "CGPA" : 3.80
#     },
#     "student_3": {
#         "Name" : "Udoy",
#         "Id" : 22303143,
#         "Dept" : "CSE",
#         "CGPA" : 3.95
#     }

# }

# print(st_ds)
# #Datasets:
 
# #List: List are defined using square brackets: [1, 2, "apple"]. Lists allow duplicate elements and are highly flexible. 
# #Tuple: Like lists, tuples allow duplicates and maintain order, but their contents cannot be changed once defined. They are defined using parentheses: (1, 2, "apple").
# #Set: Sets do not allow duplicates and automatically filter them out. Because they are unordered. They are defined using curly braces: {1, 2, "apple"}.
# #Dictionary: Dictionaries are ordered, do not allow duplicate keys, and are highly efficient for retrieving specific data based on a defined key. They are defined using curly braces with colons separating keys and values: {"name": "Alice", "age": 25}.