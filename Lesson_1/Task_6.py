# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной
# кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.

import locale

from chardet import detect



# узнаем кодировку файла
with open('test_file.txt', 'rb') as f:
    content = f.read()

encoding = detect(content)['encoding']
print('encoding - ', encoding)

# Читаем из файла
with open('test_file.txt', 'r', encoding=encoding) as f:
    for i in f:
        print(i, end='')
    f.seek(0)