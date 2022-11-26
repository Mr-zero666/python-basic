def CountHeadsAndLegs(m, n):
    for chicken in range(1,m):
        pig = m-chicken
        if 2*chicken+4*pig == n:
            return chicken, pig

if __name__ == '__main__':
    r = CountHeadsAndLegs(35, 94)
    print(r)
    assert r == (23, 12)
