## Imports
import useful
import ast
import re
import os
RIGHT=1
LEFT=-1

## The functions below look useless, but I want it to be easy to flesh them out someday
## Like, I won't do anything unless it is in a function
def get_default_directory():
    default_directory="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\WorkRelated"
    return default_directory
    
def get_utility_library_directory():
    utility_library_directory="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\WorkRelated\Utility_Libraries"
    return utility_library_directory
    
def get_current_utility():
    current_utility="Consolidated Edison"
    return current_utility


## This takes a location and outputs a list with a page of text at each entry
## In the string
def get_document_list(text_file):
    #text_file=useful.getPath(document_list_location)
    with open(text_file,'r') as fh:
        lines=fh.readlines()
    document_list=[]
    for i in range(0,len(lines),2):
        document_list.append(lines[i+1].rstrip('\n'))
        page_list=[]
    return document_list

## Pulls from a file, should pull from data base
## Ouput in any case is a dictionary
## Takes a location and the desired utility
def get_utility_library(utility,utility_dictionary_location):
    fh=open(utility_dictionary_location,'r')
    
    #utility_dictionary=ast.literal_eval(fh.readlines()[0])
    #utility_library_scope_def=utility_dictionary[utility]

    lines_list=fh.readlines()
    whole_doc=''
    for line in lines_list:
        whole_doc=whole_doc+line

    ##  These lines were here because I thought that white space was causing
    ##  ast.literal_eval to fail. But it was in fact that I had variables
    ##  declared in the library that the eval didn't like - So this is
    ##  no longer required. I had fun writing it though. So leave it in. 
        
    #whole_doc_no_white=re.sub('\s+',' ',whole_doc).strip()
    #utility_dictionary=ast.literal_eval(whole_doc_no_white)

    utility_dictionary=ast.literal_eval(whole_doc)
    utility_library_scope_def=utility_dictionary[utility]
    fh.close()
    return utility_library_scope_def

## This uses get_index_and_match to find a match for a given
## Regex and then collects some characters in the vicinity.
def get_raw_chars(page_text,library_entry):
    data_flag=library_entry['data_flag']
    flag_inst=library_entry['data_flag_inst']
    direction=library_entry['direction']
    num_chars=library_entry['raw_char_collect']

    if direction==RIGHT:
        ## If going to the right find flag, and make start index right after the last char of the flag
        index_and_match=useful.get_index_and_match(page_text,data_flag,flag_inst)
        match_length=len(index_and_match['match'])

        try:
            start_index=index_and_match['index']+match_length
            end_index=start_index+num_chars
            if end_index>len(page_text):
                end_index=len(page_text)
            raw_text=page_text[start_index:end_index].strip()
        except:
            start_index=index_and_match['index']
            end_index=index_and_match['index']
            raw_text=index_and_match['index']
      
        ## Get end_index be adding 
    elif direction==LEFT:
        ## if left, just find the index of the flag
        index_and_match=useful.get_index_and_match(page_text,data_flag,flag_inst)
        match_length=len(index_and_match['match'])
        try:
        ## And subtract to get the right character range
            end_index=index_and_match['index'] - 1
            start_index=end_index-num_chars
            if start_index<0:
                start_index=0
            raw_text=page_text[start_index:end_index].strip()
        except:
            start_index=index_and_match['index']
            end_index=index_and_match['index']
            raw_text=index_and_match['index']
    return raw_text

def print_to_workbook(library,refined_results,text_file,tab_type):

    ## Openpyxl library imports
    from openpyxl import Workbook
    from openpyxl import load_workbook

    ## Get the excel filename from the name of the text file that the user navigated to
    book_name=useful.getFilenameFromPath(text_file)+'.xlsx'

    try: ## Try opening the workbook with the same name"
        wb=load_workbook(book_name)
        new_wb=-1
        ws = wb.get_active_sheet()
        
    except: ## If it doesn't exist then start a new workbook in memory
        wb = Workbook()
        ws = wb.get_active_sheet()
        new_wb=1
        i=0
        for key in library['library_info']['heading_order']:
            c=ws.cell(row=0, column=i)
            c.value=key
            i=i+1
    
    for entry in refined_results:
    
        last_occ_row=ws.rows[-1][0].row

        i=0
        for key in library['library_info']['heading_order']:
            c=ws.cell(row=last_occ_row, column=i)
            c.value=entry[key]
            i=i+1
            
    wb.save(book_name)
    return book_name

## Ouputs a list of strings - each entry is a page's worth of text.
ocr_text_path=useful.getPath(get_default_directory())
document_list=get_document_list(ocr_text_path)

## Retrieves the utility library from the utility dictionary for the specified utility
## which is currently determined with a function (That just returns "Consolidated Edison"
utility_library=get_utility_library(get_current_utility(),get_utility_library_directory())

## Sample of using def get raw chars
#library_entry_sample=utility_library['extraction_parameters']['G&T Demand1']
#raw_chars=get_raw_chars(document_list[0],library_entry_sample)


raw_text_list=[]
for i in range(len(document_list)):
    print "-----------------------------------------------------------"
    print "RAW TEXT FOR PAGE: "+str(i+1)
    print "-----------------------------------------------------------"
    for key in utility_library['library_info']['collection_order']:
        #print utility_library['extraction_parameters'][key]
        raw_chars=get_raw_chars(document_list[i],utility_library['extraction_parameters'][key])
        print str(key)+": "+str(raw_chars)
        raw_text_list.append(raw_chars)

book_name=print_to_workbook(utility_library,raw_text_list,"condedtest.txt","raw")


##Printing is next on the agenda
## It is not working right now. 










