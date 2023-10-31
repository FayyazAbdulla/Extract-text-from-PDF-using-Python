import PyPDF2

# Open the PDF file in binary mode
with open('example.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader('Screening_for_lung_cancer.pdf')

    # Access and print the XMP metadata
    xmp_metadata = pdf_reader.xmp_metadata
    if xmp_metadata:
        print(xmp_metadata)
    else:
        print("No XMP metadata found.")

    # Close the PDF file
    pdf_file.close()
