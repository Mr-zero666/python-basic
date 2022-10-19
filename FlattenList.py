def FlattenList( l ):
    new = []
    for i in range(len(l)):
        if isinstance(l[i], list):
            new += l[i]
        else:
            new.append(l[i])
    return new



if __name__=='__main__':
    r = FlattenList( [1, [2], [3,4,5], [6,7], 8] )
    assert r == [1, 2, 3, 4, 5, 6, 7, 8]
