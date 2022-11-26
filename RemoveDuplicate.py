def RemoveDuplicate(l):
    comp = None
    out = []
    for x in l:
        if comp is None:
            comp = x
            out.append(x)
        elif comp != x:
            out.append(x)
            comp = x
    return out

if __name__ == '__main__':
    l = [0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 2, 2]
    r = RemoveDuplicate(l)
    print(r)
    assert r == [0, 1, 2, 3, 4, 5, 6, 2]
