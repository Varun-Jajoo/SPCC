data = [
    ['S', ['aBDh']],
    ['B', ['cC']],
    ['C', ['bC', 'è']],
    ['D', ['EF']],
    ['E', ['g', 'è']],
    ['F', ['f', 'è']]
]

first = {
    'S': {'a'},
    'B': {'c'},
    'C': {'b', 'è'},
    'D': {'g', 'f', 'è'},
    'E': {'g', 'è'},
    'F': {'f', 'è'}
}

follow = {}

for i in range(len(data)):
    left = data[i][0]
    temp_follow = set()

    if i == 0:
        temp_follow.add("$")

    for j in range(len(data)):
        for k in data[j][1]:
            index = k.find(left)

            if index == -1:
                continue

            # NT at end
            if index == len(k) - 1:
                if left != data[j][0]:
                    for ele in follow[data[j][0]]:
                        temp_follow.add(ele)

            # T after NT in follow
            elif k[index + 1].islower():
                temp_follow.add(k[index + 1])

            # NT after NT in follow
            else:
                next_index = index + 1
                while next_index < len(k):
                    next_symbol = k[next_index]
                    if next_symbol.islower():
                        temp_follow.add(next_symbol)
                        break
                    else:
                        for ele in first[next_symbol]:
                            if ele != 'è':
                                temp_follow.add(ele)
                        if 'è' not in first[next_symbol]:
                            break
                        next_index += 1
                if next_index == len(k):
                    if left != data[j][0]:
                        for ele in follow[data[j][0]]:
                            temp_follow.add(ele)

    follow[left] = temp_follow

print("Follow : ")
print(follow)
