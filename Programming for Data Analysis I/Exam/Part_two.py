from multiples import Multiples
#class Multiples:
    
#    def __init__(self, x=1):
#        self.x = x
#        self.index = 1
    
#    def get_multiple(self, i=1):
#        return self.x*i
    
#    def get_next(self):
#        i = self.index
#        self.index += 1
#        return self.x*i
    
#problem 2.1
def bounded_multiples(x,n):
    less_than = []
    b = Multiples(x)
    c = n // x
    int(c)
    for i in range(c+ 1):
        less_than.append(b.get_multiple(i))
    less_than.pop(0)
    return less_than
    

print(bounded_multiples(6,113))



#problem 2.2
x = int(input('Input X'))
n = int(input('Input N'))
boundmult = bounded_multiples(x,n)
print(boundmult)
