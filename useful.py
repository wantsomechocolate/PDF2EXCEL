import os
import Tkinter, tkFileDialog
import re

def getPath(default_directory):
    origDir=os.getcwd()
    os.chdir(default_directory)
    root=Tkinter.Tk()                           ##  Explicitly call the root window so that you can...
    root.withdraw()                             ##  withdraw it!
    filePath=tkFileDialog.askopenfilename()     ##  imageFile will store the filename of the image you choose   
    root.destroy()                              ##  Some overkill
    os.chdir(origDir)                           ##  Change dir back for net zero change
    return filePath
    ## This returns a full path - not a filename

def getFilenameFromPath(path):

    filename=path[path.rindex('/')+1:path.rindex('.')]
    return filename

##def getPathFromFullFileName(full_filename):
##    path=full_filename

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
    
        #####Sample code to test get_index_and_match
        ####sample_text1="aaaasdfaaaasclfaaaasdfaaaasdf"
        ####sample_text2="aaasdffhjdkhkjfls"
        ####sample_regex='as[cd]l?f'
        ####flag_index=get_index_and_match(sample_text1,sample_regex,5)
        ####print flag_index


## The function below does not protect against accidentally having a repeat
## character in the character list.
def character_selection(string_to_pull_from, list_of_characters):
    new_string=""
    matched=0
    
    #print "list_of_characters"
    #print list_of_characters
    #print "string"
    #print string_to_pull_from

    string_to_pull_from=unicode(string_to_pull_from,"utf-8")

    #print "string"
    #print string_to_pull_from

    for char_in_string in string_to_pull_from:
        matched=0
        for char_in_list in list_of_characters:
            #print "char_in_list"
            #print char_in_list
            if char_in_string==char_in_list:
                matched=1
            else:
                pass
        if matched==1:
            new_string=new_string+str(char_in_string)
        else:
            pass

    return new_string            


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



    
