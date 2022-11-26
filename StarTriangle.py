def OutputStarTriangle(n):
    for i in range(1, n+1, 1):
        num1 = n - i + 1
        for j in range(1, num1):
            print(" ", end="")
        num2 = 2 * i - 1
        print('*' * num2)

if __name__ == '__main__':
    OutputStarTriangle(5)
