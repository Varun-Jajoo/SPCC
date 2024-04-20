def main():
    input_str = "a=b*c+d*e"
    print(f"Tac of the string {input_str}: ")
    input_split = input_str.split("=")
    input_char = list(input_split[1])
    t = [['' for _ in range(3)] for _ in range(3)]
    count = 0
    t_val = ''

    for i in range(len(input_char)):
        if input_char[i] in ['/', '*', '%']:
            t[count][0] = input_char[i - 1]
            t[count][1] = input_char[i]
            t[count][2] = input_char[i + 1]
            count += 1
        if input_char[i] in ['+', '-']:
            t[2][0] = '1'
            t[2][1] = input_char[i]
            t[2][2] = '2'

    for i in range(3):
        if i == 0:
            t_val = "t1"
        elif i == 1:
            t_val = "t2"
        else:
            t_val = "t3"
        print("\n" + t_val + "=", end="")
        for j in range(3):
            if i == 2:
                if j == 0 or j == 2:
                    print("t" + t[i][j], end="")
                else:
                    print(t[i][j], end="")
            else:
                print(t[i][j], end="")
    print("\n" + input_split[0] + "=" + t_val)

main()
