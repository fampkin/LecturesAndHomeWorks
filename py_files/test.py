import barcode
from barcode.writer import ImageWriter

# Генерируем штрих-код
ean = barcode.get("ean13", "123456789012", writer=ImageWriter())
filename = ean.save("barcode")  # сохраняем как PNG

# Вставляем штрих-код в чек
barcode_img = Image.open(filename + ".png")
image.paste(barcode_img, (50, 200))
image.save("check_with_barcode.png")