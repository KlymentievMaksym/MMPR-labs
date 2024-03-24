import numpy as np

# Перевірити, чи буде дане відношення рефлексивним, антирефлексивним,
# симетричним, антисиметричним, асиметричним, транзитивним. Відшукати
# для нього найбільший, найменший , максимальний та мінімальний елементи,
# якщо такі існують, і побудувати обернене й додаткове відношення

# [1, 1, 0, 1, 0]
# [1, 1, 1, 1, 0]
# [0, 0, 0, 0, 1]
# [1, 0, 1, 1, 1]
# [0, 1, 0, 0, 0]

# r = np.matrix([[1, 1, 0, 1, 0],
#                [1, 1, 1, 1, 0],
#                [0, 0, 0, 0, 1],
#                [1, 0, 1, 1, 1],
#                [0, 1, 0, 0, 0]])

# r = np.matrix([[0, 0, 0, 0],
#                [0, 1, 1, 1],
#                [0, 1, 1, 1],
#                [0, 0, 0, 0]])

r = np.matrix([[1, 0, 0],[1, 0, 1],[0, 1, 1]])


def check_refl(r):
    i = 0
    j = 0

    is_refl = False
    is_antirefl = False

    while i != r.shape[0] and j != r.shape[1]:
        if r[i, j] == 1:
            is_refl = True
        elif is_refl and r[i, j] == 0:
            is_refl = False
            break
        elif r[i, j] == 0:
            is_antirefl = True
        elif is_antirefl and r[i, j] == 1:
            is_antirefl = False
            break
        i += 1
        j += 1
    return ["Neither refl nor antirefl", ["Refl", "Antirefl"][is_antirefl]][is_refl or is_antirefl]


def check_sym(r):

    is_sym = True
    is_asym = True
    is_antisym = True

    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            if r[i, j] != r[j, i]:
                is_sym = False
            elif i != j and not ((r[i, j] and r[j, i]) == 0):
                is_antisym = False
            if r[i, j] == 1 and r[j, i] == 1:
                is_asym = False
    return ["Neither sym nor antisym", ["Sym", "Antisym"][is_antisym]][is_sym or is_antisym] + [", Not asym", ", Asym"][is_asym]


def check_transit(r):
    r_2 = r**2
    r_2[r_2>1] = 1

    print(r_2)

    is_transit = True

    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            if r_2[i, j] > r[i, j]:
                is_transit = False
    return ["Not transit", "Transit"][is_transit]


def find_best_and_worst(r, is_row=True, goal=1):
    best = []
    worst = []

    r_count = 1

    for row in r:
        if is_row:
            if np.all(row==goal):
                best += [r_count]
        else: 
            if np.all(row==goal):
                worst += [r_count]
        r_count += 1
    return best, worst


def strong_relation(r):
    # r_s = np.zeros_like(r)
    r_s = r - r.T
    r_s[r_s < 0] = 0
    # for i in range(r.shape[0]):
    #     for j in range(r.shape[1]):
    #         if (r[i, j] or r[j, i]) != 0 and (r[j, i] == 0):
    #             r_s[i, j] = 1
    return r_s


def find_max_and_min(r):
    r_s = strong_relation(r)
    print(f"\nStrong relation: \n{r_s}")
    max = find_best_and_worst(r_s, is_row=False, goal=0)[1]
    min = find_best_and_worst(r_s, goal=0)[0]
    return max, min


def addition(r):
    r_a = np.zeros_like(r)
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            r_a[i,j] = 1 - r[i,j]
    return r_a

print(f"Our R is: \n{r}\n")

print(check_refl(r))
print(check_sym(r))
print(check_transit(r))

r_t = r.T
best1, worst1 = find_best_and_worst(r)
best2, worst2 = find_best_and_worst(r_t, is_row=False)

best1 += best2
worst1 += worst2

print(f"\nBest is: {list(set(best1))}(Rows that has only 1)\nWorst is: {list(set(worst1))}(Cols that has only 1)")

maxi, mini = find_max_and_min(r)
print(f"\nMax is: {maxi}(Cols that has only 0)\nMin is: {mini}(Rows that has only 0)")

try:
    r_1 = r**(-1)
    print(f"\nR^(-1) is: \n{r_1}")
except np.linalg.LinAlgError:
    print(f"\nIt doesn't have inverse (R^(-1)), so heres comes transposition: \n{r.T}")

print(f"\nR addition is: \n{addition(r)}")
