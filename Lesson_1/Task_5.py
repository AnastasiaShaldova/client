# Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат из байтовового
# типа данных в строковый без ошибок для любой кодировки операционной системы.
import platform
import subprocess

from chardet import detect

def ping_url(domain):
    ping = ['ping', domain]

    url_subprocess = subprocess.Popen(ping, stdout=subprocess.PIPE)

    for line in url_subprocess.stdout:
        result = detect(line)
        encoded_line = line.decode(result['encoding']).encode(encoding='utf8')
        print(encoded_line.decode(encoding='utf8'))

ping_url('yandex.ru')
ping_url('youtube.com')