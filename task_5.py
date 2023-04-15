"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet as chardet


def ping(host_name):
    args = ["ping", host_name]
    ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in ya_ping.stdout:
        res = chardet.detect(line)
        # print(res)
        print(line.decode(encoding=res["encoding"]))


ping("yandex.ru")
print("------------------------------------")
ping("youtube.com")
