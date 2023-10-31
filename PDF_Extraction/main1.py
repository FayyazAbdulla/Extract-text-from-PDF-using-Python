import PyPDF2

# Open the PDF file in binary mode
with open('Screening_for_lung_cancer.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    PdfReader = PyPDF2.PdfReader(pdf_file)

    # Access and print the metadata
    metadata = PdfReader.metadata
    if metadata:
        print(metadata)
    else:
        print("No metadata found.")

    # Access and print the XMP metadata
    xmp_metadata = PdfReader.xmp_metadata
    if xmp_metadata:
        print(xmp_metadata)
    else:
        print("No XMP metadata found.")

    # Get the number of pages
    num_pages = len(PdfReader.pages)  # Use len(PdfReader.pages)
    print(f"Number of pages: {num_pages}")

    # Access and print the content of page 2
    if num_pages >= 1:
        page = PdfReader.pages[1]  # Page numbering is 0-based
        page_text = page.extract_text()
        print("Content of page 2:")
        print(page_text)


        str = ""
        for i in range(1,21):
            with open("text_format.txt" , "w" , encoding="utf-8") as f:
                f.write(str)
    else:
        print("Page 2 does not exist.")


    

    # Close the PDF file
    pdf_file.close()
