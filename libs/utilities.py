from PIL import Image, ImageDraw, ImageFont


PEN_W = 1
SIZE_COUNT = 4

TEXT_FONT = '../data/roboto_flex.ttf'

PEN_COLOR = (194, 194, 194)
TEXT_COLOR = (0, 0, 0)
QR_BACKGROUND = (255, 255, 255)
COLOR_BACKGROUND = (255, 255, 255)

SIZE_A4 = (2480, 3508)


def correlate_size(type_qr):
    switcher = {
        'micro': 1,
        'small': 2,
        'standard': 3,
        'wide': 4,
    }
    return switcher.get(type_qr, 3)


def correlate_color(color):
    switcher = {
        'черный': 'black',
        'красный': 'red',
        'синий': 'blue',
        'зеленый': 'green'
    }
    return switcher.get(color, 'black')


def draw_field(block_w, block_h):
    block = Image.new(mode="RGB", size=(block_w, block_h), color=COLOR_BACKGROUND)

    draw = ImageDraw.Draw(block)
    draw.line((0, 0, block_w, 0), fill=PEN_COLOR, width=PEN_W)
    draw.line((block_w - PEN_W, 0, block_w - PEN_W, block_h), fill=PEN_COLOR, width=PEN_W)
    draw.line((block_w, block_h - PEN_W, 0, block_h - PEN_W), fill=PEN_COLOR, width=PEN_W)
    return block


def get_width_in_pixel(size, box_size):
    return (17 + size * 4) * box_size


def size_selection(count, mode_a4, block_w, block_h):
    if type(count) == int:
        quantity_column = count
        if mode_a4:
            quantity_lines = 0
            for i in range(1, quantity_column):
                if quantity_column % i == 0 and block_w * (quantity_column // i) <= SIZE_A4[0] and (block_h - PEN_W) * i <= SIZE_A4[1]:
                    quantity_lines = quantity_column // i
                    quantity_column = i
                    break
            if quantity_lines == 0:
                print('\n*Невозможно расположить заданное количество qr-кодов такого размера на листе А4!*\n')
        else:
            quantity_lines = quantity_column
            quantity_column = 1
    else:
        quantity_column = count[0]
        quantity_lines = count[1]
        if mode_a4:
            if block_w * quantity_column > SIZE_A4[0] or (block_h - PEN_W) * quantity_lines > SIZE_A4[1]:
                quantity_column *= quantity_lines
                quantity_lines = 0
                for i in range(1, quantity_column):
                    if quantity_column % i == 0 and block_w * (quantity_column // i) <= SIZE_A4[1] and (block_h - PEN_W) * i <= SIZE_A4[0]:
                        quantity_lines = quantity_column // i
                        quantity_column = i
                        break
                if quantity_lines == 0:
                    print('\n*Невозможно расположить заданное количество qr-кодов такого размера на листе А4!*\n')
                else:
                    print('\n*Количество qr-кодов выходит за рамки листа А4! Рекомендуется сгенерировать ', quantity_column, 'x', quantity_lines, ' qr-кодов текущего размера!*\n')
                    quantity_lines = 0

    return quantity_lines, quantity_column


def create_background_a4():
    return Image.new(mode="RGB", size=SIZE_A4, color=COLOR_BACKGROUND)


def create_background_by_size(block_w, block_h, n, m):
    return Image.new(mode="RGB", size=(block_w * n, (block_h - PEN_W) * m), color=COLOR_BACKGROUND)
