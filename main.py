def work_with_phonebook():
    choice = show_menu()
    
    phone_book = read_txt('phone.txt')

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname: ')
            print(find_by_lastname(phone_book, last_name))    
        elif choice == 3:
            last_name = input('lastname: ')
            new_number = input('new number: ')
            print(change_number(phone_book, last_name, new_number))    
        elif choice == 4:
            last_name = input('lastname: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('number: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data: ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:
            copy_line_to_another_file()
        
        choice = show_menu()

def copy_line_to_another_file():
    try:
        source_filename = 'phone.txt'
        destination_filename = input("Введите имя файла для копирования: ")
        line_number = int(input("Введите номер строки для копирования: "))

        with open(source_filename, 'r', encoding='utf-8') as src_file:
            lines = src_file.readlines()
            print(f"Количество строк в исходном файле: {len(lines)}")

            # Проверка диапазона
            if line_number < 1 or line_number > len(lines):
                print("Ошибка: Номер строки выходит за пределы допустимого диапазона.")
                return

            line_to_copy = lines[line_number - 1].strip()  # Убираем символы новой строки
            print(f"Скопированная строка: {line_to_copy}")

        with open(destination_filename, 'a', encoding='utf-8') as dest_file:
            dest_file.write(line_to_copy + '\n')  # Добавляем символ новой строки

        print(f"Строка номер {line_number} успешно скопирована в файл {destination_filename}.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

def find_by_number(phone_book, number):
    for record in phone_book:
        if record['Телефон'].strip() == number:
            return record
    return None

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'].strip() == last_name:
            phone_book.remove(record)
            return True
    return False

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'].strip() == last_name:
            record['Телефон'] = new_number
            return True
    return False

def find_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'].strip() == last_name:
            return record
    return None

def print_result(phone_book):
    for record in phone_book:
        print(record)

def read_txt(filename): 
    phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        lines = phb.readlines()
        for line in lines:
            if line.strip(): #пропускаем пустые строки
                record = dict(zip(fields, line.strip().split(',')))
                phone_book.append(record)

    return phone_book

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер телефона абонента\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Копировать строку в другой файл\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

if __name__ == "__main__":
    work_with_phonebook()
