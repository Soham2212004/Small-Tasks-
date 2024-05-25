from win32com import client as win32

def word_to_pdf(input_docx, output_pdf):
    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(input_docx)
    doc.SaveAs(output_pdf, FileFormat=17)
    doc.Close()
    word.Quit()

# Example usage
input_docx_file = 'input_path'
output_pdf_file = 'output_path'

word_to_pdf(input_docx_file, output_pdf_file)
