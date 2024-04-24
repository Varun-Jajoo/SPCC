def cal_first(s, productions):
    first = set()
    for i in range(len(productions[s])):
        for j in range(len(productions[s][i])):
            c = productions[s][i][j]
            if c.isupper():
                f = cal_first(c, productions)
                if 'ε' not in f:
                    first.update(f)
                    break
                else:
                    if j == len(productions[s][i]) - 1:
                        first.update(f)
                    else:
                        first.update(f)
            else:
                first.add(c)
                break
    return first

productions = {
        'S': [['a', 'B', 'D', 'h']],
        'B': [['c', 'C']],
        'C': [['b', 'C'], ['ε']],
        'D': [['E', 'F']],
        'E': [['g'], ['ε']],
        'F': [['f'], ['ε']]
    }
first = {}

for s in productions.keys():
    first[s] = cal_first(s, productions)

print("*****FIRST*****")
for lhs, rhs in first.items():
    print(lhs, ":", rhs)
    print("")
