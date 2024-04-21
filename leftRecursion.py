
data = [ ['A', ['ABd','Aa','a']]]

for i in range(len(data)):

    left = data[i][0]
    right = data[i][1]

    alpha = []
    beta = []

    for j in right:
        index = j.find(left)

        if index == -1:
            beta.append(j)
        else:
            alpha.append(j[index + 1:len(j):])

    temp = []
    temp1 = []

    if len(alpha) > 0:
        for itr in beta:
            temp.append(f"{itr}{left}^")
        
        for itr in alpha:
            temp1.append(f"{itr}{left}^")
        
        temp1.append("è")

        data[i][1] = temp
        data.append([f"{left}^", temp1])


print(data)
