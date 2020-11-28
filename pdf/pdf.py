import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

output = PdfFileWriter()

ipdf = PdfFileReader(open('super.pdf', 'rb'))
wpdf = PdfFileReader(open('wtr.pdf', 'rb'))
watermark = wpdf.getPage(0)
for i in range(ipdf.getNumPages()):
    page = ipdf.getPage(i)
    page.mergePage(watermark)
    output.addPage(page)

with open('super-wtr.pdf', 'wb') as f:
    output.write(f)
