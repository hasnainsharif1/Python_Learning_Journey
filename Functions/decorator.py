""" Decorator's is basically when you want to add another function into or perform any functionality into the main function  """

def exp_decorator(fun):
    def wrapper():
        print("Before Hasnian")
        fun()
        print("After Hansian")
    return wrapper

@exp_decorator
def fun():
    print("Mid Hasnain.....")

fun()
