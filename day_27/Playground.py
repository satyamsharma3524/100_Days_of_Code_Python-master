# unlimited position arguments using *args (collects all the arguments in a tuple)
# def add(*args):
#     return sum(args)

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(2, 3, 4, 5))
