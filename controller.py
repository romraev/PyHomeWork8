import view as v
import model as m
import text as t


def start():
    pb = m.Phonebook()
    while True:
        select = v.menu()
        match select:
            case 1:
                if pb.open_file():
                    v.print_message(t.load_successful)
                else:
                    v.print_message(t.load_error)
            case 2:
                if pb.save_file():
                    v.print_message(t.save_successful)
                else:
                    v.print_message(t.save_error)
            case 3:
                v.show_contacts(pb.get(), t.empty_book)
            case 4:
                new = v.add_contact()
                pb.add_contact(new)
                v.print_message(t.add_successful(new.get('name')))
            case 5:
                word = v.search_word()
                result = pb.search(word)
                v.show_contacts(result, t.empty_search(word))
            case 6:
                word = v.search_word()
                result = pb.search(word)
                if len(result) != 0:
                    v.show_contacts(result, t.empty_search(word))
                    i = v.select_id(t.upd_contact)
                    new = v.add_contact()
                    pb.change_contact(i, new)
                    v.print_message(t.upd_successful(new.get('name')))
                else:
                    v.print_message(t.empty_search(word))
            case 7:
                word = v.search_word()
                result = pb.search(word)
                if len(result) != 0:
                    v.show_contacts(result, t.empty_search(word))
                    i = v.select_id(t.del_contact)
                    deleted = pb.delete_contact(i)
                    v.print_message(t.del_successful(deleted.get('name')))
                else:
                    v.print_message(t.empty_search(word))
            case 8:
                if pb.check_on_exit():
                    answer = v.search_word(t.change_confirm)
                    if answer != 'n':
                        pb.save_file()
                v.print_message(t.goodbye)
                break