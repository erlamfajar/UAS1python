#pip install PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader
def secure_pdf(file, password) :
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range (pdf.numPages) :
        parser.addPage (pdf.getPage (page))
    parser.encrypt(password)
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} created..")
if __name__ == "__main__" :
    file ="asd.pdf"
    #nama file pdf yang anda ingin enkripsi
    password = "123"
    #password yang anda inginkan untuk file pdf anda
    secure_pdf(file, password)