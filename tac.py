def generate_tac(expression):
    temp_count = 0
    code = []
    tokens = tokenize(expression)
    output_queue, operator_stack = [], []

    for token in tokens:
        if token.isalnum():
            output_queue.append(token)
        elif token in {'+', '-', '*', '/', '^'}:
            while operator_stack and has_higher_precedence(operator_stack[-1], token):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    output_queue.extend(reversed(operator_stack))
    build_tac(output_queue, temp_count, code)
    return code

def tokenize(expression):
    tokens = []
    current_token = ''
    for char in expression:
        if char.isalnum():
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens

def has_higher_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence.get(op1, 0) >= precedence.get(op2, 0)

def build_tac(tokens, temp_count, code):
    operand_stack = []
    for token in tokens:
        if token.isalnum():
            operand_stack.append(token)
        elif token in {'+', '-', '*', '/', '^'}:
            operand2, operand1 = operand_stack.pop(), operand_stack.pop()
            result_var = f't{temp_count}'
            temp_count += 1
            code.append(f'{result_var} = {operand1} {token} {operand2}')
            operand_stack.append(result_var)

# Example usage:
if __name__ == "__main__":
    expression = "a = ( b * c) + 12 * ( e /f ) ^ g"
    tac = generate_tac(expression)
    print("Three Address Code (TAC) for expression:", expression)
    for statement in tac:
        print(statement)
