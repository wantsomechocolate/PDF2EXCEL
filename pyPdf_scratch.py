from pyPdf import PdfFileWriter, PdfFileReader
import os, sys

def cropNzoom(inputFile,pageNumber,zoomFactor):

    print "Cropping and scaling pdf"
    
    pageNumber=pageNumber-1
    outputFile=inputFile[:inputFile.rindex('.')]+'_'+str(pageNumber+1)+'test.pdf'

    output=PdfFileWriter()
    input1=PdfFileReader(file(inputFile,"rb"))
    
    page = input1.getPage(pageNumber)
        
    page.scaleBy(zoomFactor)
    output.addPage(page)

    print "Saving cropped pdf as: "+outputFile[outputFile.rindex('\\')+1:]
    
    outputStream = file(outputFile, "wb")
    output.write(outputStream)
    outputStream.close()

    return outputFile

testingDir="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\WorkRelated\scaleTesting"+'\\'
samplePDF="Electric_Cute.pdf"
samplePdfPath=testingDir+samplePDF
pageNumber=1
zoomFactor=2
output=cropNzoom(samplePdfPath,pageNumber,zoomFactor)
print output

