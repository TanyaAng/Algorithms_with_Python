def find_matches(text, word, vector, idx=0):
    if text == [] or len(word) == sum(len(x) for x in vector):
        print(*vector, sep=' ')
        return
    if word.startswith(text[idx]):
        first_word = text[idx]
        text.remove(first_word)
        vector.append(first_word)
        find_matches(text, word[len(first_word):], vector, idx=0)
    else:
        find_matches(text, word, vector, idx + 1)


text = input().split(', ')
searched_word = input()
vector = []

find_matches(text, searched_word, vector)

# text=['asd','asd','a']
# print(sum(len(x) for x in text))