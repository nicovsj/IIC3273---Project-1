from time import time
import pandas as pd

from pollard import pollards_rho
from bsgs import bsgs
from pohlighellman import pohlig_hellman_bsgs

M = 424242

args_ph = [
    (2, 11, 59, {59:1}),
    (5, 234, 719, {719:1}),
    (2, 11, 4127, {4127:1}),
    (7, 3245, 19079, {19079:1}),
    (11, 67231, 360947,{360947:1}),
    (5, M, 5041259, {5041259:1}),
    (5, M, 87993167, {87993167:1}),
    (2, M, 1726565507, {1726565507:1}),
    (7, M, 24455596799, {24455596799:1}),
    (5, M, 368585361623, {368585361623:1}),
    (11,M, 4520967464159, {4520967464159:1}),
    (5, M, 66008980226543, {66008980226543:1}),
    (5, M, 676602320278583, {676602320278583:1}),
    (2, M, 2075952270932339, {2075952270932339:1})
    # (7, M, 21441211962585599)
]

functions = {
    "Pollard's rho": pollards_rho,
    "BSGS": bsgs,
    "Pohlig-Hellman (BSGS)": pohlig_hellman_bsgs,
    # "Naive" : brutelog
}

cols = {
    "Pollard's rho": 'pollard',
    "BSGS": 'bsgs',
    "Pohlig-Hellman (BSGS)": 'pohlig-hellman'
}

df = pd.DataFrame(columns = ['p', 'pollard', 'bsgs', 'pohlig-hellman'])

for arg in args_ph:
  print("\nParams -> g = {}; h = {}; r = {}".format(* arg))
  data = dict()
  data['p'] = arg[2]

  for key in functions:
    print("\nAlgorithm:", key)
    if key != "Pohlig-Hellman (BSGS)":
      print(functions[key](arg[0], arg[1], arg[2]))
    else:
      print(functions[key](*arg))

  # df.append(pd.Series(data), ignore_index=True)