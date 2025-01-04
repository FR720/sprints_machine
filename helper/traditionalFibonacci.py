
def traditionalFibonacci(n):
    fibList = []
    a, b = 0, 1
    for _ in range(n):
        fibList.append(a)
        a, b = b, a + b
    return fibList