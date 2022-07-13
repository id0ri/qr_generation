from qr_generation import create_qr_code

type_qr = input('Тип qr-кода: ')
color = input('Цвет: ')
input_file_link = input('Json файл с данными: ')
n = int(input('Количество qr-кодов по горизонтали: '))
m = int(input('Количество qr-кодов по вертикали: '))

create_qr_code(type_qr, color, input_file_link, n, m)
