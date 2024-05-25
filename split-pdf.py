import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf_by_range(input_pdf_path, output_folder, start_page, end_page):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PdfFileReader(input_file)
        num_pages = pdf_reader.getNumPages()

        if start_page < 1 or start_page > num_pages or end_page < start_page or end_page > num_pages:
            print("Invalid page range.")
            return

        for page_num in range(start_page - 1, end_page):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page_num))

            output_file_path = os.path.join(output_folder, f'page_{page_num + 1}.pdf')

            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f'Page {page_num + 1} saved as {output_file_path}')

input_pdf_path = 'input_path'  
output_folder = 'output_path'
start_page = 2
end_page = 2
split_pdf_by_range(input_pdf_path, output_folder, start_page, end_page)
