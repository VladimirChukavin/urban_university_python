# Домашнее задание по теме "Позиционирование в файле"


def custom_write(file_name, strings):
    byte_list = []

    file_write = open(file_name, "w", encoding="utf-8")
    for string in strings:
        byte_list.append(file_write.tell())
        file_write.write(f"{string}\n")
    file_write.close()

    file_read = open(file_name, "r", encoding="utf-8")
    text_list = file_read.readlines()
    text_dict = {
        (i + 1, byte_list[i]): text_list[i].rstrip("\n") for i in range(len(text_list))
    }
    file_read.close()

    return text_dict


info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)

for elem in result.items():
    print(elem)
