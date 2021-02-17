def func():
    x = 20

    def funcN():
        # checks for the global variable x (fully outside the nested functions)
        global x
        x = 10  # changes the global x to 10, not the local x of the func() function
        print(x)
    funcN()
    print(x)


func()
print(x)
