# def add():
#     a=int(input("Enter the value of a"))
#     b=int(input("Enter the valure of b"))
#     print(a+b)
#
#
# add()
#
# def add(a,b):
#     print(a+b)
#
#
# add(4,2)
# global Test t



def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("REcu")
tri_recursion(6)
