phone_book = {}
path: str = 'list.txt'

def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    # print(data)
    file.close()
    for i, contact in enumerate(data):  # захотелось всё-таки отсортировать по алфавиту, поэтому сделал enumerate, чтобы непостоянные были id
        nc = contact.strip().split(':')
        phone_book[i+1] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    print('\nТелефонная книга успешно загружена'.ljust(100, "="))

def show_contacts(book: dict[int, dict]):
    print('\n' + '=' * 100)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 100 + '\n')

def add_contact():
    uid = max(list(phone_book.keys())) + 1
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}
    print('\n' + '=' * 100)
    print(f'\nКонтакт {name} успешно добавлен! '.ljust(100, "="))
    print('=' * 100 + '\n')

def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    new_data = sorted(data, key=lambda item: item[2]) # тут получается сортировка по алфавиту по первой букве имени
    new_data = '\n'.join(new_data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(new_data)
    print('\n' + '=' * 100)
    print(f'\nТелефонная книга успешно сохранена!'.ljust(100, "="))
    print('=' * 100 + '\n')
    open_file() # ещё раз запускаю чтобы обновить phone_book

def search():
    result = {}
    count = 0
    word = input('Введите слово по которому будет производиться поиск: ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
            count+=1
    print('\n' + '=' * 100)
    print(f'Найдено {count} совпадений: ') # чисто так, для красоты))
    return result

def remove():
    result = search()
    show_contacts(result)
    index = int(input('Введите ID контакта, которого хотите удалить: '))
    del_cnt = phone_book.pop(index)
    print('\n' + '=' * 100)
    print(f'\nКонтакт {del_cnt.get("name")} успешно удалён! '.ljust(100, "="))
    print('=' * 100 + '\n')

def change(): # пошел по легкому пути, но самому верному)
    result = search()
    show_contacts(result)
    index = int(input('Введите ID контакта, которого хотите изменить: '))
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[index] = {'name': name, 'phone': phone, 'comment': comment}
    print('\n' + '=' * 100)
    print(f'\nКонтакт {name} успешно изменён! '.ljust(100, "="))
    print('=' * 100 + '\n')

def menu() -> int:
    main_menu = ''' Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход '''
    print(main_menu)
    while True:
        select = input('Выберете пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода')

open_file()
while True:
    select=menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacts(result)
        case 6:
            change()
        case 7:
            remove()
        case 8:
            print("До свидания! До новых встреч")
            break