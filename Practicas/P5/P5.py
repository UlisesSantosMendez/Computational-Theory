from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r)
                               for r in range(len(s)+1))


print(list(powerset(['q0', 'q1', 'q2'])))
Q = ['q0', 'q1']
Sigma = ['a', 'b']
s = 'q0'
F = ['q1']
DELTA = {('q0', 'a'): ['q0', 'q1'],
         ('q0', 'b'): ['q1'],
         ('q1', 'b'): ['q0', 'q1']}

Qprima = list(powerset(Q))
Fprima = []
for q in Qprima:
    for x in q:
        if x in F:
            Fprima.append(q)


print("Qprima", Qprima)
print("Fprima", Fprima)
sprima = (s,)
Sigmaprima = Sigma
