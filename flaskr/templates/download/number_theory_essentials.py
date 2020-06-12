
import math
import itertools

functions_in_this_package = {"is_prime": "a primality test Miller-Rabin",
                             "lucas_lehmer": "Lucas Lehmer mersenne prime test",
                             "prime_gen": "generates primes",
                             "lucas_lehmer_gen": "generates mersenne primes",
                             "factor": "factors a number",
                             "partition": "partitions a number",
                             "primitive_root": "finds primitive roots modulo n",
                             "root_equivalents": "finds numbers modulo n equivalent to root given its square",
                             "sum_set_exploration": "a tool for exploring various sum sets",
                             "pigeon_hole": "finds number of theoretical items needed to be pulled blindly to ensure "
                                            "a certain number of items of the same color"}


# Prime stuff


def is_prime_wilson_theorem(n):
    if math.factorial(n - 1) % n == n - 1:
        return True
    else:
        return False


def pythagorean_theorem(num):
    # This is not finished
    for i in range(1, num ** 2):
        i = i + 1
        return i


def is_prime(num):
    prime = True
    if (num % 2 != 0 or 2) and num != 1:
        for i in range(2, num):
            if num % i == 0:
                prime = False
    else:
        prime = False
    return prime


def prime_gen(start, stop):
    ans = []
    for i in range(start, stop + 1):
        if is_prime(i):
            ans.append(i)
    return ans


def lucas_lehmer(p):
    s = 4
    m = pow(2, p) - 1
    for i in range(1, p - 1):
        s = (pow(s, 2) - 2) % m
    if s == 0:
        return True, pow(2, p) - 1


def lucas_lehmer_gen(start, stop):
    answer = []
    for j in range(start, stop + 1):
        if lucas_lehmer(j):
            print(j, lucas_lehmer(j))
            answer.append(j ** 2 - 1)
        return answer


def prime_factor(number):
    ans = []
    for i in range(2, number):
        if is_prime(i):
            x = 0
            while x == 1:
                if number % i == 0:
                    ans.append(i)
                    number = int(number / i)
                else:
                    x = 2
            if number == 1:
                return ans


def factor(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


def find_lcm(m, n):
    result = m * n / math.gcd(m, n)
    print(result)


def totient_function(m, print_units):
    units = []
    for i in range(1, m + 1):
        if math.gcd(i, m) == 1:
            units.append(i)
    ans = len(units)
    if not print_units:
        return ans
    else:
        return ans, units


def nth_power(stop, power):
    ans = []
    for i in range(1, stop + 1):
        power = i ** power
        ans.append(power)
    return ans


def pascal_triangle(n, x):
    ans = 1
    for i in range(0, x + 1):
        number = n - i
        ans = number * ans
    ans = ans / math.factorial(x)
    return int(ans)


def pascals_triangle(stop):
    ans = []
    for n in range(1, stop + 1):
        l = [1]
        for k in range(1, n):
            l.append(pascal_triangle(n, k))
        l.append(1)
        print(l)
        ans.append(l)
    return ans


def d(n, m):
    if (m / n) % 1 == 0:
        return True


def partition(n):
    partitions = []
    l = ""
    for i in range(1, n + 1):
        l += str(i)
    for i in range(1, n + 1):
        combination = itertools.product(l, repeat=i)
        for element in combination:
            z = 0
            for character in element:
                z += int(character)
            if z == n:
                new_part = []
                for item in element:
                    new_part.append(int(item))
                if sorted(new_part) not in partitions:
                    partitions.append(new_part)
    return partitions


def primitive_root(n):
    primitive_roots = []
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            number = []
            power = pow(i, 2) % n
            while (power != i) and (power != 0) and (power != 1):
                if power not in number:
                    number.append(power)
                power = pow(power, 2) % n
                if len(number) == n:
                    return i, number
    if len(primitive_roots) == 0:
        number = []
        for w, y in itertools.product(range(2, n), repeat=2):
            number = []
            for x in range(1, n):
                for z in range(1, n):
                    if (math.gcd(w, n) == 1) and (math.gcd(y, n) == 1):
                        if not (pow(w, x) * pow(y, z)) % n in number:
                            number.append((pow(w, x) * pow(y, z)) % n)
            if len(number) == n / 2 - ((n / 2) % 1):
                return str(w) + ", " + str(y)
    return "none"


def primitive_root_table_multiplication(modulus):
    modulus = int(modulus)
    name = "primitive_root_table" + str(modulus) + ".txt"
    file = open(name, 'w')
    file.write(
        '\\documentclass{article}\n' + '\\usepackage[utf8]{inputenc}\n' + '\\begin{document}\n' + '\\begin{tabular}{|c|c|}\n' + '     number & primitive root equivalent \\\ \n')
    primitive_roots = primitive_root(modulus)
    two_gens = False
    if "," in str(primitive_roots):
        two_gens = True
    if two_gens:
        list_of_numbers = {}
        for w, x, y, z in itertools.product(range(0, modulus), repeat=4):
            if pow(int(w), int(x)) * pow(y, z) % int(modulus) not in list_of_numbers:
                list_of_numbers.update({str(w) + " " + str(x) + " " + str(y) + " " + str(z): (pow(w, x) * pow(y, z))})
        for key in list_of_numbers:
            new_key = ""
            w = 0
            x = 0
            y = 0
            z = 0
            var = ""
            for item in key:
                if item == " ":
                    if w == 0:
                        w = var
                    elif x == 0:
                        x = var
                    elif y == 0:
                        y = var
                    elif z == 0:
                        z = var
                    var = ""
                else:
                    var = var + item
            new_key = "$" + str(w) + "^" + str(x) + "\\cdot" + str(y) + "^" + str(z) + "$"
            line = new_key + " & " + "$" + str(modulus) + "^" + str(list_of_numbers[key]) + "$"
            line = line + '\\\ ' + '\n'
            file.write(line)
    else:
        pass
    file.write('\\end{tabular}\n' + '\\end{document}\n')
    file.close()


def root_equivalents(modulus, square_of_root):
    root_equivalent = []
    for i in range(0, modulus):
        if i ** 2 % modulus == square_of_root:
            root_equivalent.append(i)
    return root_equivalent


def sum_set_exploration(set_a, set_b):
    sum_set = []
    for a in set_a:
        for b in set_b:
            sum_set.append(a + b)
    sum_set = set(sum_set)
    return sum_set


def pigeon_hole(colors, number_needed):
    return (number_needed - 1) * colors
