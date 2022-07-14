import qrcode
import json
from block_generation import Blocks
from utilities import *


def create_qr_code(type_qr, color, input_file_link, n, m):
    with open(input_file_link, 'r') as json_file:
        link_file = json.load(json_file)

    with open('library.json', 'r') as library:
        library = json.load(library)

    size = correlate_size(type_qr)
    color = correlate_color(color)

    step_x = library[str(size)]['block_w']
    step_y = library[str(size)]['block_h']
    box_size = library[str(size)]['box_size']
    text_size = library[str(size)]['text_size']
    dept = link_file['dept']

    block_type = Blocks(step_x, step_y, box_size, text_size)

    image_background = create_background_by_size(step_x, step_y, n, m)

    position_link = 0
    inserting_qr_x = 0
    inserting_qr_y = 0

    for i in range(n):
        for j in range(m):
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
            block = block_type.class_selection(size, dept, text, image_qr)
            image_background.paste(block, (inserting_qr_x, inserting_qr_y))

            inserting_qr_x += step_x

        inserting_qr_x = 0
        inserting_qr_y += step_y - PEN_W

    image_background.save('qr_list.png')
    image_background.show()