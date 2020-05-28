import statistics
from number_theory import number_theory_essentials
import math


# from numbertheorylists import *


def partial_sum_for_half_plus_fourth(n):
    result = 0
    for i in range(1, n + 1):
        result = result + 1 / i
    return result


def lucas_lehmer(p):
    s = 4
    m = pow(2, p) - 1
    for i in range(1, p - 1):
        s = (pow(s, 2) - 2) % m
    if s == 0:
        return True, pow(2, p) - 1


def lucas_lehmer_gen(n):
    answer = []
    for j in range(1, n):
        if number_theory_essentials.is_prime(j):
            if lucas_lehmer(j):
                print(j, lucas_lehmer(j))
                n = input("Continue?")
                answer.append(j)
                if "continue" not in n:
                    return answer


# Patterns for modular arithmetic
def pattern_mod_n_adding(n, mod):
    ans = []
    number = n % mod
    new_number = 2 * number
    print(number)
    while number != new_number:
        ans.append(new_number % mod)
        new_number = (number + new_number) % mod
    return ans


def pattern_mod_n_multipling(number, mod):
    x = number % mod
    result = []
    actual = x * x
    while x != actual:
        result.append(actual)
        actual = actual * x
    return result


def pattern_mod_n_multipling_gen(end, start_1, start_2):
    lengths = []
    for i in range(start_1, end):
        print("mod=" + str(i) + ":")
        for dictionary in range(start_2, i):
            print("mod=" + str(i) + " number=" + str(dictionary) + ":")
            print()
            pattern_mod_n_multipling(dictionary, i)
            z = int(len(pattern_mod_n_adding(dictionary, i)))
            print("The length is " + str(z))
            lengths.append(z)
            print(lengths)
    print("The mean is:" + str(statistics.mean(lengths)))
    print("The median is:" + str(statistics.median(lengths)))
    print("The max is:" + str(max(lengths)))
    print("The min is:" + str(min(lengths)))
    dictionary = {"Interquartile_range": str(statistics.median_high(lengths) - statistics.median_low(lengths)),
                  "1st quartile": str(statistics.median_low(lengths)),
                  "Third_quartiles": str(statistics.median_high(lengths)),
                  "mean": float(statistics.mean(lengths)), "median": statistics.median(lengths)}
    return dictionary


def pattern_mod_n_adding_gen(end, start_1, start_2):
    lengths = []
    for mod in range(start_1, end):
        print("mod=" + str(mod) + ":")
        for number in range(start_2, mod):
            print("mod=" + str(mod) + " number=" + str(number) + ":")
            print()
            print(pattern_mod_n_adding(number, mod))
            z = int(len(pattern_mod_n_adding(number, mod)))
            print("The length is " + str(z))
            lengths.append(z)
    print(lengths)
    print("The mean is:" + str(statistics.mean(lengths)))
    print("The median is:" + str(statistics.median(lengths)))
    print("The max is:" + str(max(lengths)))
    print("The min is:" + str(min(lengths)))
    print("Interquartile range:" + str(statistics.median_high(lengths) - statistics.median_low(lengths)))
    dictionary = {"Interquartile_range": str(statistics.median_high(lengths) - statistics.median_low(lengths)),
                  "1st quartile": str(statistics.median_low(lengths)),
                  "Third_quartiles": str(statistics.median_high(lengths)),
                  "mean": float(statistics.mean(lengths)), "median": statistics.median(lengths)}
    return dictionary


# noinspection PyGlobalUndefined,PyGlobalUndefined,PyGlobalUndefined
def pattern_mod_n_analytics_v1(end_1, start_1_1, start_2_1, end_2, start_1_2, start_2_2, the_function):
    global first, last
    if "add" in the_function:
        first = pattern_mod_n_adding_gen(end_1, start_1_1, start_2_1)
        last = pattern_mod_n_adding_gen(end_2, start_1_2, start_2_2)
    elif "multiplication" in the_function:
        first = pattern_mod_n_multipling_gen(end_1, start_1_1, start_2_1)
        last = pattern_mod_n_multipling_gen(end_2, start_1_2, start_2_2)
    for key in first:
        print(key + str(float(last[key]) - float(first[key])))


