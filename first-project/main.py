FILENAME = 'contacts.txt'

# считываем контакты из файла
def load_contacts():
    contacts = []
    try:
        with open(FILENAME, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, phone = line.strip().split(',')
                contacts.append({'name': name, 'phone': phone})
    except FileNotFoundError:
        pass
    return contacts

# сохраняем текущий список контактов в файл
def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

# добавляем новый контакт
def add_contact(contacts):
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    contacts.append({'name': name, 'phone': phone})
    save_contacts(contacts)
    print("Контакт добавлен.")

# удаляем контакт
def remove_contact(contacts):
    name = input("Введите имя контакта, который хотите удалить: ")
    phone = input("Введите номер телефона контакта, который хотите удалить: ")
    initial_len = len(contacts)
    contacts = [contact for contact in contacts if not (contact['name'] == name and contact['phone'] == phone)]
    if len(contacts) < initial_len:
        save_contacts(contacts)
        print("Контакт удален.")
    else:
        print("Контакт не найден.")

# редактируем контакт
def edit_contact(contacts):
    name = input("Введите имя контакта, который хотите редактировать: ")
    phone = input("Введите номер телефона контакта, который хотите редактировать: ")
    for contact in contacts:
        if contact['name'] == name and contact['phone'] == phone:
            contact['phone'] = input(f"Введите новый номер телефона (текущий: {contact['phone']}): ")
            save_contacts(contacts)
            print("Контакт обновлен.")
            return
    print("Контакт не найден.")

# выводим все контакты
def view_contacts(contacts):
    if not contacts:
        print("Список контактов пуст.")
    else:
        for contact in contacts:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")

def main():
    contacts = load_contacts()
    while True:
        print("\nМеню:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Редактировать контакт")
        print("4. Просмотреть контакты")
        print("5. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            remove_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            view_contacts(contacts)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
