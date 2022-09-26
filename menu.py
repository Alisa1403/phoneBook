from log import print_result, watch_list

def start():
    var = input('Добро пожаловать в справочник контактов! Выберите, что Вы хотите сделать: \n1-записать новый контакт\n2-посмотреть весь справочник\n')

    if var == '1':
        name_contact = str(input("Введите имя контакта: "))
        phone_number = int(input("Введите номер телефона: "))
        print_result(name_contact, phone_number)
    if var == '2':
        watch_list()