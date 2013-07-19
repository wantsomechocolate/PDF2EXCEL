PDF2XLS
=======

NOTE: If the program is only looking at a small peice of each page of your pdf, I know it sounds dumb, but print your pdf.... to a pdf.., using cutePDF. I had the same problem with some of my test PDFs and spent days trying to figure out what it was, to no avail. So try the cutePDF thing out. If that doesn't work, and you don't want to mess with the source, then .... contact me? I think I know a really long annoying way around the problem that I never looked into because the cutePDF solution suited my needs. 

Welcome to the README for PDF2XLS. The decision to embark on the journey to make this program was fueled by the hatred of performing a repetative action, which is probably the case for a lot of programs. 

The input to the program at this point is meant to be Consolidated Edison Utility Bills. Of course ESCO bills will come after. Anyway the program works by taking a pdf, scaling it to 400% the original size (using pyPdf), converting the scaled version to a png image file (using ImageMagick and the Wand python binding) and then giving that image to Google's Tesseract, which returns a string. Then the string has to be parsed to look for the desired data from the original document, in this case a utility bill. 

I am currently at the string parsing stage. I'm going to first analyze the output looking only for perfect matches and call that 100% confidence. That won't give me much of the data I want, but at least I can see how well everything is working and how I want to output the data. 

Future Considerations:
Fix the raw output so that each page is in its own div so that it can be viewed locally with a browser. 
Try to code in confidence levels to the output. 
Consider taking multiple pdfs as inputs.
Look into printing through cute PDF programatically
Investigate enhancing the image a little bit prior to submitting it to the Tesseract. 
Code the open file dialog. Should just be an import from an old project. 
  (I remember SOMEONE telling me that the python tk command to retrieve a directory didn't work on a mac...)
The program has to be able to know what utility's bill it's looking at, and what page of the bill, if applicable. 
  I'm still trying to decide if this is more or less important than getting the info from a particular bill. 
Make all these considerations projects and milestones within Github. 

System Reqs

pyPdf - pip install pyPdf works

ImageMagick - http://www.imagemagick.org/script/binary-releases.php#windows (Obviously for Windows)

  Note: You must manually create a new system variable called MAGICK_HOME which is set to the top dir of the ImageMagick Installation

Wand - pip install wand works after ImageMagick is properly installed (Reboot probably required)

python-tesseract - http://code.google.com/p/python-tesseract/

cv2
  Apparently this involves downloading numpy first...
  pip install numpy failed for me with "unable to find vcvarsall.bat"
  I used "http://www.softpedia.com/get/Programming/Other-Programming-Files/Numpy.shtml" - it's the one where the alt    text comes up saying this is the one to click
  I used this guys site to download opencv "http://opencvpython.blogspot.com/2012/05/install-opencv-in-windows-for-python.html"
  
ghostscript - http://www.ghostscript.com/download/gsdnld.html

Once all that is done it runs and imports everything successfully

I really need to work on extracting the actual data soon...............
