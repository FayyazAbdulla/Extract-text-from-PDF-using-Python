import PyPDF2

a = PyPDF2.PdfReader('Screening_for_lung_cancer.pdf')

str = ""
for i in range(1,11):
    # str += a.getPage(i).extractText()
    str += a.read.Pages[1]


with open("text.txt ","w", encoding='utf-8') as f:
    f.write(str)