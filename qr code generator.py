import qrcode

data = 'yeyeye coode!'  # this is what we are going to encode

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/Utilizator/Desktop/python projects/the rest/qr code/myqrcode.png')

#now the image was encoded and saved 

"""
#the following will decode the qrcode image

from pyzbar.pyzbar import decode
from PIL import Image #pillow library

img = Image.open('C:/Users/Utilizator/Desktop/python projects/the rest/qr code/myqrcode.png')

result = decode(img)

print(result)
"""

"""
img = qrcode.make(data)

img.save('C:/Users/Utilizator/Desktop/python projects/the rest/qr code/myqrcode.png')
"""

