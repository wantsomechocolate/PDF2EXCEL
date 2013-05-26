# -*- coding: utf-8 -*-
import os
import Tkinter, tkFileDialog
import re

#------------------------------------------------------
## Path Manipulations
#------------------------------------------------------

## Asks user to select a file and returns the path
## This is eventually going to let the user select a Path OR Directory
## and return a list from 1-n entries. 
def getPath(default_directory):
    path_list=[]
    origDir=os.getcwd()
    os.chdir(default_directory)
    root=Tkinter.Tk()                           ##  Explicitly call the root window so that you can...
    root.withdraw()                             ##  withdraw it!
    filePath=tkFileDialog.askopenfilename()     ##  imageFile will store the filename of the image you choose
    path_list.append(filePath)
    root.destroy()                              ##  Some overkill
    os.chdir(origDir)                           ##  Change dir back for net zero change
    return path_list
    ## This returns a full path - not a filename


def getPaths(default_directory):
    path_list=[]
    origDir=os.getcwd()
    os.chdir(default_directory)
    root=Tkinter.Tk()                           ##  Explicitly call the root window so that you can...
    root.withdraw()                             ##  withdraw it!
    filePaths=tkFileDialog.askopenfilenames()    ##  imageFile will store the filename of the image you choose

    matched=1
    regex="{.*?}"
    start_index=0
    while matched==1:
        filePaths=filePaths[start_index:]
        try:
            match=re.search(regex,filePaths).group()
            start_index=start_index+len(match)
            path_list.append(match[1:-1])
        except:
            #print "GetPaths was excepted"
            matched=0    
    
    #path_list.append(filePath)
    root.destroy()                              ##  Some overkill
    os.chdir(origDir)                           ##  Change dir back for net zero change
    return path_list

## Self explanatory. Returns just the file name
## It is easy to break this function, but I'll just deal with it if/when it happens
def getFilenameFromPath(path):
    filename=path[path.rindex('/')+1:path.rindex('.')]
    return filename

## This is just a place holder function for when I write a way to get
## "the last visited directory" or the last directory saved in
def get_default_directory():
    default_directory="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\WorkRelated"
    return default_directory

#------------------------------------------------------
## Facilitates Text Extraction Portion
#------------------------------------------------------

## Regex based index function that also returns the match itself
def get_index_and_match(text,regex,inst):

    ## Dictionary Keys
    dict_key_index='index'
    dict_key_match='match'
    ## Error messages
    no_match_message='NO MATCHES'
    inst_not_found_message='INSTANCE NOT FOUND'
    ## Variable Declarations
    char_index=-1
    match_list=[]
    regex_finds_match=True

    ## Keep trying to match regex until failure
    while regex_finds_match==True:
        try:
            ## If it can't find a match, or the regex is bad,
            ## the message will be NO MATCHES
            match=re.search(regex,text[(char_index+1):]).group() 
            char_index=text.index(match,char_index+1)
            match_list.append((char_index,match))
            
        except:
            ## The first time it can't find a match, exit the loop
            regex_finds_match=False

    ## If it found no matches at all, say so. 
    if len(match_list)==0:
        return {dict_key_index:no_match_message, dict_key_match:no_match_message}
    ## If it did find some
    else:
        ## Try applying the desired instance 
        try:
            ## If you can great
            char_index=match_list[inst-1][0]
            match=match_list[inst-1][1]
            return {dict_key_index:char_index, dict_key_match:match}
        except:
            ## If you can, say that it found at least one match, but the instance
            ## You wanted wasn't found
            return {dict_key_index:inst_not_found_message, dict_key_match:inst_not_found_message}


## Takes a string and list and basically removes all characters from the string
## That are not in the list.
        
def character_selection(string_to_pull_from, list_of_characters):
    new_string=""
    matched=0
    for char_in_string in string_to_pull_from:
        matched=0
        for char_in_list in list_of_characters:
            boolean=(char_in_list==char_in_string)

            if char_in_string==char_in_list:
                matched=1
            else:
                pass
        if matched==1:
            new_string=new_string+str(char_in_string)
        else:
            pass
    return new_string            

## Takes a string and a dictionary and replaces every character in the string
## that matches a dictionary key, to the corresponding dictionary value. 
def character_transform(string,dictionary):
    new_string=""
    matched=0
    for char in string:
        matched=0
        for key in dictionary.iterkeys():
            if char==key:
                matched=1
                new_string=new_string+str(dictionary[key])
            else:
                pass
        if matched==0:
            new_string=new_string+char
        else:
            pass       
    return new_string

#------------------------------------------------------
## Facilitates the PDF OCR Portion
#------------------------------------------------------

## Takes a string and prints 2 lines to a file, the first is the PDF source
## of the text, the next is the text. 
def printOutput(text_string,target_pdf,i): #4th arg - write priviledges?
    outputFile=target_pdf[:target_pdf.rindex('.')]+' Text Output.txt'
    filename=useful.getFilenameFromPath(target_pdf)
    filehandle=file(outputFile,'a')
    filehandle.write("TEXT FROM "+str(filename)+" PAGE "+str(i))
    filehandle.write("\n")
    filehandle.write(text_string)
    filehandle.write('\n')
    return outputFile










def getIntegerInput(start, end, promptString, default, list_of_utils):

    flag="BAD"
    while flag=="BAD":

        for i in range(len(list_of_utils)):
            print i+1,
            print " : "+list_of_utils[i]

        userSelection=raw_input(promptString)

        if userSelection=="":
            userSelection=default

        try:
            userSelection=int(userSelection)
            if userSelection<start:
                print "Option Doesn't Exist."
            elif userSelection>end:
                print "Option Doesn't Exist."
            else:
                flag="GOOD"
            
        except:
            print "Please enter an integer."

    return userSelection
