from utils import ehcf, findinverse


def mixing_function(x, g, a, p):
  x = x % p
  if x <= p/3:
    return g*x % p
  elif x < 2*p/3:
    return pow(x,2,p)
  else:
    return a*x % p


def alpha_function(alpha, x, p):
  alpha = alpha % (p-1)
  if x <= p/3:
    return (alpha + 1) % (p-1)
  elif x < 2*p/3:
    return 2*alpha % (p-1)
  else:
    return alpha


def beta_function(beta, x, p):
  beta = beta % (p-1)
  if x <= p/3:
    return beta
  elif x < 2*p/3:
    return 2*beta % (p-1)
  else:
    return (beta + 1) % (p-1)

def pollards_rho(g, a, p):
  i = 1
  x = mixing_function(1, g, a, p)
  y = mixing_function(mixing_function(1, g, a, p), g, a, p)
  alpha = alpha_function(0, x, p)
  beta = beta_function(0, x, p)
  gamma = alpha_function(alpha_function(0,y,p), mixing_function(y, g, a, p), p)
  delta = beta_function(beta_function(0, y, p), mixing_function(y, g, a, p), p)
  while x != y:
    i += 1
    alpha = alpha_function(alpha, x, p)
    beta = beta_function(beta, x, p)
    gamma = alpha_function(alpha_function(gamma, y, p), mixing_function(y, g, a, p), p)
    delta = beta_function(beta_function(delta, y, p), mixing_function(y, g, a, p), p)
    x = mixing_function(x, g, a, p)
    y = mixing_function(mixing_function(y, g, a, p), g, a, p)
  u = (alpha - gamma) % (p-1)
  v = (delta - beta) % (p-1)
  d = ehcf(v, p-1)[2]
  if d == 1:
    return (findinverse(v, p-1)*u) % p
  else:
    s = ehcf(v, p-1)[0]
    w = (s*u) % (p-1)
    for k in range(d):
      if pow(g, (w//d + k*(p-1)//d)%p, p) == a % p:
        return (w//d + k*(p-1)//d) % p
    return None