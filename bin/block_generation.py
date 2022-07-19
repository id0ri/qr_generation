from utilities import *


class Blocks:
    def __init__(self, block_w=252, block_h=328, box_size=8, text_size=26):
        self.block_w = block_w
        self.block_h = block_h
        self.box_size = box_size
        self.text_size = text_size

    def class_selection(self, size, dept, text, image_qr):
        if size == 1:
            block = self.create_micro_block(size, dept, text, image_qr)
        elif size == 2:
            block = self.create_small_block(size, dept, text, image_qr)
        elif size == 4:
            block = self.create_wide_block(size, dept, text, image_qr)
        else:
            block = self.create_standard_block(size, dept, text, image_qr)
        return block

    def create_micro_block(self, size, dept, text, image_qr):
        block = draw_field(self.block_w, self.block_h)

        qr_width = (17 + size * 4) * self.box_size
        border = (self.block_h - qr_width) // 2

        block.paste(image_qr, (border, border))

        font = ImageFont.truetype(font=TEXT_FONT, size=self.text_size)
        ImageDraw.Draw(block).text((qr_width + 2 * border, self.block_h // 4), dept, font=font, fill=TEXT_COLOR, anchor='lm')
        ImageDraw.Draw(block).text((qr_width + 2 * border, self.block_h * 3 // 4), text, font=font, fill=TEXT_COLOR, anchor='lm')

        return block

    def create_small_block(self, size, dept, text, image_qr):
        block = draw_field(self.block_w, self.block_h)

        qr_width = (17 + size * 4) * self.box_size
        border = (self.block_h - qr_width) // 2

        block.paste(image_qr, (border, border))

        font = ImageFont.truetype(font=TEXT_FONT, size=self.text_size)
        ImageDraw.Draw(block).text((qr_width + 2 * border, self.block_h // 4), dept, font=font, fill=TEXT_COLOR, anchor='lm')
        ImageDraw.Draw(block).text((qr_width + 2 * border, self.block_h * 3 // 4), text, font=font, fill=TEXT_COLOR, anchor='lm')

        return block

    def create_standard_block(self, size, dept, text, image_qr):
        block = draw_field(self.block_w, self.block_h)

        qr_width = (17 + size * 4) * self.box_size
        border = (self.block_w - qr_width) // 2

        block.paste(image_qr, (border, self.block_h - qr_width - border))

        font = ImageFont.truetype(font=TEXT_FONT, size=self.text_size)
        ImageDraw.Draw(block).text((border, (self.block_h - qr_width - border) // 4), dept, font=font, fill=TEXT_COLOR, anchor='lm')
        ImageDraw.Draw(block).text((border, (self.block_h - qr_width - border) * 3 // 4), text, font=font, fill=TEXT_COLOR, anchor='lm')

        return block

    def create_wide_block(self, size, dept, text, image_qr):
        block = draw_field(self.block_w, self.block_h)

        qr_width = (17 + size * 4) * self.box_size
        border = (self.block_h - qr_width) // 2

        block.paste(image_qr, (border, border))

        font = ImageFont.truetype(font=TEXT_FONT, size=self.text_size, encoding='UTF-8')
        ImageDraw.Draw(block).text((qr_width + 3 * border, self.block_h // 4), dept, font=font, fill=TEXT_COLOR, anchor='lm')
        ImageDraw.Draw(block).text((qr_width + 3 * border, self.block_h * 3 // 4), text, font=font, fill=TEXT_COLOR, anchor='lm')

        return block
