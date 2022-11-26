def LeftRotate(l, k):
    new = l[:k]
    new1 = l[k:]
    out = new1 + new
    return out
if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    r = LeftRotate(l, 1)
    print(r)
    assert r == [2, 3, 4, 5, 1]
