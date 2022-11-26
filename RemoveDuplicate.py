def RemoveDuplicate(l):
    a = l
    i = 0
    while i < len(l)-1:
        if a[i] == a[i+1]:
            del a[i]
        else:
            i += 1
    return a

if __name__ == '__main__':
    l = [0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 2, 2]
    r = RemoveDuplicate(l)
    print(r)
    assert r == [0, 1, 2, 3, 4, 5, 6, 2]