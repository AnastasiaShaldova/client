# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_list = ['разработка', 'администрирование', 'protocol', 'standard']

for i in str_list:
    enc_result = str.encode(i, encoding='utf8')
    print(enc_result)

    dec_result = bytes.decode(enc_result, encoding='utf8')
    print(dec_result)
