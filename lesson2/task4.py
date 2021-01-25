# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

words = input('Введите несколько слов разделенных пробелами: ');
oneWord = list();
numb = 1;
for i in range(words.count(' ') + 1):
    oneWord = words.split();
    if len(str(oneWord)) <= 10:
        print(f" {numb} {oneWord [i]}");
        numb += 1;
    else:
        print(f" {numb}) {oneWord [i] [0:10]}");
        numb += 1;