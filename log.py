def print_result(name_contact='', phone_number=''):
    with open('result.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{name_contact} - {phone_number} \n')


def watch_list():
    file = 'result.txt'
    data = open(file, 'r')
    for line in data:
        print(line)
    data.close()