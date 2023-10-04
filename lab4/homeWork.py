# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def test():
    x = 4  # 100
    y = 1  # 001
    a = x & y  # 0   /   0 0 0
    b = x | y  # 5   /   1 0 1
    c = ~x  # -5   /   0b100 -> 1b011
    d = x ^ 5  # 1   /   100 ^ 110 -> 10
    e = x >> 2  # 1   /   100 >> 2 -> 001
    f = x << 2  # 16   /   100 << 2 -> 10000
    print(a, b, c, d, e, f)


if __name__ == '__main__':
    test()
