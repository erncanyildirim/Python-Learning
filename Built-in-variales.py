# local, enclosing, global, built-in variables

x = "Global x"

def fonk():
    x = "Local x"
    print(x)

#fonk()
#print(x)

def outer():
    x = "Enclosing x"
    print(x)
    def inner():
        x = "Local x"
        print(x)
    inner()

print(x)
outer()
