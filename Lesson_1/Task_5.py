# Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат из байтовового
# типа данных в строковый без ошибок для любой кодировки операционной системы.

import subprocess


yandex = ['ping', 'yandex.ru']
youtube = ['ping', 'youtube.com']
subprocess_yandex = subprocess.Popen(yandex, stdout=subprocess.PIPE)
subprocess_youtube = subprocess.Popen(youtube, stdout=subprocess.PIPE)

for line in subprocess_yandex.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'), end='')


for line in subprocess_youtube.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'), end='')