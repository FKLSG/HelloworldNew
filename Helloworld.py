x=10
if (x>9):
    print ("big number")
else:
    print ("small number")
y = range (5,10,1)
print y


def func(x):
    x = x+1
    print "X = ", x

func(3)
func(4)

def make_incrementor(n):
    return lambda x: x +n

f = make_incrementor(40)
print f(2)



