import random
import sympy

TESTS_PER_PRIME = 10

for i in range(1,15):
    p = sympy.prime(i)
    for _ in range(TESTS_PER_PRIME):
        a,b,c = 1, random.randrange(p), random.randrange(p)
        roots = []
        for x in range(p):
            v = (a*x**2 + b*x + c) % p
            if v == 0:
                roots.append(x)
        if roots:
            print(f"x^2+{b}x + {c} mod {p}", "is reducable with roots", roots)
        else:
            print(f"x^2+{b}x + {c} is irreducible in mod {p}")
