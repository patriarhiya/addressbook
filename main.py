FILE_NAME = 'phone_directory.txt'
ID = 'id'
FIRST_NAME = 'имя'
LAST_NAME = 'фамилия'
SECOND_NAME = 'отчество'
PHONE = 'телефон'
HEADERS = [ID, LAST_NAME, FIRST_NAME, SECOND_NAME, PHONE]
ANSWER = {'y', 'yes', 'да'}


def load_date():
    """Загрузка данных в память"""
    date = []
    with open(FILE_NAME, 'r') as file:
        for i, line in enumerate(file, start = 1):
            row = [i] + line.strip().split()
            date.append(dict(zip(HEADERS, row)))

    return date

def print_date(date):
    """Вывод всех данных на экран"""
    for item in date:
        print(*(f"{k}: {v:<16}" for k, v in item.items()))  # без звездочки выводится просто объкт, почему так?

def add_new_contact(date):
    """Добавление нового контакта в базу"""
    row = input('Введите ФИО и телефон через пробел: ').split()
    line = [len(date) + 1] + [item.strip().capitalize() for item in row]
    date.append(dict(zip(HEADERS, line)))
    print("Данные добавлены")


def find_date_by_key(key: str, value: str, date: list[dict[str, str]]):
    """Поиск совпадения значения в данных п столбцу"""
    for item in date:
        if item[key] == value:
            print(item)


def delete_contact_by_id(number: str, date):
    """Удаляем строку в данных по 'id' """
    id_num = int(number)
    if number.isdigit() and id_num <= len(date):
        print(*(f"{k}: {v:<16}" for k, v in date[id_num - 1].items()))
        question = input("Удаляем (y/n): ")
        if question in ANSWER:
            date.pop(id_num - 1)
            print('Запись успешно удалена')
    else:
        print(f"Записи под таким номером - {ID} нет. ")


def edit_cell_last_name(old_last_name: str, date):
    """Запрашиваем новую фамилию и заменяем ее в данных"""
    new_last_name = input("Введите новую фамилию для замены: ")
    new_last_name.strip().capitalize()
    for item in date:
        if item[LAST_NAME] == old_last_name:
            item[LAST_NAME] = new_last_name
            print("Замена фамилии в данных прошла успешно")
            print(*(f"{k}: {v:<16}" for k, v in item.items()))


def delete_cell_by_first_name(name: str, date):
    """Удалем ячейку по совпадению"""
    for item in date:
        if item[FIRST_NAME] == name:
            print(*(f"{k}: {v:<16}" for k, v in item.items()))
            date.remove(item)
            print("Удаление ячейки прошло успешно")
            break

def copy_date_in_file(numer_row: str, date):
    """Копируем строку number в новый файл"""
    id_num = int(numer_row)
    if numer_row.isdigit() and id_num <= len(date):
        print(*(f"{k}: {v:<16}" for k, v in date[id_num - 1].items()))
        with open('new_file.txt', 'w', encoding='utf-8') as file:
                file.write(' '.join(f"{v}" for k, v in date[id_num - 1].items() if k != ID) + "\n")
        print("Файл создан и в него успешно дбавлена строка")



def main(date):
    while True:
        print(f'''\nЧто вы хотите сделать?
        1: Вывести все данные
        2: Записать новый контакт
        3: Найти контакт по полю - "{LAST_NAME}"
        4: Удалить контакт по полю - "{ID}"
        5: Изменить поле - "{LAST_NAME}"
        6: Удалить данные по полю - "{FIRST_NAME}"
        7: Скопировать данные по полю - "{ID}" в новый файл
        0: Выйти''')

        x = input('Ваш выбор: ')

        if x == "1":
            print_date(date)
        elif x == "2":
            add_new_contact(date)
        elif x == "3":
            user_iput = input(f'{LAST_NAME.title()}: ')
            user_iput.strip().capitalize()
            find_date_by_key(key=LAST_NAME, value=user_iput, date=date)
        elif x == "4":
            num_cell = input("Введите номер поля, которое хотите удалить: ")
            delete_contact_by_id(number=num_cell, date=date)
        elif x == "5":
            old_last_name = input("Введите фамилию, которую нужно заменить: ")
            old_last_name.strip().capitalize()
            edit_cell_last_name(old_last_name=old_last_name, date=date)
        elif x == "6":
            name = input("Введите имя, которое необходимо удалить: ")
            name.strip().capitalize()
            delete_cell_by_first_name(name=name, date=date)
        elif x == "7":
            num = input("Введите номер строки, которую хотите скопировать в новый файл: ")
            copy_date_in_file(numer_row=num, date=date)
        elif x == "0":
            break
        else:
            print("неверная команда")


main(load_date())