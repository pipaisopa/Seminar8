def work_with_phonebool():
    choise = show_menu()
    
    phone_book = read_txt('phone.txt')

    while (choise!=7):
        if choise == 1:
            print_result(phone_book)
        elif choise == 2:
            last_name = input('lastname')
            print(find_by_lastname(phone_book, last_name))    
        elif choise == 3:
            last_name = input('lastname')
            new_number = input('new number')
            print(change_number(phone_book, last_name, new_number))    
        elif choise == 4:
            last_name = input('lastname')
            print(delete_by_lastname(phone_book, last_name))
        elif choise == 5:
            number = input('number')
            print(find_by_number(phone_book,number))
        elif choise == 6:
            user_data = input('new data')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)            






def add_user():
    return

def find_by_number():
    return

def delete_by_lastname():
    return

def change_number():
    return

def find_by_lastname():
    return

def print_result():
    return

def read_txt(filename): 

    phone_book=[]

    fields= ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	

    return phone_book

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
                изменить данные
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choise = int(input())
    return choise

def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')     