class Probability:
    def __init__(self, desired_outcomes, all_outcomes):
        self.desired_outcomes = desired_outcomes
        self.all_outcomes = all_outcomes
    def value(self):
        v = len(set(self.desired_outcomes)) / len(set(self.all_outcomes))
        return v
    def complement(self):
        v = len(set(self.desired_outcomes)) / len(set(self.all_outcomes))
        return 1 - v
    
def are_mututally_exclusive(A, B):
    A_intersection_B = (set(A.desired_outcomes)).intersection(set(B.desired_outcomes))
    if A_intersection_B == 0:
        return True
    else:
        return False

def A_or_B(A, B, universal_set):
    A_intersection_B = (set(A.desired_outcomes)).intersection(set(B.desired_outcomes))
    prob_A_intersection_B = len(A_intersection_B) / len(universal_set)
    a_or_b = A.value() + B.value() - prob_A_intersection_B
    return a_or_b

def A_and_B_single_try_independent(A, B, universal_set):
    A_intersection_B = (set(A.desired_outcomes)).intersection(set(B.desired_outcomes))
    prob_A_intersection_B = len(A_intersection_B) / len(universal_set)
    return prob_A_intersection_B

def A_and_B_two_tries_independent(A, B):
    return A.value() * B.value()

def A_given_B(A, B, universal_set):
    A_intersection_B = (set(A.desired_outcomes)).intersection(set(B.desired_outcomes))
    prob_A_intersection_B = len(A_intersection_B) / len(universal_set)
    prob_A_given_B = prob_A_intersection_B / B.value()
    return prob_A_given_B

def Bayes_A_given_B(A, B, universal_set):
    prob_B_given_A = A_given_B(B, A, universal_set)
    numerator = prob_B_given_A * A.value()
    val = numerator / B.value()
    return val
