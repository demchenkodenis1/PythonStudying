# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open("file_2.txt", 'r', encoding="utf-8") as my_file:
    print(f'Содержимое файла: \n{my_file.read()}')
with open("file_2.txt", 'r', encoding="utf-8") as my_file:
    lines = 1
    letters = 1
    for line in my_file.readlines():
        lines += line.count('\n')
        letters = line.count('')-1
        print(f'Количество символов строки:\n{line} - {letters}')#не получилось вывести номер строки вместо ее озвучания
    print(f'Количество строк в файле - {lines}')
with open("file_2.txt", 'r', encoding="utf-8") as my_file:
    content = my_file.read()
    content = content.split()
    print(f'Общее количество слов - {len(content)}')
my_file.close()