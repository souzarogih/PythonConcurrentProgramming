def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFunII(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFunII(first='Geeks', mid='for', last='Geeks')

# https://www.geeksforgeeks.org/args-kwargs-python/