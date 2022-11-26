def CompareItems(item):
    min_value = min(item)
    item = sorted(item)
    return item, min_value


def SortEmbedded(l):
    a = []
    for i in range(len(l)):
        if isinstance(l[i], list):
            sort_list, min_value = CompareItems(l[i])
            l[i] = sort_list
            a.append(min_value)
        else:
            a.append(l[i])
    for now in range(len(a)):
        for j in range(now + 1, len(a)):
            if a[now] > a[j]:
                t = l[now]
                l[now] = l[j]
                l[j] = t
    return l


if __name__ == '__main__':
    r = SortEmbedded([1, [13, 12], [6, 5, 7, 8, 9]])
    print(r)
    assert r == [1, [5, 6, 7, 8, 9], [12, 13]]
