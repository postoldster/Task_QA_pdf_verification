import src.pdf_verify as pv



def test_verify_text_positions():
    pv.check_title_pos()
    pv.check_text()
    pv.check_notes_pos()

def test_verify_barcodes():
    pv.check_barcode_pn()
    pv.check_barcode_qty()