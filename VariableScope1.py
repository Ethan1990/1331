var = 'foo'

def ex2():
    var = 'bar'
    print ('inside the function var is ', var)

ex2()

def ex3():
    global var
    var = 'bar'
    print ('inside the function var is ', var)

ex3()
print ('outside the function var is ', var)
