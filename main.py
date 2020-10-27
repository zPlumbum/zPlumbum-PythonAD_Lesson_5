from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)
print('\n\n')

FIO = []
for i, item in enumerate(contacts_list):
    for j, element in enumerate(item):
        if j < 3:
            FIO.append(element)

    FIO = ', '.join(FIO)
    FIO = FIO.split(' ')

    for n, element in enumerate(FIO):
        if n < 3:
            contacts_list[i][n] = element.replace(',', '')

    FIO.clear()

contacts_list_edited = []
individual_person_list = []
duplicate_list = []
for i, person in enumerate(contacts_list):
    last_name = person[0]
    first_name = person[1]
    initials = (last_name, first_name)

    for j, individual_person in enumerate(contacts_list):
        if (individual_person[0] == last_name) and (individual_person[1] == first_name) and ((individual_person[0], individual_person[1]) not in duplicate_list):
            individual_person_list.append(individual_person)

    if len(individual_person_list) >= 1:
        person_lastname = ''
        person_firstname = ''
        person_surname = ''
        person_organization = ''
        person_position = ''
        person_phone = ''
        person_email = ''

        for person_data in individual_person_list:
            if person_data[0] != '':
                person_lastname = person_data[0]
            if person_data[1] != '':
                person_firstname = person_data[1]
            if person_data[2] != '':
                person_surname = person_data[2]
            if person_data[3] != '':
                person_organization = person_data[3]
            if person_data[4] != '':
                person_position = person_data[4]
            if person_data[5] != '':
                person_phone = person_data[5]
            if person_data[6] != '':
                person_email = person_data[6]

        contacts_list_edited.append([person_lastname, person_firstname, person_surname, person_organization, person_position, person_phone, person_email])

    individual_person_list.clear()
    duplicate_list.append(initials)

phonenubmer_filter = '(\+7|8)\s*\(*(\d+)\)*[\s-]*(\d+)[- ](\d+[- ]*\d+)*((.+)(доб\.)\s*(\d+)\)*)*'
pattern = re.compile(phonenubmer_filter)
for person in contacts_list_edited:
    phone = person[5]
    phone_edited = pattern.sub(r'+7(\2)\3-\4 \7\8', phone)
    person[5] = phone_edited.strip()

pprint(contacts_list_edited)

with open('phonebook_edited.csv', 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list_edited)
