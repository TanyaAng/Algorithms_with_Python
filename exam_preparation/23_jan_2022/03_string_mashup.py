def string_mashup(string, result):
    n = len(string)
    mx = 2 ** n
    string = string.lower()

    for i in range(mx):
        combination = [k for k in string]
        for j in range(n):
            # if (((i >> j) & 1) == 1):
            temp = i // (2 ** j)
            if temp & 1 == 1:
                combination[j] = string[j].upper()

        combination_as_string = ""
        for i in combination:
            combination_as_string += i
        result.add(combination_as_string)


result = set()
string_mashup('x1y2z', result)
print(*result, sep='\n')
