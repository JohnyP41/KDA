from scipy.linalg import hadamard
a=input("Podaj wielkosc\n")
b=int(a)
for _ in hadamard(b):
  for a in _:
    print(" 1" if a == 1 else a, end='  ')
  print()
