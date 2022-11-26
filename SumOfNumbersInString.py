def SumOfNumbersInString(s):
    b = s.split(" ")
    sum = 0
    for i in range(len(b)):
        if b[i].isnumeric():
            sum += int(b[i])
    return sum

if __name__ == '__main__':
    s = '123 abc 45678 defghijk 1'
    t = SumOfNumbersInString(s)
    print(t)
    assert t == 123 + 45678 + 1