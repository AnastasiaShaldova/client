"""Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в
него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv()."""
import csv
import glob
import re

from chardet import detect

txt_files = glob.iglob('*.txt')

os_prod_list = []  # «Изготовитель системы»
os_name_list = []  # «Название ОС»
os_code_list = []  # «Код продукта»
os_type_list = []  # «Тип системы»



"""Перебор файлов с данными, их открытие и считывание данных"""
def get_data():

    main_data = []  # главный список
    column_name = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    for file in txt_files:
        open_file = open(file, 'rb').read()
        encoding_file = detect(open_file)['encoding']
        opened_file = open_file.decode(encoding_file).encode(encoding='utf8').decode(encoding='utf8')

        os_prod = re.findall(f'{column_name[0]}.*$', opened_file, re.MULTILINE)
        os_name = re.findall(f'{column_name[1]}.*$', opened_file, re.MULTILINE)
        os_code = re.findall(f'{column_name[2]}.*$', opened_file, re.MULTILINE)
        os_type = re.findall(f'{column_name[3]}.*$', opened_file, re.MULTILINE)

        os_prod_l= re.split(r':', os_prod[0])[1].strip()
        os_name_l = re.split(r':', os_name[0])[1].strip()
        os_code_l = re.split(r':', os_code[0])[1].strip()
        os_type_l = re.split(r':', os_type[0])[1].strip()

        os_prod_list.append(os_prod_l)
        os_name_list.append(os_name_l)
        os_code_list.append(os_code_l)
        os_type_list.append(os_type_l)

        file_main = [os_prod_l, os_name_l, os_code_l, os_type_l]
        main_data.append(file_main)
        main_file_name = file.split('.')[0]
        main_file = open(f'main_data_{main_file_name}.csv', 'w+', encoding='utf-8')
        for counter, header in enumerate(column_name):
            main_file.write(f'{header}: {file_main[counter]}\n')

    return column_name, main_data

def write_to_csv(csv_report):
    data_column_name, data_values_main = get_data()
    with open(csv_report, 'w') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(data_column_name)
        f_writer.writerows(data_values_main)

csv_report = open('main_data_report.csv', 'w', encoding='utf-8')
csv_report.close()

write_to_csv('main_data_report.csv')

