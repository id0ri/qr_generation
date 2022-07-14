from utilities import *


class Blocks:
    def __init__(self, block_w=252, block_h=328, box_size=8, text_size=26):
        self.block_w = block_w
        self.block_h = block_h
        self.box_size = box_size
        self.text_size = text_size

    def class_selection(self, size, dept, text, image_qr):
        if size == 2:
            block = self.create_small_block(size, dept, text, image_qr)
        else:
            block = self.create_standard_block(size, dept, text, image_qr)
        return block

    def create_small_block(self, size, dept, text, image_qr):
        block = draw_field(self.block_w, self.block_h)

        qr_width = (17 + size * 4) * self.box_size
        border = (self.block_h - qr_width) // 2

        block.paste(image_qr, (border, border))

        font = ImageFont.truetype(font='Roboto.ttf', size=self.text_size)
        ImageDraw.Draw(block).text((qr_width + 2 * border, 2 * border), dept, font=font, fill=TEXT_COLOR)
        ImageDraw.Draw(block).text((qr_width + 2 * border, self.block_h // 2 + border), text, font=font, fill=TEXT_COLOR)

        return block

    def create_standard_block(self, size, dept, text, image_qr):
        block = draw_field(self.block_w, self.block_h)

        qr_width = (17 + size * 4) * self.box_size
        border = (self.block_w - qr_width) // 2

        block.paste(image_qr, (border, self.block_h - qr_width - border))

        font = ImageFont.truetype(font='Roboto.ttf', size=self.text_size)
        ImageDraw.Draw(block).text((border, border), dept, font=font, fill=TEXT_COLOR)
        ImageDraw.Draw(block).text((border, 2 * border + self.text_size), text, font=font, fill=TEXT_COLOR)

        return block

