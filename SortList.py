def SortList(lst, order):
    New_list = lst.copy()

    if order == 'asc':
        New_list.sort()
    elif order == 'desc':
        New_list.sort(reverse=True)
    return New_list

if __name__ == '__main__':
    lst = [1, 3, 2, 5, 4]
    l = SortList(lst, 'asc')
    print(l)
    l = SortList(lst, 'desc')
    print(l)
    l = SortList(lst, 'none')
    print(l)