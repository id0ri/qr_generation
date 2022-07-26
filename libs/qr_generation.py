import qrcode
import json
import os
from block_generation import Blocks
from utilities import *


def create_qr_code(type_qr, color, input_file, mode_a4, count, output_file):
    with open(input_file, 'r') as json_file:
        link_file = json.load(json_file)

    with open('../data/parameters.json', 'r') as library:
        library = json.load(library)

    size = correlate_size(type_qr)
    block_w = library[str(size)]['block_w']
    block_h = library[str(size)]['block_h']

    n, m = size_selection(count, mode_a4, block_w, block_h)

    if m != 0:
        if mode_a4:
            image_background = create_background_a4()
        else:
            image_background = create_background_by_size(block_w, block_h, n, m)

        color = correlate_color(color)
        box_size = library[str(size)]['box_size']
        text_size = library[str(size)]['text_size']
        dept = link_file['dept']

        block_type = Blocks(block_w, block_h, box_size, text_size)

        position_link = 0
        inserting_qr_x = 0
        inserting_qr_y = 0

        for i in range(m):
            for j in range(n):
                qr = qrcode.QRCode(
                    version=size,
                    error_correction=qrcode.constants.ERROR_CORRECT_Q,
                    box_size=box_size,
                    border=0,
                )

                qr.add_data(link_file['data'][position_link]['link'])
                text = link_file['data'][position_link]['text']
                position_link = position_link + 1

                image_qr = qr.make_image(fill_color=color, back_color=QR_BACKGROUND)
                if i == 0 and j == 0:
                    print(image_qr.size)
                block = block_type.create_block(size, dept, text, image_qr)
                image_background.paste(block, (inserting_qr_x, inserting_qr_y))

                inserting_qr_x += block_w

            inserting_qr_x = 0
            inserting_qr_y += block_h - PEN_W

        if not os.path.isdir(output_file):
            os.mkdir(output_file)
        image_background.save(output_file + '/qr_list.png')
        image_background.show()
