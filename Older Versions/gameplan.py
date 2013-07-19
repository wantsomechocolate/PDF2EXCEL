##
##start program, lookup program data and stuff
##
##present menu
##    1.) ocr a pdf and parse text to xlsx
##    2.) ocr an image and parse text to xlsx
##    3.) ocr a pdf
##    4.) ocr an image
##    5.) parse text from .txt to an xlsx
##    6.) do some regex testing/refinement
##    7.) exit
##
##if choice 1
##
##get utility type (this determines how the pages will be ocred - not all
##                  are done straight up, some are broken into peices. 
##
##get listofpdfs
##
##for pdf in listofpdfs:
##    for page in pdf:
##        scale pdf
##        convert pdf to image
##        convert image to text
##        parse text for desired information
##        print text to file



## Things I want in the program data, the utility libraries, the most recent
## directory accessed by the user. Every single page that was ever ocred
## and the text. and then any item that didn't get a match, find the text
## that was supposed to have the match and add it, that way someone can foo
## around with the regex and try to get it to match as many as it can on the
## fly. Also store each regex guess and it's corresponding score.

## Also, make an error logger, a sign in, a gui, and millions. 
