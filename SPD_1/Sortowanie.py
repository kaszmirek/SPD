from RandomNumberGenerator import RandomNumberGenerator as Rng
import itertools


seed = int(input("Ziarno: "))
n = int(input("Ilosc elementow:"))

rng = Rng(seedVaule=seed)

pi = []
P_j = []  # czasy wykonania
R_j = []  # czasy przygotowania/termin dostepnosci
S_j = []  # czasy rozpoczecia
C_j = []  # czasy zakonczenia
Q_j = []  # czas dostarczenia/stygniecia
A = 0
X = 29

for i in range(n):
    pi.append(i)

for i in range(n):
    p_j = rng.nextInt(1, 29)
    P_j.append(p_j)
    A = A + p_j

for i in range(n):
    r_j = rng.nextInt(1, A)
    R_j.append(r_j)

for i in range(n):
    q_j = rng.nextInt(1, X)
    Q_j.append(q_j)

for i in range(n):
    print(pi[i], end=' ')
print()

print('-'*2*n)

print('r:', end=' ')
for i in range(n):
    print(R_j[i], end=' ')
print()

print('p:', end=' ')
for i in range(n):
    print(P_j[i], end=' ')
print()

print('q:', end=' ')
for i in range(n):
    print(Q_j[i], end=' ')
print()

# PI = itertools.permutations(pi)
#
# for i in PI:
#     S_j.append(0)
#     cnt = 0
#     temp = 0
#     C_pimax = 0
#     for j in i:
#         if cnt != 0:
#             S_j.append(max(R_j[j], C_j[temp]))
#         temp = cnt
#         C_j.append(S_j[cnt] + P_j[cnt])
#         cnt = cnt + 1
#         C_pimax = max(C_j)
#
#     if C_pimax < Cmin:
#         Cmin = C_pimax
#         optimal = i
#     S_j.clear()
#     C_j.clear()
#
# print(f'optimal: {optimal}')
# print(f'C_min: {Cmin}')

S_j.append(R_j[0])
C_j.append(S_j[0] + P_j[0])
C_max = C_j[0] + Q_j[0]

for j in range(n):
    if j != 0:
        S_j.append(max(R_j[j], C_j[j-1]))
        C_j.append(S_j[j] + P_j[j])
        C_max = max(C_max, C_j[j] + Q_j[j])

print(f'Cmax: {C_max}')
print(pi)
print(S_j)
print(C_j)

for i in range(n):
    print(C_j[i] + Q_j[i], end=' ')
print()

# Algorytm Schrage

N = pi
G = []
t = min(R_j)
k = 1

while G != 0 or N != 0:
    while N != 0 and min(R_j) <= t:
