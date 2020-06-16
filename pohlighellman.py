from bsgs import bsgs
from utils import ehcf, findinverse
import numpy as np

def pohlig_hellman_bsgs(g, h, p, N_fact):
  N = 1
  while pow(g, N, p) != 1:
    N+=1
  print(N)
  a = []
  m = []
  for i in N_fact:
    g_i = pow(g, int(p/(i**N_fact[i])), p)
    h_i = pow(h, int(p/(i**N_fact[i])), p)
    y_i = bsgs(g_i, h_i, p)
    a.append(y_i)
    m.append(i**N_fact[i])

  return chinese_remainder(a, m)

def chinese_remainder(a, m):
  if len(a) != len(m):
    return "a and m are of different lengths"
  for i in range(len(m)):
    for j in range(i+1, len(m)):
      if ehcf(m[i], m[j])[2] != 1:
        return "The chosen moduli are not coprime"
  moduli_product = np.prod(m)
  return solve_system(a, m) % moduli_product

def solve_system(a, m):
  i = len(a)
  if i == 1:
    x = a[0]
  else:
    b, n = a[0:i-1], m[0:i-1]
    c = solve_system(b,n)
    p = np.prod(n)
    y = findinverse(p, m[i-1]) * (a[i-1]-c)
    x = c+p*y
  return x