# TASK №2


def combine_lists(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        limit = len_a
    else:
        limit = len_b
    i = 0
    r = []
    while i < limit:
        r.append(a[i])
        r.append(b[i])
        i += 1
    return r

if __name__ == '__main__':
    a = ['a', 'b', 'c']
    b = ['A', 'B', 'C', 'D']
    print(repr(combine_lists(a, b)))