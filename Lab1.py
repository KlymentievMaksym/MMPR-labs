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

r = np.matrix([[1, 1, 0, 1, 0],[1, 1, 1, 1, 0],[0, 0, 0, 0, 1],[1, 0, 1, 1, 1],[0, 1, 0, 0, 0]])
# print(r.shape)

# Відношення R називається рефлексивним, якщо
# x R x для будь-якого елемента x∈Ω .

# Відношення R називається антирефлексивним, коли
# твердження x R y означає, що x ≠ y ∀ ∈x Ω. 
# У матриці антирефлексивного відношення елементи головної діагоналі
# дорівнюють нулю, тобто aij = ,0 якщо i = j .

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


# Відношення R називається симетричним, якщо
# x R y ⇒ y R x
# Матриця симетричного відношення теж симетрична, тобто a(ij) = a(ji) для
# всіх значень i, j. 

# Відношення R називається асиметричним, якщо
# R cross R^-1 = 0 (тобто з двох виразів x R y та y R x хоча б один не відповідає
# дійсності). 
# У матриці симетричного відношення a(ij) ∧ a(ji) = 0 для всіх значень i, j.
# Інакше кажучи, з двох симетричних елементів a(ij) і a(ji) хоча б один обов’язково
# дорівнює 0.

# Відношення R називається антисиметричним,
# якщо твердження x R y та y R x можуть бути правильними одночасно тоді й
# тільки тоді, коли x = y. 
# У матриці антисиметричного відношення a(ij) ∧ a(ji) = 0, коли i ≠ j . 

def check_sym(r):

    is_sym = False
    is_asym = False
    is_antisym = False

    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            if r[i, j] == r[j, i]:
                is_sym = True
            elif is_sym and r[i, j] != r[j, i]:
                is_sym = False
            elif i != j and not ((r[i, j] and r[j, i]) == 0):
                is_antisym = True
            if r[i, j] and r[j, i]:
                is_asym = True
            else:
                is_asym = False
    return ["Neither sym nor antisym", ["Sym", "Antisym"][is_antisym]][is_sym and is_antisym] + [", Not asym", ", Asym"][is_asym]


# Відношення R називається транзитивним, якщо
# R^2 <= R ( тобто, коли з тверджень x R z та z R y випливає, що x R y ). 
# Зауважимо, що умова: , 2 ≤ RR дає зручний спосіб перевірки
# транзитивності відношення в разі, коли відношення задано за допомогою
# матриці. Для цього необхідно обчислити матрицю відношення 2 R (тобто
# піднести до квадрату матрицю вихідного відношення) і перевірити умову.
# Якщо ij( )≤ ij( ) RaRa 2 для всіх значень i, j, то відношення транзитивне

def check_transit(r):
    r_2 = r**2

    is_transit = False

    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            if r_2[i, j] <= r[i, j]:
                is_transit = True
            elif is_transit and r_2[i, j] > r[i, j]:
                is_transit = False
    return ["Not transit", "Transit"][is_transit]

# Елемент * x множини Х будемо називати найкращим з огляду на
# відношення R, якщо x R x * справедливе для всякого елемента x∈ X .

# Елемент ∈ Xx* будемо називати найгіршим з огляду на відношення R,
# якщо * x R x для всіх елементів x∈ X . 

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

# Елемент max x називається максимальним за відношенням S R на множині
# Х, коли для абиякого елемента x∈ X має місце твердження xRx S
# max або
# елемент max x непорівнянний з x.
# Іншими словами, не існує елемента (альтернативи) x∈ X , який був би
# кращим за альтернативу max x .
# Множина максимальних з огляду на відношення R елементів множини Х
# позначається R X .max

# Елемент min x називається мінімальним відносно S R на множині Х, якщо
# для всіх x∈ X або min xx RS , або х непорівняний з min x . Отже, не існує елемента
# x ∈ X який був би гіршим за min x ; немає жодного елемента х, над яким би
# домінував елемент min x .
# Множина мінімальних з огляду на відношення R елементів множини Х
# позначається як min R X . 

def strong_relation(r):
    r_s = np.zeros_like(r)
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            if (r[i, j] or r[j, i]) != 0 and (r[j, i] == 0):
                r_s[i, j] = 1
    return r_s


def find_max_and_min(r):
    r_s = strong_relation(r)
    print(f"\nStrong relation: \n{r_s}")
    max = find_best_and_worst(r_s, is_row=False, goal=0)[1]
    min = find_best_and_worst(r_s, goal=0)[0]
    return max, min



# Оберненим до відношення R називається
# відношення −1 R , яке задовольняє таку умову:
#  xR yy x R- 1 ⇔ . (2.4)
# Для матриць відношень R та −1 R буде мати місце така формула:
# ij( )= ji( )

# Відношення R називається доповненням відношення
# R , тоді й тільки тоді, коли воно пов’язує тільки ті пари елементів, для яких не
# виконується відношення R .
# Очевидно, що
# Ω ,\ 2 R = R (2.3)
# тому в матричному записі ij( ) 1−= ij( ) RaRa , = ,1, nji . 

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

print(f"\nBest is: {list(set(best1))}\nWorst is: {list(set(worst1))}")

maxi, mini = find_max_and_min(r)
print(f"\nMax is: {maxi}\nMin is: {mini}")

try:
    r_1 = r**(-1)
    print(f"\nR^(-1) is: \n{r_1}")
except np.linalg.LinAlgError:
    print("\nIt doesn't have inverse (R^(-1))")

print(f"\nR addition is: \n{addition(r)}")
