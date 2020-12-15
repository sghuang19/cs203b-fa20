import time


def flo_test(m1, m2, n):
    print("benchmark starts")

    time1 = time.time()
    for i in range(n * n):
        s = m1[i] + m2[i]
    time2 = time.time()
    alpha = time2 - time1
    print(time2 - time1)

    time1 = time.time()
    for i in range(n * n):
        s = m1[i] * m2[i]
    time2 = time.time()
    pi = time2 - time1
    print(time2 - time1)

    print("the ratio of alpha and pi is ", pi / alpha)
