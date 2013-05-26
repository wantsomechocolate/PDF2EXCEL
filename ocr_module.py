##Use this to fix seg fault
##https://code.google.com/p/python-tesseract/issues/detail?id=31

##  Some imports
## Standard Import
import os, sys

## For scaling and retreiving data about the PDF
from pyPdf import PdfFileWriter, PdfFileReader

## For converting the scaled PDF to an image
from wand.image import Image                    
import ctypes

## For converting the images to strings
import tesseract                                
import cv2.cv as cv

## For letting user select file paths
import Tkinter, tkFileDialog

## Import the extraction stuff
import extraction_module as extraction

import useful

#dest_file_extraction="test.csv"


default_directory="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\WorkRelated\Castle"


##  Takes a pdf path as an argument and returns the number of pages in that pdf
def getNumPages(inputFile):
    input1=PdfFileReader(file(inputFile,"rb"))
    num_pages=input1.getNumPages()
    return num_pages
    ## I don't why I need to do with with its own function - don't judge me
    ## Return a friggin integer

##  Takes a pdf, the page to scale and a zoom factor to scale by and
##  returns the path to a new pdf document that is scaled by the scale factor
def scalePDF(inputFile,pageNumber,zoomFactor):
    #print "entered scalepdf"
    #print "SCALING PDF TO INCREASE IMAGE QUALITY FOR TESSERACT"
    #print "---------------------------------------------------"
    #Proper indexing
    pageNumber=pageNumber-1
    
    #Generate output filename (Puts everything in its own directory)
    outputDirectory=inputFile[:inputFile.rindex('.')]#+inputFile[inputFile.rindex('/'):inputFile.rindex('.')]+inputFile[inputFile.rindex('/'):inputFile.rindex('.')]
    #print outputDirectory
    if not os.path.exists(outputDirectory): os.makedirs(outputDirectory)

    outputFile=inputFile[:inputFile.rindex('/')]+inputFile[inputFile.rindex('/'):inputFile.rindex('.')]+inputFile[inputFile.rindex('/'):inputFile.rindex('.')]+'_'+str(pageNumber+1)+'.pdf'
    #outputFile=inputFile[:inputFile.rindex('.')]+'_'+str(pageNumber+1)+'.pdf'
    output=PdfFileWriter()
    input1=PdfFileReader(file(inputFile,"rb"))
    page = input1.getPage(pageNumber)
    # I ran into some trouble with scaling a certain page, I
    # still can't figure out what it was. So I use try here.
    try:
        page.scaleBy(zoomFactor)
    except:
        print "---PAGE WAS NOT SCALED: "+str(pageNumber+1)
        #print "---------------------------------------------------"
    #Add page to output
    output.addPage(page)
    #Print just the file name
    #print "SAVING   SCALED    PDF   AS: "+outputFile[outputFile.rindex('/')+1:]
    #print "---------------------------------------------------"
    outputStream = file(outputFile, "wb")
    output.write(outputStream)
    outputStream.close()
    return outputFile
    ## This returns a filepath - not a filename - it's intermediate - should I delete when done? Probably

##  Takes a path to a (scaled) pdf and saves it as an image.
##  Then it returns the image path
def pdf2img(pdf_path,ext):
    #print "entered pdf2img"
    #print "CONVERTING SCALED PDF TO AN IMAGE"
    #print "---------------------------------------------------"
    img = Image(filename=pdf_path)
    imgname=pdf_path[:pdf_path.rindex('.')]+ext
    #print "SAVING CONVERTED IMAGE AS: "+imgname[imgname.rindex('/')+1:]
    #print "---------------------------------------------------"
    img.save(filename=imgname)
    return imgname
    #print "Is this a filename or filepath: " + imgname
    ## This returns the filename of an image - not a file path

