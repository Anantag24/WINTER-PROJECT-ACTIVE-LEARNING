def f(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    f = [0, 1]
    for i in range(2, n):
        f.append(f[-1] + f[-2])
    return f

print(f(10))