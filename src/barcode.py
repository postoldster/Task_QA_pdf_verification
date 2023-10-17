import os
import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

filepath = "page.png"

def convert_pdf_to_png(page, filepath = filepath):
    pix = page.get_pixmap()  # render page to an image
    pix.save(filepath)

def remove_converted_file(filepath = filepath):
    os.remove(filepath)

def get_barcode_info(page, filepath = filepath):
    
    convert_pdf_to_png(page)

    img = cv2.imread(filepath)
    decoded_list = decode(img, symbols=[ZBarSymbol.CODE128])
    decoded_list.sort(key=lambda l: l.rect.top and l.rect.left)

    barcode_info = [{"barcode_text": d.data.decode(), 
                     "barcode_type": d.type,
                     "position": (d.rect.left, d.rect.top,
                                  d.rect.width + d.rect.left, d.rect.height + d.rect.top)} 
                    for d in decoded_list]
    
    remove_converted_file(filepath)

    return barcode_info

