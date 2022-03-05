def enclosing():
    x='Closed over'
    def local_func():
        print(x)
    return local_func

lf= enclosing()
# lf()
lf.__closure__


# Function factories
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x,exp)
    return raise_to_exp

square = raise_to(2)
print(square.__closure__)
print(square(5))