# define a basic function

def func1():
    print ("I am a function")


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


#function with default argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# multi add function
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func1()
#func2(10,30)
print(func2(10,23))
power(3)
print (power(3))
print (power(2,4))
print (multi_add())
print (multi_add(2,6,8,78))