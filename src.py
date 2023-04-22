# импортируем модуль для работы с файлами и папками
import os
import shutil

# задаем путь к папке localization
loc_path = "path"

# создаем папку russian внутри localization, если ее нет
rus_path = os.path.join(loc_path, "russian")
if not os.path.exists(rus_path):
    os.mkdir(rus_path)

# получаем список файлов и папок внутри english
eng_path = os.path.join(loc_path, "english")
eng_items = os.listdir(eng_path)

# проходим по всем элементам внутри english
for item in eng_items:
    # получаем полный путь к элементу
    item_path = os.path.join(eng_path, item)
    # если это файл с расширением .yml
    if item.endswith(".yml"):
        # получаем новое имя файла с _russian вместо _english
        new_name = item.replace("_english", "_russian")
        # получаем полный путь к новому файлу в папке russian
        new_path = os.path.join(rus_path, new_name)
        # копируем файл из english в russian
        shutil.copy(item_path, new_path)
        # открываем новый файл для чтения и записи
        with open(new_path, "r+", encoding="utf-8") as f:
            # читаем содержимое файла в список строк
            lines = f.readlines()
            # если первая строка начинается с l_english:
            if lines[0].startswith("﻿l_english:"):
                # заменяем начало строки на l_russian:
                lines[0] = lines[0].replace("﻿l_english:", "﻿l_russian:")
                # переходим в начало файла
                f.seek(0)
                # записываем измененный список строк в файл
                f.writelines(lines)
                # обрезаем лишние символы в конце файла
                f.truncate()
    # если это папка
    elif os.path.isdir(item_path):
        # создаем такую же папку внутри russian, если ее нет
        sub_rus_path = os.path.join(rus_path, item)
        if not os.path.exists(sub_rus_path):
            os.mkdir(sub_rus_path)
        # получаем список файлов и папок внутри этой папки
        sub_eng_items = os.listdir(item_path)
        # проходим по всем элементам внутри этой папки (аналогично предыдущему циклу)
        for sub_item in sub_eng_items:
            sub_item_path = os.path.join(item_path, sub_item)
            if sub_item.endswith(".yml"):
                new_name = sub_item.replace("_english", "_russian")
                new_path = os.path.join(sub_rus_path, new_name)
                shutil.copy(sub_item_path, new_path)
                with open(new_path, "r+", encoding="utf-8") as f:
                    lines = f.readlines()
                    if lines[0].startswith("﻿l_english:"):
                        lines[0] = lines[0].replace("﻿l_english:", "﻿l_russian:")
                        f.seek(0)
                        f.writelines(lines)
                        f.truncate()
