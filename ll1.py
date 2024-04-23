data = {
    'E': ['TX'],
    'X': ['+TX', 'e'],
    'T': ['FY'],
    'Y': ['*FY', 'e'],
    'F': ['id', '(E)']

}
first = {
    'F': {'id': ['id'], '(E)': ['(']},
    'Y': {'*FY': ['*'], 'e': ['e']},
    'T': {'FY': ['id', '(']},
    'X': {'+TX': ['+'], 'e': ['e']},
    'E': {'TX': ['id', '(']},
}

follow = {
    "E": [')', '$'],
    'X': [')', '$'],
    'T': ['+', ')', '$'],
    'Y': ['+', ')', '$'],
    'F': ['+', '*', ')', '$']
}


def ll1(data, first, follow):
    terminal = []
    l = {}
    for i in first:
        for j in first[i]:
            for k in first[i][j]:
                if k != 'e':
                    l[i, k] = j
                    terminal.append(k)
                else:
                    for a in follow[i]:
                        l[i, a] = j
    for i in follow:
        for j in follow[i]:
            if j != '$':
                terminal.append(j)
    terminal = list(set(terminal))
    key = l.keys()
    terminal = sorted(terminal)
    terminal.append('$')
    
    for i in terminal:
        print("\t\t\t  " + i, end='')
    print("\n", "=" * 80)
    for i in data:
        print(i + "\t\t", end='')
        for j in terminal:
            if ((i, j) in key):
                print(f"| {i}--->{l[i, j]}\t", end='')
            else:
                print("| \t\t\t", end='')

        print("\n", "=" * 80)


ll1(data, first, follow)
