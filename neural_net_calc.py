from math import e

x = [1, 1, 1]
w1 = [[0.4, 0.2, 0.9], [0.3, 0.1, 0.4]]
w2 = [[0.8, 0.7], [-0.6, -0.4]]
target_outputs = [1, 0]

def calculate(x, w1, w2, target_outputs):
    print('Calculate h')
    print('-'*20)
    hidden_nodes = []
    for i, values in enumerate(w1):
        s = 0
        equation_string = ''
        for j, node in enumerate(values):
            s += node * x[j]
            equation_string += f'{node} * {x[j]} + '
        equation_string = equation_string[:-3] + f' = {s:.3f}'
        print(equation_string)
        h = 1/(1+pow(e, -s))
        print(f'h{i+1} = 1/(1+e^-{s:.3f}) = {h:.3f}\n')
        hidden_nodes.append(h)


    print('\nCalculate o')
    print('-'*20)
    output_nodes = []
    for i, values in enumerate(w2):
        s = 0
        equation_string = ''
        for j, node in enumerate(values):
            s += node * hidden_nodes[j]
            equation_string += f'{node} * {hidden_nodes[j]:.3f} + '
        equation_string = equation_string[:-3] + f' = {s:.3f}'
        print(equation_string)
        o = 1/(1+pow(e, -s))
        print(f'o{i+1} = 1/(1+e^{-1*s:.3f}) = {o:.3f}\n')
        output_nodes.append(o)
        

    print('\nCalculate d2')
    print('-'*20)
    output_node_errors = []
    for i, node in enumerate(output_nodes):
        node_error = node * (1 - node) * (target_outputs[i] - node)
        print(f'd{i+1}: {node:.3f} * (1 - {node:.3f}) * ({target_outputs[i]} - {node:.3f}) = {node_error:.3f}')
        output_node_errors.append(node_error)


    print('\nCalculate d1')
    print('-'*20)
    hidden_node_errors = []
    for i in range(len(w2)):
        s = 0
        equation_string = ''
        for j, one in enumerate(output_node_errors):
            s += one * w2[j][i]
            equation_string += f'{one:.3f} * {w2[j][i]:.3f} + '
        equation_string = equation_string[:-3] + f' = {s:.3f}'
        hi = hidden_nodes[i] * (1 - hidden_nodes[i]) * s
        print(equation_string)
        print(f'h{i+1}: {hidden_nodes[i]:.3f} * (1 - {hidden_nodes[i]:.3f}) * {s:.3f} = {hi:.3f}\n')
            


calculate(x, w1, w2, target_outputs)
