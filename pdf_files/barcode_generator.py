import barcode
from barcode.writer import ImageWriter
from io import BytesIO

Code128 = barcode.get_barcode_class('Code128')

options = dict(
    module_width=0.4,  # Controls the width of each bar
    module_height=8.0,  # Controls the height of the barcode
    quiet_zone=1.0,    # Reduced quiet zone
    write_text=True,
    text_distance=5,
    font_path='./merchant-copy.ttf',
    font_size=15,
    background='white',
    foreground='black',
    # center_text=True,
    format='PNG'
)

mbr = Code128('nT114137DH11319M674ATDMLn', writer=ImageWriter())

fullname = mbr.save('code128_barcode', options)
print(f"Saved barcode to: {fullname}")
