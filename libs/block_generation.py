from utilities import *


class Blocks:
    block_w: int
    block_h: int
    block_size: int
    text_size: int

    def __init__(self, block_w=252, block_h=328, box_size=8, text_size=26) -> None:
        self.block_w = block_w
        self.block_h = block_h
        self.box_size = box_size
        self.text_size = text_size

    def create_block(self, size: int, dept: str, text: str, image_qr: Image, qr_width: int) -> Image:
        block = draw_field(self.block_w, self.block_h)

        if 4 <= size <= 6:
            border = (self.block_w - qr_width) // 2
            qr_position_y = self.block_h - qr_width - border
            title_position_x = border
            title_position_y = self.block_h - qr_width - border
        else:
            border = (self.block_h - qr_width) // 2
            qr_position_y = border
            title_position_x = qr_width + 2 * border
            title_position_y = self.block_h
        qr_position_x = border

        block.paste(image_qr, (qr_position_x, qr_position_y))

        font = ImageFont.truetype(font=TEXT_FONT, size=self.text_size)
        ImageDraw.Draw(block).text((title_position_x, title_position_y // 4), dept, font=font, fill=TEXT_COLOR, anchor='lm')
        ImageDraw.Draw(block).text((title_position_x, title_position_y * 3 // 4), text, font=font, fill=TEXT_COLOR, anchor='lm')

        return block
