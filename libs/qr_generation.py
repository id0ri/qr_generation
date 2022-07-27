import qrcode
import json
import os
import sys
from block_generation import Blocks
from utilities import *


def check_size(link_file: str, library: str, type_qr: str) -> int:
    max_link_len = 0
    for i in range(len(link_file['data'])):
        if len(link_file['data'][i]['link']) > max_link_len:
            max_link_len = len(link_file['data'][i]['link'])
    if max_link_len > library[type_qr]['max_len']:
        return -1
    elif max_link_len <= library[type_qr]['normal_len']:
        return library[type_qr]['size']
    else:
        counter = 0
        while max_link_len > QR_CAPASITY[counter]:
            counter += 1
        counter += 1
        return counter


def create_qr_code(type_qr: str, color: str, input_file: str, mode_a4: bool, count: Union[int, list], output_file: str) -> None:
    try:
        with open(input_file, 'r', encoding='utf-8') as json_file:
            link_file = json.load(json_file)
    except:
        print('*Не удалось открыть данный json файл с ссылками!*')
        sys.exit()

    try:
        with open('../data/parameters.json', 'r') as library:
            library = json.load(library)
    except:
        print('*Не удалось открыть данный json файл с параметрами!*')
        sys.exit()

    size = library[type_qr]['size']
    box_size = library[type_qr]['box_size']
    block_w = library[type_qr]['block_w']
    block_h = library[type_qr]['block_h']

    qr_width = get_width_in_pixel(size, box_size)
    real_size = check_size(link_file, library, type_qr)
    if real_size < 0:
        print('*Данный тип qr-кода не может вместить ссылки такой длины!*')
        sys.exit()
    elif real_size > size:
        qr_width = get_width_in_pixel(real_size, box_size)
        if block_w < block_h:
            block_w = qr_width + 20
            block_h += (qr_width - get_width_in_pixel(size - 1, box_size))
        else:
            block_h = qr_width + 20
            block_w += (qr_width - get_width_in_pixel(size - 1, box_size))

    n, m = size_selection(count, mode_a4, block_w, block_h)

    if n == 0:
        sys.exit()

    if mode_a4:
        image_background = create_background_a4()
    else:
        image_background = create_background_by_size(block_w, block_h, n, m)

    color = correlate_color(color)
    text_size = library[type_qr]['text_size']
    dept = link_file['dept']

    block_type = Blocks(block_w, block_h, box_size, text_size)

    position_link = 0
    inserting_qr_x = 0
    inserting_qr_y = 0

    for i in range(m):
        for j in range(n):
            qr = qrcode.QRCode(
                version=real_size,
                error_correction=qrcode.constants.ERROR_CORRECT_Q,
                box_size=box_size,
                border=0,
            )
            qr.add_data(link_file['data'][position_link]['link'])
            text = link_file['data'][position_link]['text']
            position_link = position_link + 1

            image_qr = qr.make_image(fill_color=color, back_color=QR_BACKGROUND)
            block = block_type.create_block(size, dept, text, image_qr, qr_width)
            image_background.paste(block, (inserting_qr_x, inserting_qr_y))

            inserting_qr_x += block_w

        inserting_qr_x = 0
        inserting_qr_y += block_h - PEN_W

    output_file += 'results/'
    if not os.path.isdir(output_file):
        os.mkdir(output_file)
    image_background.save(output_file + 'qr_list.png')
