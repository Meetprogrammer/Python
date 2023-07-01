"""x = "Meet"

def myfun():
    print("Hey My Name Is: " + x)
    
myfun()"""

"""x = "Meet "

def myfunc():
    y = "Is Fantastic"
    print(x +y)

myfunc()

print(x)"""

def myfunc():
    global x
    x = "Meet"

myfunc()
print("My Name Is "+x)