##  Takes the image path and uses tess to return a string
def img2txt(image_path,api):
    #print "entered img2txt"
    #print "CONVERTING IMAGE TO TEXT"
    #print "---------------------------------------------------"
    image=cv.LoadImage(image_path, cv.CV_LOAD_IMAGE_GRAYSCALE)
    #print "set image"
    tesseract.SetCvImage(image,api)
    #print "did the tesseract thing"
    text=api.GetUTF8Text()
    #print "actually got the text"
    conf=api.MeanTextConf()
    ##  Remove every '\n' PUT IN BY TESS and put everything back together with a space!    
    page_text=" ".join(text.splitlines())
    #print "Text for " + image_path + " : " + text
    return page_text
    ## This is just a string (without newlines in it)


#This needs to be changed to print the filename as well as the page number
#if I want to be able to print multiple pdfs to the same file.

def printOutput(text_string,target_pdf,i): #4th arg - write priviledges?
    #print "entered printoutput1"
    outputFile=target_pdf[:target_pdf.rindex('.')]+' Text Output.txt'
    filename=useful.getFilenameFromPath(target_pdf)
    filehandle=file(outputFile,'a')
    filehandle.write("TEXT FROM "+str(filename)+" PAGE "+str(i))
    filehandle.write("\n")
    filehandle.write(text_string)
    filehandle.write('\n')
    return outputFile

##----THE ACTUAL PROGRAM----##

## Ask user for the target pdf, in the future I plan to have it
## be able to get all the pdfs in a directory! Or maybe I'll have
## the user make the PDF themselves? because this program still doesn't really
## know how to handle blank pages.

def pdf2txt(target_pdf,page_num,scale_factor,ext,num_pages,api):    

    print "---------------------------------------------------"
    print "THE TARGET PDF FILENAME IS: "+target_pdf[target_pdf.rindex('/')+1:]
    print "THE NUMBER OF PAGES IN THE PDF IS: "+str(num_pages)

    ##  Some empty lists for storing the data from multiple pages
    scaled_pdf, converted_image, word_list=[],[],[]

    for i in range(num_pages):
        #print "page" + str(i)
    #---Get data for each page---

        #First scale the PDF so that tess can read it better
        scaled_pdf_inter=scalePDF(target_pdf,i+1,scale_factor)

        ## pass the scaled PDF to wand to get turned into image
        converted_image_inter=pdf2img(scaled_pdf_inter,ext)

        ## not really a list anymore, passes the image to tess which makes it into a string
        print "EXTRACTING TEXT FROM PAGE: "+str(i+1)
        word_list_inter=img2txt(converted_image_inter,api)

        ##THIS IS THE HEART OF THE PROGRAM
        ##It's not meant to be raw anymore, it's meant to return a list of the desired information
        ## based on the libraries above. Eventually, you'll be able to make libraries on the fly.
        ## and they obviously won't be stored in the .py file

        #raw_text_list=extraction.refined_extract("raw_Castle_Lib",word_list_inter)
        #print raw_text_list

        ## When the list comes back, I want to print it to a .xlsx, possibly even
        ## a .xlsm. The printing thing has to be pretty smart and compare account numbers
        ## to print like bills with like bills.
        #extraction.csv_printer(raw_text_list,dest_file_extraction)

    #----Gather data from every page----
        scaled_pdf.append(scaled_pdf_inter)
        converted_image.append(converted_image_inter)
        word_list.append(word_list_inter)

        #print "---------------------------------------------------"
        print "WRITING EXTRACTED TEXT TO FILE"
        output_file=printOutput(word_list[i],target_pdf,i)

    return output_file


####  Initializations for Tess
##api = tesseract.TessBaseAPI()   
##api.SetOutputName("outputName");
##api.Init(".","eng",tesseract.OEM_DEFAULT)
##api.SetPageSegMode(tesseract.PSM_AUTO)
##
##target_pdfx = useful.getPath(default_directory)[0]
##page_numx = 1        #Initial Page Number
##scale_factorx = 4    #Each page of each PDF gets magnified by this
##extx='.png'          #Desired Image Extension
##num_pagesx=getNumPages(target_pdfx) ## Get num of pages in pdf


##output_file=pdf2txt(target_pdfx,page_numx,scale_factorx,extx,num_pagesx)

##-----UNUSED FUNCTIONS (ALTERNATE WAYS TO USE TESS)--------##
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
