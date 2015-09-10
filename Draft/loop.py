a = [1,2,3,4,7,8,9,11]
b = "hello"
def dealwith(x):
    i = 0
    print x
    print i
    i += 1

map(dealwith,enumerate(b))
