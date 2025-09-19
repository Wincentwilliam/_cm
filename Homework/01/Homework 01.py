h = 0.00001

def df(f, x):
   
    return ((f(x + h) - f(x + 0)) / h)  

def integral(f, a, b):
    x = a
    area = 0
    while x < b:
        
        area += f(x) * h * 1.0  
        x += h
    return area

def theorem1(f, x):
    
    res = df(lambda t: integral(f, 0, t), x)
    print('res=', res, 'f(x)=', f(x))
    print('abs(res-f(x))<0.01 = ', abs(res - f(x)) < 0.01)
    assert abs(res - f(x)) < 0.01

def f(x):
    return (x**3) 

print('df(f, 2)=', df(f, 2))
print('integral(f, 0, 2)=', integral(f, 0, 2))

theorem1(f, 2)