from RandomNumberGenerator import RandomNumberGenerator as Rng


# Zwraca indeks elementu listy arr, ktoremu odpowiada najmniejszy parametr z listy arg
def min_ind(ind, arg):
    if type(ind) is list and type(arg) is list:
        i_val = 0
        v_min = 99999
        for id in ind:
            if arg[id] < v_min:
                v_min = arg[id]
                i_val = id
    else:
        print('Invalid arguments')
    return i_val


# Zwraca argument z listy arg, sposrod indeksow z listy arr
def min_arg(ind, arg):
    if type(ind) is list and type(arg) is list:
        v_min = 99999
        for id in ind:
            if arg[id] < v_min:
                v_min = arg[id]
                i_val = id
    else:
        print('Invalid arguments')
    return v_min


# Zwraca indeks elementu listy arr, ktoremu odpowieada najwiekszy parametr z listy arg
def max_ind(ind, arg):
    if type(ind) is list and type(arg) is list:
        i_val = 0
        v_max = 0
        for id in ind:
            if arg[id] > v_max:
                v_max = arg[id]
                i_val = id
    else:
        print('Invalid arguments')
    return i_val


seed = int(input("Ziarno: "))
n = int(input("Ilosc elementow:"))

rng = Rng(seedVaule=seed)

Cq = []
J = []
P_j = []    # czasy wykonania
R_j = []    # czasy przygotowania/termin dostepnosci
S = []      # czasy rozpoczecia
C = []      # czasy zakonczenia
Q_j = []    # czas dostarczenia/stygniecia
G = []
A = 0

for i in range(n):
    J.append(i)

for i in range(n):
    p_j = rng.nextInt(1, 29)
    P_j.append(p_j)
    A = A + p_j

for i in range(n):
    r_j = rng.nextInt(1, A)
    R_j.append(r_j)

X = A
for i in range(n):
    q_j = rng.nextInt(1, X)
    Q_j.append(q_j)

Cq = []
S.append(R_j[0])
C.append(P_j[0])
Cq.append(C[0] + Q_j[0])
C_max = C[0] + Q_j[0]

for i in range(1, n):
    S.append(max(R_j[i], C[i-1]))
    C.append(S[i] + P_j[i])
    Cq.append(C[i] + Q_j[i])
    C_max = max(C_max, Cq[i-1])


for i in range(n):
    J[i] += 1

print(f'nr:{J}')
print(f'r:{R_j}')
print(f'p:{P_j}')
print(f'q:{Q_j}')
print()

for i in range(n):
    J[i] -= 1
PI = J.copy()

# print('Przed algorytmem Schrage:')
#
# for i in range(n):
#     PI[i] += 1
#
# print(f'PI:{PI}')
# print(f'S:{S}')
# print(f'C:{C}')
# print(f'Cq:{Cq}')
# print(f'Cmax: {C_max}')
# print()
#
# for i in range(n):
#     PI[i] -= 1

S.clear()
C.clear()
Cq.clear()
PI.clear()

# _____________________Algorytm Schrage________________________________

G.clear()
N = J.copy()
t = min_arg(N, R_j)

while len(G) != 0 or len(N) != 0:
    while len(N) != 0 and min_arg(N, R_j) <= t:
        e = min_ind(N, R_j)
        G.append(e)
        N.remove(e)
    if len(G):
        e = max_ind(G, Q_j)
        PI.append(e)
        G.remove(e)
        t += P_j[e]
    else:
        t = min_arg(N, R_j)


S.append(R_j[PI[0]])
C.append(P_j[PI[0]])
Cq.append(C[0] + Q_j[PI[0]])
C_max = C[0] + Q_j[PI[0]]

for i in range(1, n):
    S.append(max(R_j[PI[i]], C[i-1]))
    C.append(S[i] + P_j[PI[i]])
    Cq.append(C[i] + Q_j[PI[i]])
    C_max = max(C_max, Cq[i-1])


print('Po zastosowaniu algorytmu:')
for i in range(n):
    PI[i] += 1

print(f'PI:{PI}')
print(f'S:{S}')
print(f'C:{C}')
print(f'Cq:{Cq}')
print(f'Cmax: {C_max}')
print()

for i in range(n):
    PI[i] -= 1

S.clear()
C.clear()
Cq.clear()
PI.clear()
G.clear()
N.clear()

# _____________________Algorytm Schrage z kolejka__________________________________


Nk = []
tmp = J.copy()
while len(tmp) != 0:
    m = min_ind(tmp, R_j)
    Nk.append(m)
    tmp.remove(m)

t = min_arg(Nk, R_j)

while len(G) != 0 or len(Nk) != 0:
    while len(Nk) != 0 and min_arg(Nk, R_j) <= t:
        e = Nk[0]
        G.append(e)
        Nk.pop(0)

    tmp = G.copy()
    G.clear()
    done = 0
    while len(tmp) != 0 and done == 0:
        m = max_ind(tmp, Q_j)
        G.append(m)
        tmp.remove(m)
    done = 1

    if len(G):
        e = G[0]
        PI.append(e)
        G.pop(0)
        t += P_j[e]
    else:
        t = min_arg(N, R_j)


S.append(R_j[PI[0]])
C.append(P_j[PI[0]])
Cq.append(C[0] + Q_j[PI[0]])
C_max = C[0] + Q_j[PI[0]]

for i in range(1, n):
    S.append(max(R_j[PI[i]], C[i-1]))
    C.append(S[i] + P_j[PI[i]])
    Cq.append(C[i] + Q_j[PI[i]])
    C_max = max(C_max, Cq[i-1])


print('Po zastosowaniu algorytmu na z kolejka:')
for i in range(n):
    PI[i] += 1

print(f'PI:{PI}')
print(f'S:{S}')
print(f'C:{C}')
print(f'Cq:{Cq}')
print(f'Cmax: {C_max}')
print()

for i in range(n):
    PI[i] -= 1

S.clear()
C.clear()
Cq.clear()
PI.clear()
G.clear()

# _____________________________Algorytm SchragePmtn__________________________________

C_max = 0
N = J.copy()
t = 0
l = 0

while len(G) != 0 or len(N) != 0:
    while len(N) != 0 and min_arg(N, R_j) <= t:
        e = min_ind(N, R_j)
        G.append(e)
        N.remove(e)
        if Q_j[e] > Q_j[l]:
            P_j[l] = t - R_j[e]
            t = R_j[e]
            if P_j[l] > 0:
                G.append(e)
    if len(G):
        e = max_ind(G, Q_j)1
        G.remove(e)
        t += P_j[e]
        C_max = max(C_max, t + Q_j[e])
        l = e
    else:
        t = min_arg(N, R_j)


print('Po zastosowaniu algorytmu z przerwaniami:')
print(f'Cmax: {C_max}')
print()
