# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

import os, time

N = 7
path = r"G:\test_gpb\test"
for file in os.listdir(path):
    if os.stat(os.path.join(path, file)).st_birthtime < time.time() - (N * 86400):
        os.remove(os.path.join(path, file))
