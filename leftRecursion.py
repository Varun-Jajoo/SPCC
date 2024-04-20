productions = [
    "E->EA|A",
    "A->AT|a",
    "T->a",
    "E->i"
]

for production in productions:
    print("\nGRAMMAR:", production)
    non_terminal = production[0]
    index = 3  # starting of the string following "->"
    if non_terminal == production[index]:
        alpha = production[index + 1]
        print(" is left recursive.")
        while index < len(production) and production[index] != '|' and production[index] != '\0':
            index += 1
        if index < len(production):
            beta = production[index + 1]
            print("Grammar without left recursion:")
            print(f"{non_terminal}->{beta}{non_terminal}'")
            print(f"{non_terminal}'->{alpha}{non_terminal}'|E")
        else:
            print(" can't be reduced")
    else:
        print(" is not left recursive.")
