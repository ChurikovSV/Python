from easygui import *
from function_book import *

contacts = load_contacts()   #вызываем функцию по загрузке файла БД

#циклом проходим по выбору действия
while True:
    choices = ['Добавить контакт', 
               'Просмотр всех контактов', 
               'Редактировать контакт',
               'Поиск по фамилии',
               'Удаление контакта',
               'Выход']
    choice = buttonbox("Выбор действия с записями", "Справочник", choices)

    if choice == 'Добавить контакт':
        msg = "Введите данные"
        title = "Карточка"
        field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
        field_values = multenterbox(msg, title, field_names)
        
        if field_values:
            add_contact(contacts, field_values)
            msgbox("Контакт успешно добавлен!")
    
    elif choice == 'Просмотр всех контактов':
        view_all_contacts(contacts)

    elif choice == 'Редактировать контакт':
        if not contacts:
            msgbox("Справочник пуст. Нельзя изменить запись.", 'Справочник')
        else:           
            if len(contacts) == 1:
                edit_contact(contacts, 0)
            else:
                try:
                    contact_names = [f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}" for contact in contacts]
                    choice = choicebox("Выберите контакт для изменения", "Справочник", contact_names)
                    if choice:
                        index = contact_names.index(choice)
                        edit_contact(contacts, index)
                except ValueError:
                    msgbox("Некоррекный ввод. Изменение не выполнено.", 'Справочник')
                
    elif choice == 'Удаление контакта':
        if not contacts:
            msgbox("Справочник пуст. Нельзя удалить запись.", 'Справочник')
        else:            
            if len(contacts) == 1:
                delete_contact(contacts, 0)
            else:
                try:   
                    contact_names = [f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}" for contact in contacts]
                    choice = choicebox("Выберите запись для удаления", "Справочник", contact_names)
            
                    if choice:
                        index = contact_names.index(choice)
                        delete_contact(contacts, index)
                except ValueError:
                    msgbox("Некоррекный ввод. Удаление не выполнено.", 'Справочник')
    
    elif choice == 'Поиск по фамилии':
        if not contacts:
            msgbox("Справочник пуст.", 'Справочник')
        else:    
            surname_search = enterbox("Введите фамилию", "Поиск по фамилии")
            if surname_search:
                found_contacts = search_by_surname(contacts, surname_search)
                if found_contacts:
                    msg = ""
                    for contact in found_contacts:
                        msg += f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}\n"
                    msgbox(msg, 'Результат поиска')
                else:
                    msgbox(f"Запись с фамилией '{surname_search}' не найден.", 'Результат поиска')          
              
    elif choice == 'Выход':
        msg_exit = "Вы хотите выйти из справочника?"
        title_exit = "Важно!"
        choices_exit = ("[<F1>]Да", "[<F2>]Нет")
        exit_func = ynbox(msg_exit, title_exit, choices_exit, image=None, default_choice="[<F1>]Да", cancel_choice="[<F2>]Нет")
        if exit_func == True:
            msgbox("Хорошего дня")
            break 
