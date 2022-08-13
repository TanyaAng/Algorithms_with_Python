expression = input().split()
expression_idx = []

for i in range(len(expression)):
    if expression[i] == '?':
        expression_idx.append(i)

current_result = None
for idx in reversed(expression_idx):
    expected = expression[idx - 1]
    if_true = expression[idx + 1]
    if_false = expression[idx + 3]
    if expected == 't':
        current_result = if_true
    else:
        current_result = if_false
    expression.insert(idx + 4, current_result)
    expression = expression[0:idx - 1] + expression[idx + 4:]

print(current_result)
