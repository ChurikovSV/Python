import json
from easygui import *

#загружаем файл БД
def load_contacts():
    try:
        with open("phone_book.json", "r") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []
 
#открываем файл для редактирования w   
def save_contacts(contacts):
    with open("phone_book.json", "w") as file:
        json.dump(contacts, file, indent=2)

#функция по изменению контакта
def add_contact(contacts, data):
    contacts.append({"Фамилия": data[0], "Имя": data[1], "Отчество": data[2], "Номер телефона": data[3]})
    save_contacts(contacts)

#функция по просмотру всех контактов    
def view_all_contacts(contacts):
    if not contacts:
        msgbox("Справочник пуст", 'Справочник')
        return

    msg = ""
    for contact in contacts:
        msg += f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}\n"
        msgbox(msg, 'Справочник')

#функция по редактированию контакта      
def edit_contact(contacts, index):
    contact = contacts[index]
    msg = "Измените запись"
    title = "Карточка контакта"
    field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    field_values = multenterbox(msg, title, field_names, 
                                values=[contact['Фамилия'], contact['Имя'], 
                                        contact['Отчество'], contact['Номер телефона']])

    if field_values:
        contacts[index] = {"Фамилия": field_values[0], 
                           "Имя": field_values[1], "Отчество": field_values[2], 
                           "Номер телефона": field_values[3]}
        save_contacts(contacts)
        msgbox("Контакт успешно изменен!")

#функция по поиску контакта по Фамилии        
def search_by_surname(contacts, surname):
    found_contacts = [contact for contact in contacts if contact['Фамилия'] == surname]
    return found_contacts

#функция по удалению контакта
def delete_contact(contacts, index):
    contact = contacts[index]
    confirmation = ynbox(f"Вы уверены, что хотите удалить запись?:\n{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}?", 'Удаление контакта')

    if confirmation:
        del contacts[index]
        save_contacts(contacts)
        msgbox("Контакт успешно удален!")