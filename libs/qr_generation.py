import qrcode
import json
import os
import sys
from block_generation import Blocks
from utilities import *


def check_size(link_file, library, size):
    max_len = 0
    for i in range(len(link_file['data'])):
        if len(link_file['data'][i]['link']) > max_len:
            max_len = len(link_file['data'][i]['link'])
    if max_len <= library[str(size)]['max_len']:
        return size
    else:
        real_size = 0
        for i in range(1, SIZE_COUNT):
            if max_len > library[str(i)]['max_len'] and max_len <= library[str(i + 1)]['max_len']:
                real_size = i + 1
        if real_size == 0:
            real_size = SIZE_COUNT + 1
        return real_size

def create_qr_code(type_qr, color, input_file, mode_a4, count, output_file):
    with open(input_file, 'r') as json_file:
        link_file = json.load(json_file)

    with open('../data/parameters.json', 'r') as library:
        library = json.load(library)
    size = correlate_size(type_qr)
    box_size = library[str(size)]['box_size']
    block_w = library[str(size)]['block_w']
    block_h = library[str(size)]['block_h']

    qr_width = get_width_in_pixel(size, box_size)
    real_size = check_size(link_file, library, size)
    print(real_size)
    if real_size > size:
        qr_width = get_width_in_pixel(real_size, box_size)
        if block_w < block_h:
            block_w = qr_width + 20
            block_h += (qr_width - get_width_in_pixel(size, box_size))
        else:
            block_h = qr_width + 20
            block_w += (qr_width - get_width_in_pixel(size, box_size))

    n, m = size_selection(count, mode_a4, block_w, block_h)

    if n == 0:
        sys.exit()

    if mode_a4:
        image_background = create_background_a4()
    else:
        image_background = create_background_by_size(block_w, block_h, n, m)

    color = correlate_color(color)
    text_size = library[str(size)]['text_size']
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

    if not os.path.isdir(output_file):
        os.mkdir(output_file)
    image_background.save(output_file + 'results/qr_list.png')
    image_background.show()
