import function
import itertools
from math import *
from function import *


def totient_fuction(m, print_units):
    units = []
    for i in range(1, m):
        if gcd(i, m) == 1:
            units.append(i)
    ans = len(units)
    if not print_units:
        return ans
    else:
        return ans, units


def partition(n):
    partitions = []
    l = ""
    for i in range(1, n + 1):
        l += str(i)
    for i in range(1, n + 1):
        comb = itertools.product(l, repeat=i)
        for element in comb:
            z = 0
            for character in element:
                z += int(character)
            if z == n:
                new_part = []
                for e in element:
                    new_part.append(int(e))
                if sorted(new_part) not in partitions:
                    partitions.append(new_part)
    return partitions


def C(n, k):
    num = factorial(n)
    den = factorial(n - k) * factorial(k)
    return num / den

def P(n, k):
    num = factorial(n)
    den = factorial(n - k)
    return num / den

def generate_combinations(string, r):
    if r == 1:
        n = []
        for element in string:
            n.append(element)
    else:
        n = []
        for i in range(0, len(string)):
            str_removed = string[:i] + string[i+1:]
            comb_next_iteration = generate_combinations(str_removed, r - 1)
            for element in comb_next_iteration:
                l = string[i] + element
                s = []
                f = list(l)
                f.sort()
                f = "".join(f)
                if f not in n:
                    n.append(l)
    return n

def generate_permutations(string, r):
    if r == 1:
        perms = []
        for element in string:
            perms.append(element)
    else:
        perms = []
        for i in range(0, len(string)):
            str_removed = string[:i] + string[i+1:]
            comb_next_iteration = generate_permutations(str_removed, r - 1)
            for element in comb_next_iteration:
                perms.append(string[i] + element)
    return perms

def generate_cyclic_permutations(string):
    perm = generate_permutations(string, len(string))
    cyclic_permutations = []
    for permutation in perm:
        if cyclic_permutations != []:
            is_equal = False
            for cyclic_permutation in cyclic_permutations:
                for i in range(len(cyclic_permutation)):
                    cyclic_permutation = cyclic_permutation[1:] + cyclic_permutation[0]
                    if permutation == cyclic_permutation:
                        is_equal = True    
            if is_equal == False and permutation not in cyclic_permutations:
                cyclic_permutations.append(permutation)
        else:
            cyclic_permutations.append(permutation)
    return cyclic_permutations

def multiset_P(multiset_of_strings):
    den = 1
    elements = []
    for element in multiset_of_strings:
        if element not in elements:
            elements.append(element)
            count_of_element = multiset_of_strings.count(element)
            den *= factorial(count_of_element)
    num = factorial(len([e for e in multiset_of_strings]))
    return num / den

def sigma(oper, start, stop, str_if_statement):
    ans = 0
    for i in range(start, stop + 1):
        func = function(oper)
        func.solve(i, oper)
