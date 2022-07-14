from PIL import Image, ImageDraw, ImageFont

PEN_W = 1

PEN_COLOR = (0, 0, 0)
TEXT_COLOR = (0, 0, 0)
QR_BACKGROUND = (255, 255, 255)
COLOR_BACKGROUND = (255, 255, 255)

SIZE_A4 = (1824, 1240)


def correlate_size(type_qr):
    switcher = {
        'micro': 1,
        'small': 2,
        'standard': 3
    }
    return switcher.get(type_qr, 4)


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


def create_background_a4():
    return Image.new(mode="RGB", size=SIZE_A4, color=COLOR_BACKGROUND)


def create_background_by_size(block_w, block_h, n, m):
    return Image.new(mode="RGB", size=(block_w * m, (block_h - PEN_W) * n), color=COLOR_BACKGROUND)
