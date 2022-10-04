"""Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""
import json
import os

file_name = 'orders.json'

def write_order_to_json(item, quantity, price, buyer, date):
    if os.path.exists(file_name):
        with open(file_name, encoding="utf-8") as fl:
            data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(file_name, "w", encoding="utf-8") as fl:
            json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)

        print('Данные добавлены')

    else:
        print(f'{file_name} не найден')

write_order_to_json('Кружка', 2, 12.05, 1, '12-05-2022')
