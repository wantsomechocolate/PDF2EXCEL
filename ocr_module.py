##  Some imports
## Standard Import
import os, sys

## For scaling and retreiving data about the PDF
from pyPdf import PdfFileWriter, PdfFileReader

## For converting the scaled PDF to an image
from wand.image import Image as IMG                    
import ctypes

#### For converting the images to strings method 1
##import tesseract                                
##import cv2.cv as cv

## For converting the image to strings method 2
import pytesser as pyocr

## For letting user select file paths
import Tkinter, tkFileDialog

## Import the extraction stuff
import extraction_module as extraction

## For working with images
from PIL import Image

## For tasks that are not really related to either
## extraction or character recognition
import useful

## Some program information - eventually this will be retrieved
## from some sort of program data file. 
#default_directory="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\WorkRelated\Castle"

##  Takes a pdf path as an argument and returns the number of pages in that pdf
def getNumPages(inputFile):
    input1=PdfFileReader(file(inputFile,"rb"))
    num_pages=input1.getNumPages()
    return num_pages
    ## This returns an integer when succesful, but I'm not sure when it fails. 

##  Takes a pdf, the page to scale and a zoom factor to scale by and
##  returns the path to a new pdf document that is scaled by the scale factor
def scalePDF(inputFile,pageNumber,zoomFactor):
    pageNumber=pageNumber-1
    #Generate output filename (Puts everything in its own directory)
    outputDirectory=inputFile[:inputFile.rindex('.')]#+inputFile[inputFile.rindex('/'):inputFile.rindex('.')]+inputFile[inputFile.rindex('/'):inputFile.rindex('.')]
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
    #Add page to output
    output.addPage(page)
    outputStream = file(outputFile, "wb")
    output.write(outputStream)
    outputStream.close()
    return outputFile
    ## This returns a filepath - not a filename - it's intermediate - should I delete when done? Probably

##  Takes a path to a (scaled) pdf and saves it as an image.
##  Then it returns the image path
def pdf2img(pdf_path,ext):
    img = IMG(filename=pdf_path)
    imgname=pdf_path[:pdf_path.rindex('.')]+ext
    img.save(filename=imgname)
    return imgname

##  Takes the image path and uses pyocr to return a string
def img2txt(image_path):
    ## Open Image
    im = Image.open(image_path)
    ## Send to OCR
    text=pyocr.image_to_string(im)
    ##  Remove every '\n' put in by the ocr and put
    ## everything back together with a space  
    page_text=" ".join(text.splitlines())
    ## Return a string.
    return page_text

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

## This takes a pdf path, a starting page number (which is always 1),
## a scale factor, extension, and the number of pages in the pdf.
def pdf2txt(target_pdf,page_num,scale_factor,ext,num_pages,util_lib):    

    print "---------------------------------------------------"
    print "THE TARGET PDF FILENAME IS: "+target_pdf[target_pdf.rindex('/')+1:]
    print "THE NUMBER OF PAGES IN THE PDF IS: "+str(num_pages)

    ##  Some empty lists for storing the data from multiple pages
    scaled_pdf, converted_image, word_list=[],[],[]

    for i in range(num_pages):
    #---Get data for each page---

        #First scale the PDF so that tess can read it better
        scaled_pdf_inter=scalePDF(target_pdf,i+1,scale_factor)

        ## pass the scaled PDF to wand to get turned into image
        converted_image_inter=pdf2img(scaled_pdf_inter,ext)




        ## not really a list anymore, passes the image to tess which makes it into a string
        print "EXTRACTING TEXT FROM PAGE: "+str(i+1)
        
        pieces=util_lib["library_info"]["piece_coordinates"]
        print pieces
        for section in pieces:
            for i in range(len(section)):
                if section[i]%2=0:
                    newcoordinate=section[i]*
                
        im = Image.open(converted_image_inter)

        word_list_inter=""
        for i in range(len(pieces)):
            
            image_section_filename='croppedImageSection'+str(i)+'.png'
            
            image_section = im.crop(pieces[i])
            image_section.save(image_section_filename)
            page_text_section=img2txt(image_section_filename)

            word_list_inter=word_list_inter+page_text
            ##
            ##im2=im.crop((0,180,im.size[0]/2,im.size[1]))
            ##im2.save('croppedImageTest2.png')
            ##page_text_2=ocr_module.img2txt('croppedImageTest2.png')
            ##
            ##im3=im.crop((im.size[0]/2,180,im.size[0],im.size[1]))
            ##im3.save('croppedImageTest3.png')
            ##page_text_3=ocr_module.img2txt('croppedImageTest3.png')
            ##
            ##page_text=page_text_1+page_text_2+page_text_3
            ##print page_text
        
        #word_list_inter=img2txt(converted_image_inter)




    #----Gather data from every page----
        scaled_pdf.append(scaled_pdf_inter)
        converted_image.append(converted_image_inter)
        word_list.append(word_list_inter)

        #print "---------------------------------------------------"
        print "WRITING EXTRACTED TEXT TO FILE"
        output_file=printOutput(word_list[i],target_pdf,i)

    return output_file

def pdf2txt1page(target_pdf,page_num,scale_factor,ext):    

    #First scale the PDF so that tess can read it better
    scaled_pdf_inter=scalePDF(target_pdf,page_num,scale_factor)

    ## pass the scaled PDF to wand to get turned into image
    converted_image_inter=pdf2img(scaled_pdf_inter,ext)

    ## not really a list anymore, passes the image to tess which makes it into a string
    print "EXTRACTING TEXT FROM PAGE: "+str(i+1)
    word_list_inter=img2txt(converted_image_inter)

#----Gather data from every page----
    scaled_pdf.append(scaled_pdf_inter)
    converted_image.append(converted_image_inter)
    word_list.append(word_list_inter)

    #print "---------------------------------------------------"
    print "WRITING EXTRACTED TEXT TO FILE"
    output_file=printOutput(word_list[i],target_pdf,i)

    return output_file

## For testing this module
##target_pdfx = useful.getPath(default_directory)[0]
##page_numx = 1        #Initial Page Number
##scale_factorx = 4    #Each page of each PDF gets magnified by this
##extx='.png'          #Desired Image Extension
##num_pagesx=getNumPages(target_pdfx) ## Get num of pages in pdf
##output_file=pdf2txt(target_pdfx,page_numx,scale_factorx,extx,num_pagesx)

