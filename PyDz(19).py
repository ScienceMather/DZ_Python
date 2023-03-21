

def show_data() -> str:
    '''Эта функция показывает содержимое справочника.'''
    with open('data(PD19).txt', 'r', encoding='utf-8') as file:
        book=file.read()
    return book


def new_data (info: str) -> None:
    '''Добавляет новую информацию в справочник.'''
    with open('data(PD19).txt', 'a', encoding = 'utf-8') as file:
        file.write(f'\n{info}')
        return (f'{info} был добавлен!')


def search_data (info: str) -> str:
    '''Ищет информацию в справочнике.'''
    with open('data(PD19).txt', 'r', encoding = 'utf-8') as file:
        search_list = file.read().split('\n')
        for i in search_list:
            if info in i:
                return (f'{info} Найден!\n{i}')


def change_data (info: str) -> str:
    '''Меняет информацию в справочнике.'''
    with open('data(PD19).txt', 'r+', encoding = 'utf-8') as file:
        search_list = file.read().split('\n')
        for i in search_list:
            if info in i:
                search_list.insert(search_list.index(i),input('Введите новые данные: '))
                search_list.remove(i)
                file.close()
                with open('data(PD19).txt', 'w', encoding = 'utf-8') as file:
                    file.close()
                break
        with open('data(PD19).txt', 'r+', encoding = 'utf-8') as file:
            for i in search_list:
                if len(i) == 0:
                    continue
                file.write(f'{i}\n')
            return (file.read())


def del_data (info: str) -> str:
    '''Удаляет информацию в справочнике.'''
    with open('data(PD19).txt', 'r+', encoding = 'utf-8') as file:
        search_list = file.read().split('\n')
        for i in search_list:
            if info in i:
                search_list.remove(i)
                file.close()
                with open('data(PD19).txt', 'w', encoding = 'utf-8') as file:
                    file.close()
                break
        with open('data(PD19).txt', 'r+', encoding = 'utf-8') as file:
            for i in search_list:
                if len(i) == 0:
                    continue
                file.write(f'{i}\n')
            return (file.read())



while True:
    mode = input('Выбирите режим работы справочника: ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        print(new_data(str(input('Введите новые данные: '))))
    elif mode == '3':
        print(search_data (input('Что хотите найти?: ')))
    elif mode == '4':
        print(change_data (input('Что хотите изменить?: ')))
    elif mode == '5':
        print(del_data (input('Что хотите удалить?: ')))
    
    elif mode == '0':
        break
    else:
        print('No mode')




#Исаев Владислав Иванович | +81488148414
#Пупкин Василий Иванович | +456789084796
#Белов Виктор Петрович |  +3959530953
#Косов Степан Максимович |  +78357632523
#Чехов Антон Павлович | +3575923735
#Иванов Иван Иванович | +32959325235

#Костров Константин Львович | +37923486232