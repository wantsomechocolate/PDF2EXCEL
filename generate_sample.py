## Testing Platform

from pyPdf import PdfFileWriter, PdfFileReader
import ocr_module as ocr
import extraction_module as exmo
from wand.image import Image as wand
from PIL import Image as pili
import os

wdir="C:/Users/James McGlynn/My Programs/Python Programs/pdf2txt/CompareExperiment/"
filename="compare.pdf"
filepath=wdir+filename
save_dir=wdir+filename[:filename.rindex(".")]+'/'
ext='.png'
zoom_factor=4

def pdf2imglist(pdf_path):
    outputDirectory=save_dir
    if not os.path.exists(outputDirectory): os.makedirs(outputDirectory)
    pdf_handle=PdfFileReader(file(pdf_path,"rb"))
    num_pages=pdf_handle.getNumPages()

    for i in range(num_pages):
        output=PdfFileWriter()
        page=pdf_handle.getPage(i)
        page.scaleBy(zoom_factor)
        output.addPage(page)
        output_file=save_dir+filename[:filename.rindex(".")]+"_"+str(i+1)+filename[filename.rindex("."):]
        outputStream = file(output_file, "wb")
        output.write(outputStream)
        outputStream.close()
        im=wand(filename=output_file)
        image_path=output_file[:output_file.rindex('.')]+ext
        im.save(filename=image_path)
        im=pili.open(image_path)
        im.resize((im.size[0]/zoom_factor,im.size[1]/zoom_factor))
        im.save(image_path)  

pdf=pdf2imglist(filepath)

