
def find(arr , value):
    for i in arr:
        if i == value:
            return True
    return False


data = [ ['E', ['TA']], ['A', ['aTA', 'è']], ['T', ['FB']], ['B', ['bFB', 'è']], ['F', ['c', 'dEf']] ]

first = {
    "TA" : ['d', 'c'],
    "aTA" : ['a'],
    'FB': ['c', 'd'],
    'bFB' : ['b'],
    'c' : ['c'],
    'dEf' : ['d']
}

follow = {
    "E" : ['$'],
    'A' : ['$', 'f'],
    'T' : ['a', '$', 'f'],
    'B' : ['a', '$', 'f'],
    'F' : ['b', 'a' , '$', 'f']

}

terminals = []
nonT = []

for i in range(len(data)):
    nonT.append(data[i][0])
    for j in data[i][1]:
        for k in j:
            #print(k)
            if k.islower() and k != 'è' and not find(terminals, k):
                terminals.append(k)

terminals.append("$")

print("Terminals : ", " ".join(terminals))
print("\nFirst :")
for k, v in first.items():
    print(k, " -> " ," ,".join(v))

print("\nFollow :")

for k, v in follow.items():
    print(k, " -> " , " ,".join(v))

table = {}

for i in range(len(nonT)):
    table[nonT[i]] = {}
    for j in terminals:
        table[nonT[i]][j] = []


for i in range(len(data)):
    left = data[i][0]
    #print(left)
    right = data[i][1]
    #print(right)

    for j in right:
        #print(j)
        if j == "è":
            for itr in follow[left]:
                #print(itr)
                table[left][itr].append(f'{left}->{j}')
        else:
            for itr in first[j]:
                #print(itr)
                table[left][itr].append(f'{left}->{j}')
                #print(table)


print("\nParsing Table :")
for i in terminals:
    print(f' \t{i}', end="")
print()

for non_term in nonT:
    print(non_term, end="\t")
    for term in terminals:
        productions = table[non_term][term]
        if productions:
            print(" ".join(productions), end=" ")
        print("\t", end="")
    print()
