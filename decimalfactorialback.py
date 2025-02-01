import math


def dec_2_fact_string(nb):
    pass


def fact_string_2_dec(string):
    comp = []
    n = len(string) - 1
    while n >= 0:
        for i in string:
            d = int(i) * math.factorial(n)
            n -= 1
            comp.append(d)
    print(sum(comp))


fact_string_2_dec("341010")
