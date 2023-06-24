
import json

class Phonebook:

    def __init__(self, path: str = 'phones.json'):
        self.contact: dict = {}
        self.not_changed = {}
        self.path = path
    
    def get(self, index: int | None = None):
        if index:
            return self.contact.get(index)
        return self.contact

    def open_file(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                self.contact = json.load(file)
                self.not_changed = self.contact.copy()
            return True
        except:
            return False

    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.contact, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False

    def search(self, word: str) -> dict[int:dict[str, str]]:
        result = {}
        for index, contact in self.contact.items():
            if word.lower() in ' '.join(contact.values()).lower():
                result[index] = contact
        return result

    def check_id(self):
        if self.contact:
            return max(list(map(int, self.contact))) + 1
        return 1

    def add_contact(self, new: dict[str, str]):
        contact = {self.check_id(): new}
        self.contact.update(contact)

    def change_contact(self, i: int, cnt: dict[str, str]):
        contact = {i: cnt}
        self.contact.update(contact)

    def delete_contact(self, i: int):
        deleted = self.contact.pop(i)
        return deleted
    
    def check_on_exit(self):
        if self.contact == self.not_changed:
            return False
        else: return True