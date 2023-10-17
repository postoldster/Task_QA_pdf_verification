import fitz, re
import barcode
from position_data import pdf_blocks


pdf = fitz.open("pdf/test_task.pdf")
page = pdf[0]
raw_dict = page.get_text('words')

result = {}

def get_metadata(pdf = pdf):
    result['metadata'] = pdf.metadata
    return result


def get_text_info(pdf = pdf, pdf_blocks = pdf_blocks):
    for block in pdf_blocks.keys():
        page = pdf[0]
        words = page.get_text('text', fitz.Rect(pdf_blocks[block]),  sort=True)
        text_list = words.split('\n')

        add_text_info(text_list, block)
    return result


def add_text_info(text_list, block_title):
    for element in text_list:
        if block_title == 'title':
            result[block_title] = text_list[0]
            break
        if block_title == 'notes_block':
            result['NOTES'] = "".join(text_list)
            break
        if element in ('', ' '):
            continue
        temp = element.split(':')
        if len(temp) < 2 or temp[1] in ('', " "):
            result[re.sub("[#]","",temp[0].strip())] = None
        else:
            result[re.sub("[#]","",temp[0].strip())] = temp[1].strip()

def add_barcode_info(page = page):
    result['barcodes'] = barcode.get_barcode_info(page)

def get_pdf_data():
    get_text_info()
    get_metadata()
    add_barcode_info()
    return result

get_pdf_data()



