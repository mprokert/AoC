data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

ts = []
sets = []


for line in data.splitlines():
    c1, c2 = line.split("-")
    ts.append(sorted([c1, c2]))


for c1, c2 in ts:
    candidates1 = []
    candidates2 = []
    for x1, x2 in ts:
        if x1 == c1 and x2 != c2:
            if x2 in candidates2:
                sets.append(tuple(sorted([c1, c2, x2])))
            else:
                candidates1.append(x2)
        if x1 == c2 and x2 != c2:
            if x2 in candidates1:
                sets.append(tuple(sorted([c1, c2, x2])))
            else:
                candidates2.append(x2)
        if x2 == c1 and x1 != c1:
            if x1 in candidates1:
                sets.append(tuple(sorted([c1, c2, x1])))
            else:
                candidates2.append(x1)
        if x2 == c2 and x1 != c1:
            if x1 in candidates1:
                sets.append(tuple(sorted([c1, c2, x1])))
            else:
                candidates1.append(x1)

sets = list(set(sets))

c = 0
for c1, c2, c3 in sets:
    if c1.startswith("t") or c2.startswith("t") or c3.startswith("t"):
        c+=1
print(c)
"""
max_sets = sets[:]

while sets:
    next_sets = []
    max_sets = sets[:]
    curr_len = len(sets[0])
    print(curr_len)
    while sets:
        n = sets.pop()
        print(len(sets),len(next_sets))
        candidates = {}
        for other in sets:
            if len(set(n) & set(other)) == curr_len-1:
                candidates.setdefault(tuple(sorted(set(n)|set(other))), []).append(other)
        for candidate in candidates:
            if len(candidates[candidate]) == curr_len:
                next_sets.append(candidate)
    sets = list(set(next_sets))

print(list(set(max_sets)))
"""

conns = {}


for line in data.splitlines():
    c1, c2 = line.split("-")
    conns.setdefault(c1, []).append(c2)
    conns.setdefault(c2, []).append(c1)

max_clique = []
for k in conns:
    cliques = []
    for k2 in conns[k]:
        for clique in cliques:
            for member in clique:
                if k2 not in conns[member]:
                    break
            else:
                clique.append(k2)
                break
        else:
            cliques.append([k, k2])
    max_k = max(cliques, key=len)
    if len(max_k) > len(max_clique):
        max_clique = max_k

print(",".join(sorted(max_clique)))
