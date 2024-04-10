from itertools import combinations, product

die_a = [1,2,3,4,5,6]
die_b = [1,2,3,4,5,6]

# Part-A Question 1
def num_combinations(die_a, die_b):
    return len(die_a) * len(die_b)

# Part-A Question 2
def sum_combinations(die_a, die_b):
    sums = dict()
    for a in die_a:
        for b in die_b:
            s = a + b
            if s in sums:
                sums[s] += 1
            else:
                sums[s] = 1
    return sums

def matrix_combinations(die_a, die_b):
    matrix = [[0]*6 for _ in range(6)]
    for i, a in enumerate(die_a):
        for j, b in enumerate(die_b):
            matrix[i][j] = a + b
    return matrix

# def get_probability(die_a, die_b, s):
#     sums = sum_combinations(die_a, die_b)
#     return sums[s] / num_combinations(die_a, die_b)

# Part-A Question 3
def get_all_probabilities(die_a, die_b):
    sums = sum_combinations(die_a, die_b)
    probabilities = dict()
    for s in sums:
        probabilities[s] = sums[s] / num_combinations(die_a, die_b)
    return probabilities

def undoom_dice(die_a, die_b):
    target = sum_combinations(die_a, die_b)
    for new_die_a in product(range(5), repeat=len(die_a)):
        for new_die_b in combinations(range(9), r=len(die_b)):
            if sum_combinations(new_die_a, new_die_b) == target:
                return list(new_die_a), list(new_die_b)
    

# print(sum_combinations(die_a, die_b))
# probabilities = get_all_probabilities(die_a, die_b)
# print(probabilities)

# new_die_a, new_die_b = undoom_dice(die_a, die_b)
# print(new_die_a)
# print(new_die_b)
# print(sum_combinations(new_die_a, new_die_b))
# print(matrix_combinations(die_a, die_b))
# print(matrix_combinations(new_die_a, new_die_b))

# Part-A Question 1
print("Total number of combinations are: ", num_combinations(die_a, die_b))

# Part-A Question 2
distribution = matrix_combinations(die_a, die_b)
for row in distribution:
    print(row)
sums = sum_combinations(die_a, die_b)
print("Sum distribution: ", sums)

# Part-A Question 3
probabilities = get_all_probabilities(die_a, die_b)
print("Probabilities: ", probabilities)

print('--------------------------------------------')
# Part-B
new_die_a, new_die_b = undoom_dice(die_a, die_b)
print("New die A: ", new_die_a)
print("New die B: ", new_die_b)
distribution = matrix_combinations(new_die_a, new_die_b)
print(distribution)
probabilities = get_all_probabilities(new_die_a, new_die_b)
print(probabilities)
