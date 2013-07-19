import cv2.cv as cv
import tesseract
import ctypes
import os
import pyPdfSample as pdfmanip
## pdf to image 
from wand.image import Image  ##THIS TOOK WAY TO FUCKING LONG TO GET WORKING
## for pdf manipulation
from pyPdf import PdfFileWriter, PdfFileReader
import os, sys

## Initializations 
sampleImage="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\Resume_1_1.png"
pdf = "C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\Resume.pdf"
ext='.png'
print "Target PDF is: "+pdf[pdf.rindex('\\')+1:]

##This function hangs, but the lines when run independantly work fine :(
def img2text_method2(image_path):
    print "Using method 2 to generate text from image..."
    
    api = tesseract.TessBaseAPI()
    api.SetOutputName("outputName");
    api.Init(".","eng",tesseract.OEM_DEFAULT)
    api.SetPageSegMode(tesseract.PSM_AUTO)

    image=cv.LoadImage(image_path, cv.CV_LOAD_IMAGE_GRAYSCALE)
    tesseract.SetCvImage(image,api)
    text=api.GetUTF8Text()
    word_list=text.split()
    print word_list
    return word_list

def img2text(image_path):
    print "Choosing img2text generation method..."
    word_list=img2text_method2(image_path)
    print "20"
    return word_list

def pdf2img(pdf_path):
    print "Converting pdf section to image..."
    img = Image(filename=pdf_path)
    imgname=pdf_path[:pdf_path.rindex('.')]+ext
    print "Saving image: "+imgname[imgname.rindex('\\')+1:]
    img.save(filename=imgname)
    return imgname


#working wrapper

page_num=1
scale_factor=2
section=1


#def pdf2xls(pdf_path):

print "1"

pdfTopHalf=pdfmanip.cropNzoom(pdf_path,page_num,scale_factor,section)

#pdfBottomHalf=pdfmanip.cropNzoom(pdf_path,page_num,scale_factor,section+1)
print "2"

imageTopHalf=pdf2img(pdfTopHalf)

#imageBottomHalf=pdf2img(pdfBottomHalf)
print "3"

#word_list_topHalf = img2text(imageTopHalf)

print "Using method 2 to generate text from image..."

image_path=imageTopHalf

api = tesseract.TessBaseAPI()
api.SetOutputName("outputName");
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)

image=cv.LoadImage(image_path, cv.CV_LOAD_IMAGE_GRAYSCALE)
tesseract.SetCvImage(image,api)
text=api.GetUTF8Text()
word_list=text.split()

#word_list_bottomHalf=img2text(imageBottomHalf)
#word_list=[]
#for item in word_list_topHalf:
#    word_list.append(item)
#for item in word_list_bottomHalf:
#    word_list.append(item)
print "4"

word_list=word_list_topHalf

print "5"
print word_list
return word_list

##pdf2xls_output=pdf2xls(pdf)
##print pdf2xls_output
##word_list=img2text(sampleImage)
##print word_list


##-----UNUSED FUNCTIONS--------##
##def img2text_method1(image):
##    api = tesseract.TessBaseAPI()
##    api.Init(".","eng",tesseract.OEM_DEFAULT)
##    api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
##    api.SetPageSegMode(tesseract.PSM_AUTO)
##    
##    mImgFile = image
##    mBuffer=open(mImgFile,"rb").read()
##    text = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
##    word_list=text.split()
##    return word_list
##
##def img2text_method3(image):
##    api = tesseract.TessBaseAPI()
##    api.SetOutputName("outputName");
##    api.Init(".","eng",tesseract.OEM_DEFAULT)
##    api.SetPageSegMode(tesseract.PSM_AUTO)
##    mImgFile = image
##
##    text = tesseract.ProcessPagesWrapper(mImgFile,api)
##    word_list=text.split()
##    return word_list
##
##def img2text_method4(image):
##    api = tesseract.TessBaseAPI()
##    api.SetOutputName("outputName");
##    api.Init(".","eng",tesseract.OEM_DEFAULT)
##    api.SetPageSegMode(tesseract.PSM_AUTO)
##    mImgFile = image
##
##    text = tesseract.ProcessPagesFileStream(mImgFile,api)
##    word_list=text.split()
##    return word_list
##
##def img2text_method5(image):
##    api = tesseract.TessBaseAPI()
##    api.SetOutputName("outputName");
##    api.Init(".","eng",tesseract.OEM_DEFAULT)
##    api.SetPageSegMode(tesseract.PSM_AUTO)
##    mImgFile = image
##
##    text = tesseract.ProcessPagesRaw(mImgFile,api)
##    word_list=text.split()
##    return word_list
##    
##def img2text_method6(image):
##    api = tesseract.TessBaseAPI()
##    api.SetOutputName("outputName");
##    api.Init(".","eng",tesseract.OEM_DEFAULT)
##    api.SetPageSegMode(tesseract.PSM_AUTO)
##    mImgFile = image
##
##    f=open(mImgFile,"rb")
##    mBuffer=f.read()
##    f.close()
##    text = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
##    mBuffer=None
##    word_list=text.split()
##    return word_list


