def add(a, b):
    return a+b

    
class test:

    
    def __init__(self, addfunction):
        self.addfunction = addfunction
        
    def fuck(x, y):
        return x*y
    
f = test(addfunction = add)

print(f.addfunction(1,2))
print(test.fuck(5,7))