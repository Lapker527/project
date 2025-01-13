import json
import os

class Entry:
    def __init__(self, title):
        self.title = title
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def json(self):
        return {
            "title": self.title,
            "entries": [entry.json() for entry in self.entries]
        }

    @classmethod
    def from_json(cls, data):
        """Создает объект класса cls из JSON-данных."""
        entry = cls(data['title'])
        for sub_entry in data.get('entries', []):
            entry.add_entry(cls.from_json(sub_entry))
        return entry
    @classmethod
    def load(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
                content = json.load(f)

    def save(self, path):
        filename = f'{self.title}.json'
        full_path = os.path.join(path, filename)

        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(self.json(), f, ensure_ascii=False, indent=4)

grocery_list = {
    "title": "Продукты",
    "entries": [
        {
            "title": "Молочные",
            "entries": [
                {
                    "title": "Йогурт",
                    "entries": []
                },
                {
                    "title": "Сыр",
                    "entries": []
                }
            ]
        }
    ]
}

entry = Entry.from_json(grocery_list)
entry.save('C:\\Users\\avosa\\PycharmProjects')
loaded_entry = Entry.load('C:\\Users\\avosa\\PycharmProjects\\Продукты.json')

if loaded_entry:
    print(f'Загружено: {loaded_entry.title}')
    for sub_entry in loaded_entry.entries:
        print(f' - {sub_entry.title}')