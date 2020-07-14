def ehcf(a, b):
  p1, q1, h1, p2, q2, h2 = 1, 0, a, 0, 1, b
  from math import floor
  while h2 != 0:
    r = floor(h1/h2)
    p3 = p1-r*p2
    q3 = q1-r*q2
    h3 = h1-r*h2
    p1,q1,h1,p2,q2,h2 = p2,q2,h2,p3,q3,h3
  return (p1, q1, h1)

def findinverse(k, p):
  l = ehcf(k,p)[0] % p
  return l