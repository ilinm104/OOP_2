import os

# Чтение содержимого всех трёх файлов
files = ["1.txt", "2.txt", "3.txt"]
lines = {}
for filename in files:
    print(f"Читаю файл {filename}")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines[filename] = f.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")

# Проверка содержимого словаря lines
print("Содержимое словаря lines:")
for k, v in lines.items():
    print(f"{k}: {v[:10]}")  # Показываем первые 10 элементов списка для каждой строки

# Получение количества строк в каждом файле
line_counts = {filename: len(lines[filename]) for filename in files}

# Сортируем файлы по количеству строк
sorted_files = sorted(line_counts, key=lambda x: line_counts[x])

# Объединяем содержимое файлов в одном порядке
with open(r"C:\Python\3\United.txt", "w", encoding="utf-8") as out_file:
    for index, filename in enumerate(sorted_files, start=1):
        out_file.write(f"{index}\n")
        out_file.write(filename + "\n")
        for line_num, line in enumerate(lines[filename], start=1):
            out_file.write(
                f"Строка номер {line_num} файла номер {os.path.basename(filename)} \n"
            )
            out_file.write(line)
