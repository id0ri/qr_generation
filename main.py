from qr_generation import create_qr_code

n = int(input('Количество qr-кодов по вертикали: '))
m = int(input('Количество qr-кодов по горизонтали: '))
background_mode = input('Введите формат фона(a4/standard): ')
input_file_link = input('Путь к файлу с ссылками: ')

create_qr_code(n, m, background_mode, input_file_link)