#Function

# def great():
#     print("Hello World!")
# great()

# def with_pera(name):
#     print("Hello" , name)

# with_pera("Hijbullah")

# def sum(x, y):
#     print(x+y)

# sum(7,8)

# def multi(a,b):
#     print(a * b)

# multi(3,4)

# def sub(b,c):
#     print(b-c)

# sub(10,3)


# def div(d,e):
#     print(d/e)

# div(10,2)

# def sqr(x):
#     return x * x
# result = sqr(9)
# print(result)
    
# def str(y,z):
#     return y*z
# r = str(2,3)
# print(r)

# *Args
def show(*args):
    print(args)
show(1,3,2,4,5,22)


def total(*num):
    print(sum(num))

total(2,3,4,3,4,5,66)
total(2,3)