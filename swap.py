def Swap(a, b):
    if isinstance(a,int) and isinstance(b,float):
        a,b = int(b),float(a)
    elif isinstance(a,float) and isinstance(b,int):
        a,b = float(b),int(a)
    return a, b


if __name__ == '__main__':
    x, y = Swap(3., 5)
    print(x, y)
