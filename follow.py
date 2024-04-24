data = {
   "S":['aBDh'],
   'B':['cC'],
   'C':['bC','e'],
   'D':['EF'],
   'E':['g','e'],
   'F':['f','e']
}

first = {
   "S":['a'],
   'B':['c'],
   'C':['b','e'],
   'D':['g','f','e'],
   'E':['g','e'],
   'F':['f','e']
}
opp={}
follow = {}

# data = {
#     'S': ['TE'],
#     'E': ['+TE', 'e'],
#     'T': ['FY'],
#     'Y': ['*FY', 'e'],
#     'F': ['(S)', 'id']
# }
# first = {
#     'F': ['(', 'i'],
#     'Y': ['*', 'e'],
#     'T': ['(', 'i'],
#     'E': ['+', 'e'],
#     'S': ['(', 'i']
# }
# opp = ['(', ')', '+', '*', '-']


def fol(i, follow):
    temp = []
    if i == "S":
        temp.append("$")
    for j in data:
        for k in data[j]:
            Index = k.find(i)
            if Index == -1:
                continue
            p = Index + 1
            if p != len(k):
                print(k[p])
                if k[p].islower() or k[p] in opp:
                    temp.append(k[p])
                else:
                    for u in first[k[p]]:
                        if 'e' != u:
                            print("uuuu", u)
                            temp.append(u)
                    for u in fol(k[p], follow):
                        temp.append(u)
            else:
                if i != j:
                    for o in follow[j]:
                        if o != 'e':
                            print("hello    ", o)
                            temp.append(o)

    return temp


for i in data:
    temp = fol(i, follow)

    follow[i] = list(set(temp))
    print("temp", follow)

print("Follow : ")
print(follow)
