PDF2XLS
=======
Welcome to the README for PDF2XLS. The decision to embark on the journey to make this program was fueled by the hatred of performing a repetative action, which is probably the case for a lot of programs. 

The input to the program at this point is meant to be Consolidated Edison Utility Bills. Of course there are ESCO bills, oil bills and perhaps others, but Con Ed is the majority and thus the focus of this project. The program (supposedly) works in the following way:

<dl>
<dt>USER selects several files (pdfs and images)</dt>
<dd>This is achieved through the tk askopenfile dialouge</dd>
<dt>CONVERT each page of every PDF to images</dt>
<dd>PDF Manipulation is done primarily with pyPDF - The PDFs are scaled prior to conversion to image (necessary?)</dd>
<dt>CROP and STRAIGHTEN all the converted images and any others.</dt>
<dd>The rotation of the images is accomplished using opencv's probabilistic Hough line algorithm. It returns the coordinates of the lines it found and the angle of rotation is found by averaging the slopes and taking the arctan (don't forget to convert from radians to degrees) The cropping was a bit harder because the bounding box method typical of pretty much all image manipulation packages doesn't suit my needs because it won't ignore noise common at the edges of scanned documents. I wrote a function that checks the percent data in each row and column near the edges of the image and how long data persists into the image and get a "bounding box" based on that.</dd>
<dt>COMPARE all of the rotated and cropped images and group them into similar buckets</dt>
<dd>For example, if there are 24 bills of the same style and 4 pages in each bill. The analysis should result in 4 groups, each with 24 pages in it. This is the stage I am currently at.</dd>
<dt>USER highlights the areas in each group where the desired data resides</dt>
<dd>The idea is that data should be in the same spot on each image in the same group.</dd>
<dt>OCR each of the highlighted areas for every image in each group</dt>
<dd>If there are 4 groups and the user only needs data from one group, and they need 5 pieces of data, then there will be one group with 5 boxes, 3 groups with no boxes and every page in the one group will get OCR'ed in 5 different spots. Also, the peices may need to be magnified before going to OCR</dd>
<dt>REFINE and analyze the OCR'ed data</dt>
<dd>Each highlighted box will have a type of data it is trying to collect associated with it: ($)(#)(A). And the types of data will have allowable characters and common confusions associated with it, so that the final output has a greater chance of being correct. </dd>
<dt>WRITE the output to a spreadsheet (.xlsx)</dt>
<dd>Keeping track of everything so that it is in the same order as in the documents chosen, for easy comparison. In fact, each PDF document should get its own table (same tab). Images should all go in the same table, but each row of data will be denoted with the image filename. (This is ok to do because there are usually much less images then PDFs for any project.</dd>


**Future Considerations:**
--------------------------
**Current Considerations**

* I should consider not converting the image to black and white before applying the hough line algorithm because making an image black and white is introducing a loss of information and some of the images (one so far) doesn't rotate properly. But when I use the hough line algorithm on the original image is skews perfectly.
* Perhaps I should reevaluate using black and white images to begin with? Grayscale is probably better. I should convert everything to use grayscale.
* I also need a better logging, tracking system that stores everything and the variables used to get there and the time and all that great stuff. Because this project is getting too big for me to remember and keep track of everything. 
* I need to compare the dimensions of the images before comparing them. It is a waste of time to compare two images that were cropped and turned out to be markedly different sizes.
* Also, I need to figure out which images were roughly the same size and then crop them by shaving off the right and bottom edges to match the smallest image in the group? and then resizing the identically sized images (then I could try resizing to a rectangle based on original dimensions instead of a predetermined sized square.
* Look into how to compare images for structural similarities (being worked on above)
* Decide on platform for GUI. Web based? Desktop based?
* Consider making templates for common utilities so users don't have to draw a bunch of little boxes every time.
* Decide on the best way to present the data after it has been recovered from the documents.
* A timer to show the user how much time they are spending on data entry. 

**Slightly Outdated Considerations**

* Look into printing through cute PDF programatically 

System Requirements
-------------------
These are for Windows - I don't know how/if this would work on another platform)

**pyPdf** - "pip install pyPdf" worked on my machine

**ImageMagick** - http://www.imagemagick.org/script/binary-releases.php#windows

* Note: You must manually create a new system variable called MAGICK_HOME which is set to the top level directory of the ImageMagick Installation

**Wand** - "pip install wand" worked for me after ImageMagick was properly installed (Reboot may be required)

**PyTesser** - https://code.google.com/p/pytesser/

* Download the zip file and you can either put all the files in with the project directory (messy) 
* or you can just create a __init__.py file and put it in with all the files inside a folder called pytesser and throw that whole thing into the site packages directory. 
* Or go the super legit route and make an actuall package with the pytesser stuff, but I don't know how to do that. 

**cv2** - opencv python binding

* Apparently this involves downloading numpy first...
* pip install numpy failed for me with "unable to find vcvarsall.bat"
* I used "http://www.softpedia.com/get/Programming/Other-Programming-Files/Numpy.shtml" - it's the one where the alt text comes up saying this is the one to click
* I used this guys site to download opencv "http://opencvpython.blogspot.com/2012/05/install-opencv-in-windows-for-python.html"
  
**ghostscript** - http://www.ghostscript.com/download/gsdnld.html

Once all that is done it runs and imports everything successfully - I think. Let me know if I missed anything
