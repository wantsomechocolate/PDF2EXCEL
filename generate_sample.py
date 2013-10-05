## Testing Platform
## Consider not cropping the right and bottom edges
## top and left edges are more robust because bills aren't always justified, more likely
## left justified.
## Also consider using cv2 to display all the images, along with some of the analysis,
## for example, be able to show the hough lines for all the images and the skew angle and interim images?
## Would be pretty cool and make it super easy to fine tune parameters.
## Maybe make it be able to adjust different parameters on the fly. Would be crazy awesome.
## Still have to work on compare though :(

from pyPdf import PdfFileWriter, PdfFileReader
import ocr_module as ocr
import extraction_module as exmo
from wand.image import Image as wand
from PIL import Image as pili
import os
import rotate_and_crop as rnc
from marbles import glass as useful

wdir="C:/Users/James McGlynn/My Programs/Python Programs/pdf2txt/CompareExperiment/compare/"
filename="Test_Steam.pdf"
filepath=wdir+filename

ext='.png'
zoom_factor=4
image_handle_list=[]

def pdf2imglist(pdf_path):
    ## Where should individual pages of pdf be saved
    save_dir_pdf=pdf_path[:pdf_path.rindex(".")]+'/pdf_9_13_13/'

    ## Where should individual images be saved
    save_dir_img=pdf_path[:pdf_path.rindex(".")]+'/images_9_13_13/'

    ## Make pdf directory
    if not os.path.exists(save_dir_pdf): os.makedirs(save_dir_pdf)

    ## Make image directory
    if not os.path.exists(save_dir_img): os.makedirs(save_dir_img)

    ## Open the pdf
    pdf_handle=PdfFileReader(file(pdf_path,"rb"))

    ## Get the number of pages in the pdf
    num_pages=pdf_handle.getNumPages()

    print "There are "+str(num_pages)+" pages.
    print "Progress will be shown with dots. 

    ## iterate through every page
    for i in range(num_pages):

        ## Initialize a place to put the output
        output=PdfFileWriter()

        #print 2

        ## Use getPage to assign a page to its own variable
        page=pdf_handle.getPage(i)

        #print 3

        ## Zoom the page so that when saved, it doesn't look like shit
        page.scaleBy(zoom_factor)

        #print 4

        ## Put the page into output
        output.addPage(page)

        #print 5

        ## Prepare the pdf filename
        output_file=save_dir_pdf+useful.add_to_filename(filename,"_"+str(i+1))

        #print 6

        ## Get ready to save the file
        outputStream = file(output_file, "wb")

        #print 7

        ## Save the file
        output.write(outputStream)

        #print 8

        ## Close the file
        outputStream.close()

        #print 9 - the item below takes a long time

        ## Open up the pdf as a wand image object
        im=wand(filename=output_file)

        #print 10

        ## Prepare the image filename
        image_path=save_dir_img+filename[:filename.rindex('.')]+'_'+str(i+1)+ext

        #print 11

        ## Save the image in png format to whatever the default mode is that wand chooses
        im.save(filename=image_path)

        #print 12

        ## Open the file as a python image library object
        im=pili.open(image_path)

        #print 13

        ## Convert the image from whatever mode to grayscale
        im=im.convert('L')

        ## Rotate and crop the image
        im=rnc.rotate_and_crop(im)
        
        #im=im.resize((im.size[0],im.size[1]))

        ## Save the image
        im.save(image_path)
        
        ## Append the image handle to a list of image handles so the function can return something useful
        image_handle_list.append(im)

        print ".",

    return image_handle_list

print ""

image_handle_list=pdf2imglist(filepath)

print "Finished!"

