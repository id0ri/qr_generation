import argparse


def get_from_terminale():
    parser = argparse.ArgumentParser(description='Генерация заданного числа qr-кодов')

    parser.add_argument('input_file', type=str, help='Путь к json файлу с ссылками')

    parser.add_argument('-cl', '--color', type=str, default='черный', choices=['черный', 'красный', 'зеленый', 'синий'], help='Цвет qr-кода(черный/красный/зеленый/синий)')
    parser.add_argument('-t', '--type_qr', type=str, default='standard', choices=['micro', 'small', 'standard', 'wide'], help='Тип qr-кода(micro/small/standard/wide)')
    parser.add_argument('-n', '--horizontal', type=int, default=1, help='Количество qr-кодов по горизонтали')
    parser.add_argument('-m', '--vertical', type=int, default=1, help='Количество qr-кодов по вертикали')
    parser.add_argument('-ct', '--count', type=int, default=0, help='Общее количество qr-кодов')

    parser.add_argument('-a4', action='store_true', help='Фон а4(True/False)')

    return parser.parse_args()
