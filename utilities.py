from PIL import Image, ImageDraw, ImageFont
import json

with open('library.json', 'r') as lib:
    LIBRARY = json.load(lib)
PEN_W = 1
PEN_COLOR = (0, 0, 0)
TEXT_COLOR = (0, 0, 0)
COLOR_BACKGROUND = (255, 255, 255)
SIZE_A4 = (1824, 1240)


def correlate_size(type_qr):
    switcher = {
        'micro': 1,
        'small': 2,
        'standard': 3
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


def create_standart_block(size, dept, text, qr):
    block_w = LIBRARY[str(size)]['block_w']
    block_h = LIBRARY[str(size)]['block_h']
    block = Image.new(mode="RGB", size=(block_w, block_h), color=COLOR_BACKGROUND)

    draw = ImageDraw.Draw(block)
    draw.line((0, 0, block_w, 0), fill=PEN_COLOR, width=PEN_W)
    draw.line((block_w - PEN_W, 0, block_w - PEN_W, block_h), fill=PEN_COLOR, width=PEN_W)
    draw.line((block_w, block_h - PEN_W, 0, block_h - PEN_W), fill=PEN_COLOR, width=PEN_W)

    qr_width = (17 + size * 4) * LIBRARY[str(size)]['box_size']

    border = (block_w - qr_width) // 2
    block.paste(qr, (border, block_h - qr_width - border))

    font = ImageFont.truetype(font='Roboto.ttf', size=LIBRARY[str(size)]['text_size'], encoding='UTF-8')
    draw.text(
        (border, border),
        dept,
        font=font,
        fill=TEXT_COLOR
    )

    draw.text(
        (border, 2 * border + LIBRARY[str(size)]['text_size']),
        text,
        font=font,
        fill=TEXT_COLOR
    )
    return block


def create_background_a4():
    return Image.new(mode="RGB", size=SIZE_A4, color=COLOR_BACKGROUND)


def create_background_by_size(size, n, m):
    return Image.new(mode="RGB", size=(LIBRARY[str(size)]['block_w'] * m, (LIBRARY[str(size)]['block_h'] - PEN_W) * n), color=COLOR_BACKGROUND)
