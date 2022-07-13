import qrcode
from utilities import *


BOX_SIZE = 8
BORDER = 0
COLOR_BACKGROUND = (255, 255, 255)
QR_BACKGROUND = (255, 255, 255)
SIZE_A4 = (1824, 1240)


def create_qr_code(type_qr, color, input_file_link, n, m):
    with open(input_file_link, 'r') as json_file:
        link_file = json.load(json_file)

    size = correlate_size(type_qr)
    color = correlate_color(color)
    step_x = LIBRARY[str(size)]['block_w']
    step_y = LIBRARY[str(size)]['block_h']

    dept = link_file['dept']

    image_background = create_background_by_size(size, n, m)

    position_link = 0
    inserting_qr_x = 0
    inserting_qr_y = 0

    for i in range(n):
        for j in range(m):
            qr = qrcode.QRCode(
                version=size,
                error_correction=qrcode.constants.ERROR_CORRECT_Q,
                box_size=BOX_SIZE,
                border=0,
            )
            qr.add_data(link_file['data'][position_link]['link'])
            text = link_file['data'][position_link]['text']
            position_link = position_link + 1

            image_qr = qr.make_image(fill_color=color, back_color=QR_BACKGROUND)
            block = create_standart_block(size, dept, text, image_qr)
            image_background.paste(block, (inserting_qr_x, inserting_qr_y))

            inserting_qr_x += step_x

        inserting_qr_x = 0
        inserting_qr_y += step_y - PEN_W

    image_background.save('qr_list.png')
    image_background.show()