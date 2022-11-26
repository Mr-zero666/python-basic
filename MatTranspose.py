def MatTranspose(m):
    """
    *:将可迭代对象拆解出来
    zip:将每列原始组合成元组
    map:将每个元组转为list
    """

    return list(map(list,zip(*m)))




if __name__ == '__main__':
    r = MatTranspose([[1, 2, 3], [4, 5, 6]])
    print(r)
    assert r == [[1, 4], [2, 5], [3, 6]]