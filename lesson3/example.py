word = input()
def int_func(word):
    word = word[0].upper() + word[1:]
    return word
print(int_func(word))


source = input().split()
res = []
for word in source:
    res.append(int_func(word))
print(' '.join(res))