def addition_sums_mod_n(n):
    x = 0
    for i in range(1, n):
        x = x + i
    return x % n


def addition_sums_mod_n_gen(start, stop):
    for i in range(start, stop):
        print(addition_sums_mod_n(i))
        pass


def patern_mod_n_adding_gen_primes(end, start_1, start_2):
    lengths = []
    for mod in range(start_1, end + 1):
        if number_theory_essentials.is_prime(mod):
            print("mod=" + str(mod) + ":")
            for number in range(start_2, mod):
                print("mod=" + str(mod) + " number=" + str(number) + ":" + str(pattern_mod_n_adding(number, mod)))
                z = int(len(pattern_mod_n_adding(number, mod)))
                print("The length is " + str(z))
                lengths.append(z)
    print(lengths)
    print("The mean is:" + str(statistics.mean(lengths)))
    print("The median is:" + str(statistics.median(lengths)))
    print("The max is:" + str(max(lengths)))
    print("The min is:" + str(min(lengths)))
    print("Interquartile range:" + str(statistics.median_high(lengths) - statistics.median_low(lengths)))
    dictionary = {"Interquartile_range": str(statistics.median_high(lengths) - statistics.median_low(lengths)),
                  "1st quartile": str(statistics.median_low(lengths)),
                  "Third_quartiles": str(statistics.median_high(lengths)),
                  "mean": float(statistics.mean(lengths)), "median": statistics.median(lengths)}
    return dictionary


def prime_mult(n):
    result = 1
    for i in range(2, n):
        result = result * i
    result = result % n
    print(result)


def prime_mult_gen(n):
    for i in range(1, n):
        if number_theory_essentials.is_prime(i):
            prime_mult(i)


def powers_of_x_plus_1_mod_prime(prime, x, p):
    ans = (pow((x + 1), p)) % prime
    return ans


def powers_of_x_plus_1_mod_prime_gen(x, prime, stop_p):
    for p in range(1, stop_p + 1):
        return powers_of_x_plus_1_mod_prime(prime, x, p)


def totient_function_for_1_number(mod):
    for i in range(1, 1000000000):
        if number_theory_essentials.totient_function(i) == mod:
            print(i)


def squares_mod_m(stop, m):
    begining = number_theory_essentials.nth_power(stop, 2)
    ans = []
    for item in begining:
        number = int(item) % m
        ans.append(number)
    return ans


def nth_power_mod_m(stop, m, power):
    beginning = number_theory_essentials.nth_power(stop, power)
    ans = []
    check = 1
    for item in beginning:
        number = int(item) % m
        if check == number and item != 1:
            return ans
        ans.append(number)
    return ans


def distance(mod, number):
    if number != mod:
        ans = [number]
        count = 2
        cont = True
        while cont:
            if (number ** count) % mod != number:
                ans.append((number ** count) % mod)
            else:
                cont = False
                return ans
            count = count + 1
    else:
        pass


def special_exclusion_partition(n, i):
    x = number_theory_essentials.partition(n)
    for item in x:
        if str(i) not in item:
            x.remove(item)
    return x


# def number_of_words(n):
#     end=False
#     ans=0
#     inter=1

def string_function(string):
    zero = 0
    one = 0
    two = 0
    three = 0
    for item in str(string):
        if item == "0":
            zero = zero + 1
        elif item == "1":
            one = one + 1
        elif item == "2":
            two = two + 1
        elif item == "3":
            three = three + 1
    return str(zero) + str(one) + str(two) + str(three)


def primitive_root(n):
    primitive_roots = []
    co_prime_to_n = []
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            co_prime_to_n.append(i)
    for i in range(1, n):
        powers_of_i = []
        for e in range(1, n):
            powers_of_i.append(i ** e % n)
        if sorted(powers_of_i) == co_prime_to_n:
            primitive_roots.append(i)
    print(primitive_roots)


def root_equivalents(modulus, root):
    root_equivalent = []
    for i in range(0, modulus):
        if i ** 2 % modulus == root:
            root_equivalent.append(i)
    print(root_equivalent)


def sum_set_exploration(set_a, set_b):
    # a tool for exploring various sum_sets
    sum_set = []
    for a in set_a:
        for b in set_b:
            sum_set.append(a + b)
    sum_set = set(sum_set)
    return sum_set
