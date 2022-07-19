from qr_generation import create_qr_code
from connect_console import get_from_terminale

args = get_from_terminale()

type_qr = args.type_qr
color = args.color
input_file = args.input_file
mode_a4 = args.a4

if args.count == 0:
    count = [args.vertical, args.horizontal]
else:
    count = args.count

create_qr_code(type_qr, color, input_file, mode_a4, count)
# standart черный C:/Users/User/Desktop/qr_test_input.json 4 5