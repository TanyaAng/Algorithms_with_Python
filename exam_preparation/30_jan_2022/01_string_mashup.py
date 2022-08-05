def is_lexicographical_order(array):
    if sorted(array) == array:
        return True
    return False


def string_mashup(idx, letters, vector):
    if idx >= len(vector):
        if is_lexicographical_order(vector):
            print(*vector, sep='')
        return
    for i in range(len(letters)):
        vector[idx] = letters[i]
        string_mashup(idx+1,letters,vector)


letters = sorted(list(input()))
n = int(input())
vector = [''] * n
string_mashup(0, letters, vector)
