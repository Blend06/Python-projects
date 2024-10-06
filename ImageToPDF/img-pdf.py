imagelist = ["C:/Users/Plus Computers/Desktop/python/ImageToPDF/download1.jpg", 
             "C:/Users/Plus Computers/Desktop/python/ImageToPDF/download2.jpg", 
             "C:/Users/Plus Computers/Desktop/python/ImageToPDF/download3.jpg"]

from fpdf import FPDF

pdf = FPDF()

for image in imagelist:
    pdf.add_page()
    pdf.image(image, 20, 20, 30)
   
pdf.output("yourfile.pdf", "F")