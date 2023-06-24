import text as t

def menu() -> int:
    print(t.main_menu[0])
    for i in range(1, len(t.main_menu)):
        print(f'\t{i}. {t.main_menu[i]}')
    select = input(t.select_menu)
    if select.isdigit() and 0 < int(select) < (len(t.main_menu)):
        return int(select)
    print(t.input_error)

def add_contact():
    new = {}
    for key, value in t.new_contact.items():
        new[key] = input(value)
    return new

def show_contacts(book: dict[int: dict[str, str]], message):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for contact in book.values():
            max_name.append(len(contact.get('name')))
            max_phone.append(len(contact.get('phone')))
            max_comment.append(len(contact.get('comment')))
        size_name = max(max_name)
        size_phone = max(max_phone)
        size_comment = max(max_comment)
        print('\n' + '=' * (size_name + size_phone + size_comment + 7))
        for index, contact in book.items():
            print(f'{index:>3}. {contact.get("name"):<{size_name}} {contact.get("phone"):<{size_phone}} {contact.get("comment"):<{size_comment}}')
        print('=' * (size_name + size_phone + size_comment + 7) + '\n')
    else: 
        print(message)

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

def search_word() -> str:
    return input(t.search_word)

def select_id(text) -> int:
    id = input(text)
    return id