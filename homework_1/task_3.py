#TASK №3

def fibonacci(n=10, a=0, b=1):
    yield a
    yield b
    n -= 2
    while n > 0:
        c = a + b
        a = b
        b = c
        yield c
        n -= 1

if __name__ == '__main__':
    for n in fibonacci(100):
        print(n)