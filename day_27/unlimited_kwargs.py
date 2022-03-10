# unlimited position arguments using **kwargs (collects all the keyword arguments in a tuple)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=5, multiply=7)
