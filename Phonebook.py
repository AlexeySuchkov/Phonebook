class Contact:
    def __init__(self, name, surname, phone_number, favorite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.additional_information = kwargs

    def __str__(self):
        result = [
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Телефон: {self.phone_number}',
            f'В избранных: {"да" if self.favorite else "нет"}'
        ]
        if self.additional_information:
            result.append('Дополнительная информация:')
            for key, value in self.additional_information.items():
                result.append(f'\t{key}: {value}')
        return '\n'.join(result)

    def __repr__(self):
        return self.__str__()


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def display(self):
        print('*' * 50)
        print('Список контактов:')
        for contact in self.contacts:
            print(contact)
        print('*' * 50)

    def add(self, *args, **kwargs):
        print('*' * 50)
        self.contacts.append(Contact(*args, **kwargs))
        print('Контакт добавлен.')
        print('*' * 50)

    def delete_by_phone(self, phone_number):
        print('*' * 50)
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                self.contacts.remove(contact)
                print(f'Удален контакт с номером {phone_number}')
                print('*' * 50)
                return
        print(f'Контакт с номером {phone_number} не существует.')
        print('*' * 50)

    def get_favorites(self):
        print('*' * 50)
        print('Список избранных контактов')
        for contact in (contact for contact in self.contacts if contact.favorite):
            print(contact)
        print('*' * 50)

    def find_by_name(self, name, surname):
        print('*' * 50)
        print(f'Найденные контакты с именем и фамилий {name} {surname}')
        for contacts in (contact for contact in self.contacts if contact.name == name and contact.surname == surname):
            print(contacts)
        print('*' * 50)


if __name__ == "__main__":
    pb = PhoneBook('pb')
    pb.add('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    pb.add('John', 'Smith', '+71234567890', telegram='@johnny', email='john@smith.com', favorite=True)
    pb.add('Mary', 'Smith', '+71238673088', telegram='@mary', email='mary@smith.com')
    pb.add('Michael', 'Smith', '+71236925431', telegram='@Mike', email='mike@smith.com')
    pb.display()
    pb.delete_by_phone('+71234567809')
    pb.get_favorites()
    pb.find_by_name(*'Michael Smith'.split(' '))
