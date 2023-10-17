import fitz
from pdf_extract import get_pdf_data, raw_dict
from position_data import pdf_blocks, title_block_pos, left_block_pos, right_block_pos

result = get_pdf_data()

def check_text_pos(block_pos, prev_elem_pos = 20):
    for i in block_pos:
        try:
            assert i in result
        except AssertionError:
            print(f'Key {i} not found in {result}')
        try:
            assert int(block_pos[i][1]) > prev_elem_pos
        except AssertionError:
            print(f'Previos block position {prev_elem_pos} is higher than current {block_pos[i][1]}')
        prev_elem_pos = block_pos[i][1]

def check_title_pos():
    mywords = [w for w in raw_dict if fitz.Rect(w[:4]) in fitz.Rect(pdf_blocks['title'])]
    title_text = " ".join(["".join(line[4]) for line in mywords])
    try:
        assert title_text in result['title']
    except AssertionError:
        print(f'Key {title_text} not found in {result}')
    try:
        assert int(mywords[0][1]) < result['barcodes'][0]['position'][1]
    except AssertionError:
        print(f'Title position {mywords[0][1]} is lower than PN-barcode y: {result["barcodes"][0]["position"][1]}')

def check_notes_pos():
    mywords = [w for w in raw_dict if fitz.Rect(w[:4]) in fitz.Rect(pdf_blocks['notes_block'])]
    try:
        assert mywords[0][1] > right_block_pos['NOTES'][1]
    except AssertionError:
        print(f'Notes text position {mywords[0][1]} is higher than NOTES title {right_block_pos["NOTES"][1]}')

def check_barcode_pn(result = result):
    barcodes = result["barcodes"]
    try:
        assert barcodes[0]["position"][1] < left_block_pos['PN'][1]
    except AssertionError:
        print(f'Barcode of PN data position {barcodes[0]["position"][1]} is lower than PN text {left_block_pos["PN"][1]}')
    try:
        assert barcodes[0]["barcode_text"] == result['PN']
    except AssertionError:
        print(f'Barcode of PN data {barcodes[0]["position"][1]} is not match to PN text {result["PN"]}')

def check_barcode_qty(result = result):
    barcodes = result["barcodes"]
    try:
        assert barcodes[1]["position"][1] < left_block_pos['Qty'][1]
    except AssertionError:
        print(f'Barcode of Qty data position {barcodes[1]["position"][1]} is lower than Qty text {left_block_pos["Qty"][1]}')
    try:
        assert barcodes[1]["barcode_text"] == result['Qty']
    except AssertionError:
        print(f'Barcode of PN data {barcodes[0]["position"][1]} is not match to PN text {result["Qty"]}')

def check_text():
    check_text_pos(left_block_pos)
    check_text_pos(right_block_pos)

# check_title_pos()
# check_notes_pos()
# check_barcode_pn()
# check_barcode_qty()