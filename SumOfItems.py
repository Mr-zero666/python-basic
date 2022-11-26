def SumOfItems(l):
    a = len(l)
    sum = 0
    for item in l:
        if isinstance(item,str):
            sum += float(item)
        else:
            sum += item
    return sum

if __name__ == '__main__':
    r = SumOfItems([1, '234', '456', 670., '91000'])
    print(r)
    assert r == 92361
