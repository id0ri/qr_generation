import qrcode
from PIL import Image

BOX_SIZE = 1
BORDER = 1
COLOR_BACKGROUND = (255, 255, 255)
QR_BACKGROUND = (255, 255, 255)


def correlate_size(str_size):
    switcher = {
        'micro': 1,
        'small': 2,
        'standard': 4
    }
    return switcher.get(str_size, 4)


def create_background_a4():
    return Image.new(mode="RGB", size=(210, 297), color=(255, 255, 255))


def create_background_by_size(qr_width, n, m):
    return Image.new(mode="RGB", size=(qr_width * m, qr_width * n), color=COLOR_BACKGROUND)


def create_qr_code(n, m, background_mode, input_file_link):
    link_file = open(input_file_link, 'r')
    link_storage = link_file.readlines()
    link_storage = [line.rstrip() for line in link_storage]

    size_initial = link_storage[0]
    size = correlate_size(size_initial)

    color = link_storage[1]

    qr_size_in_pixel = 17 + size * 4
    qr_width = (qr_size_in_pixel + 2 * BORDER) * BOX_SIZE

    if background_mode == 'a4':
        image_background = create_background_a4()
    else:
        image_background = create_background_by_size(qr_width, n, m)

    position_link = 2
    inserting_qr_x = 0
    inserting_qr_y = 0

    for i in range(n):
        for j in range(m):
            qr = qrcode.QRCode(
                version=size,
                error_correction=qrcode.constants.ERROR_CORRECT_Q,
                box_size=BOX_SIZE,
                border=BORDER,
            )
            qr.add_data(link_storage[position_link])

            position_link = position_link + 1

            image_qr = qr.make_image(fill_color=color, back_color=QR_BACKGROUND)
            image_background.paste(image_qr, (inserting_qr_x, inserting_qr_y))

            inserting_qr_x = inserting_qr_x + qr_width

        inserting_qr_x = 0
        inserting_qr_y = inserting_qr_y + qr_width

    image_background.save('qr_list.png')
    image_background.show()