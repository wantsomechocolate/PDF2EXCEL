import tesseract
import ctypes
import os
import cv2.cv as cv

api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)

image_path="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\Resume_1_1.png"
#import tesseract 
#from tesseract import image_to_string
#from PIL import Image

image_path="C:\Users\James McGlynn\Documents\GitHub\PDF2XLS\eurotext.jpg"
#image_path="fakepath.jpg"
#imgobj=Image.open(image_path)
#print "1"
#print image_to_string(Image.open(imgobj))

#word_list=text.split()

#print word_list


## Uncomment next line to text function
def testy(image_path):

## Indent region below to test as function
    image=cv.LoadImage(image_path, cv.CV_LOAD_IMAGE_GRAYSCALE)
    tesseract.SetCvImage(image,api)
    text=api.GetUTF8Text()

    word_list=text.split()
    #print word_list

##Uncomment the below lines to test function
    print "Program gets here"
    return word_list

word_list=testy(image_path)
print "But not here"
print word_list


## --------OTHER METHODS TESS OFFERS------ ##

##api = tesseract.TessBaseAPI()
##api.SetOutputName("outputName");
##api.Init(".","eng",tesseract.OEM_DEFAULT)
##api.SetPageSegMode(tesseract.PSM_AUTO)
##mImgFile = "C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\Resume.png"

##result = tesseract.ProcessPagesWrapper(mImgFile,api)
##print "result(ProcessPagesWrapper)=",result

##result = tesseract.ProcessPagesFileStream(mImgFile,api)
##print "result(ProcessPagesFileStream)=",result

##result = tesseract.ProcessPagesRaw(mImgFile,api)
##print "result(ProcessPagesRaw)",result

##f=open(mImgFile,"rb")
##mBuffer=f.read()
##f.close()
##result = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
##mBuffer=None
##print "result(ProcessPagesBuffer)=",result
