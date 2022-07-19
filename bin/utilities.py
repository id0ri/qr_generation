from PIL import Image, ImageDraw, ImageFont

PEN_W = 1

TEXT_FONT = '../fonts/roboto_flex.ttf'

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


def size_selection(count, mode_a4, block_w, block_h):
    if type(count) == int:
        n = count
        if mode_a4:
            m = 0
            for i in range(1, n):
                if n % i == 0 and block_w * (n // i) <= SIZE_A4[0] and (block_h - PEN_W) * i <= SIZE_A4[1]:
                    m = n // i
                    n = i
                    break
            if m == 0:
                print('\n*Невозможно расположить заданное количество qr-кодов такого размера на листе А4!*\n')
        else:
            m = n
            n = 1
    else:
        n = count[0]
        m = count[1]
        if mode_a4:
            if block_w * n > SIZE_A4[0] or (block_h - PEN_W) * m > SIZE_A4[1]:
                n *= m
                m = 0
                for i in range(1, n):
                    if n % i == 0 and block_w * (n // i) <= SIZE_A4[1] and (block_h - PEN_W) * i <= SIZE_A4[0]:
                        m = n // i
                        n = i
                        break
                if m == 0:
                    print('\n*Невозможно расположить заданное количество qr-кодов такого размера на листе А4!*\n')
                else:
                    print('\n*Количество qr-кодов выходит за рамки листа А4! Рекомендуется сгенерировать ', n, 'x', m, ' qr-кодов текущего размера!*\n')
                    m = 0

    return m, n


def create_background_a4():
    return Image.new(mode="RGB", size=SIZE_A4, color=COLOR_BACKGROUND)


def create_background_by_size(block_w, block_h, n, m):
    return Image.new(mode="RGB", size=(block_w * n, (block_h - PEN_W) * m), color=COLOR_BACKGROUND)
