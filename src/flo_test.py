import time
import winsound


def flo_addition_test(m1, m2, n):
    print("addition benchmark starts")

    time1 = time.time()
    for i in range(n * n):
        s = m1[i] + m2[i]
    time2 = time.time()
    print(time2 - time1)


def flo_multiplication_test(m1, m2, n):
    print("multiplication benchmark starts")
    time1 = time.time()
    for i in range(n * n):
        s = m1[i] * m2[i]
    time2 = time.time()
    print(time2 - time1)
