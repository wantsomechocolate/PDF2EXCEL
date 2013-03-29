## Use a keyed list for the library
## That way the order doesn't matter!

## Extraction Algorithms
RIGHT=1
LEFT=-1

## This is the fine extraction library - below are the names of each piece of data.

#Collection type, data name, keyword, instance, direction, raw chars to collect,
#stop_method, stop_key, stop_inst, use in final table

##refined_Castle_Lib = ([0,"Address","RE:",1,RIGHT,40,"keyword","(",1,"NO"],
##                  [0,"Account#","ACCOUNT",1,RIGHT,30,"space-delimited",1,2,"NO"],
##                  [0,"Gallons","P.B.T.",1,LEFT,30,"space-delimited",2,1,"YES"],
##                  [0,"Base Price","P.B.T.",1,LEFT,30,"space-delimited-refine-chars",1,0,"NO"],
##                  #[0,"Tax","NY SALES TAX",1,LEFT,30,"space-delimited",1,0,"NO"],
##                  #[0,"Sales Tax","NY SALES TAX",1,RIGHT,30,"space-delimited",1,2,"NO"],
##                  [0,"Discount","COUNT =",1,RIGHT,30,"numbers-with-buffer-decimal-number",3,1,"NO"],
##                  [0,"Total-Discount","PAY ONLY",1,RIGHT,30,"numbers-with-buffer-decimal-number",3,1,"NO"],
##                  [0,"Delivery Date","AMOUNT",1,RIGHT,30,"numbers-with-buffer-date",2,1,"YES"],
##                  [0,"Fuel Oil Type","FUEL OIL",1,LEFT,5,"keyword-include","#",1,"YES"])

refined_Castle_Lib ={'library_info':{

                        'utility':'Castle Oil',
                        'collection_order':('account number','address','delivery date','fuel oil type',
                                            'gallons','total-discount','discount','base price'),
                        'heading_order':('address','account number','base price','discount','total-discount',
                                         'fuel oil type','delivery date','gallons')},

		    'extraction_parameters':{

                        'address':{
                                'data_flag'                : 'RE:',
                                'data_flag_inst'           : 1,
                                'direction'                : RIGHT,
                                'raw_char_collect'         : 40,
                                'collection_method'        : 'keyword',
                                'collection_parameter_1'   : '(',
                                'collection_parameter_2'   : 1,
                                'include_in_final'         : 'NO',
                                'collection_type'          : 0},

                        'account number':{
                                'data_flag'                : 'ACCOUNT',
                                'data_flag_inst'           : 1,
                                'direction'                : RIGHT,
                                'raw_char_collect'         : 30,
                                'collection_method'        : 'space-delimited',
                                'collection_parameter_1'   : 1,
                                'collection_parameter_2'   : 2,
                                'include_in_final'         : 'NO',
                                'collection_type'          : 0},

                        'gallons':{
                                'data_flag'                : 'P.B.T.',
                                'data_flag_inst'           : 1,
                                'direction'                : LEFT,
                                'raw_char_collect'         : 30,
                                'collection_method'        : 'space-delimited',
                                'collection_parameter_1'   : 2,
                                'collection_parameter_2'   : 1,
                                'include_in_final'         : 'YES',
                                'collection_type'          : 0},

                        'discount':{
                                'data_flag'                : 'COUNT =',
                                'data_flag_inst'           : 1,
                                'direction'                : RIGHT,
                                'raw_char_collect'         : 30,
                                'collection_method'        : 'numbers-with-buffer-decimal-number',
                                'collection_parameter_1'   : 3,
                                'collection_parameter_2'   : 1,
                                'include_in_final'         : 'NO',
                                'collection_type'          : 0},

                        'total-discount':{
                                'data_flag'                : 'PAY ONLY',
                                'data_flag_inst'           : 1,
                                'direction'                : RIGHT,
                                'raw_char_collect'         : 30,
                                'collection_method'        : 'numbers-with-buffer-decimal-number',
                                'collection_parameter_1'   : 3,
                                'collection_parameter_2'   : 1,
                                'include_in_final'         : 'NO',
                                'collection_type'          : 0},

                        'delivery date':{
                                'data_flag'                : 'AMOUNT',
                                'data_flag_inst'           : 1,
                                'direction'                : RIGHT,
                                'raw_char_collect'         : 30,
                                'collection_method'        : 'numbers-with-buffer-date',
                                'collection_parameter_1'   : 2,
                                'collection_parameter_2'   : 1,
                                'include_in_final'         : 'YES',
                                'collection_type'          : 0},

                        'fuel oil type':{
                                'data_flag'                : 'FUEL OIL',
                                'data_flag_inst'           : 1,
                                'direction'                : LEFT,
                                'raw_char_collect'         : 5,
                                'collection_method'        : 'keyword-include',
                                'collection_parameter_1'   : '#',
                                'collection_parameter_2'   : 1,
                                'include_in_final'         : 'YES',
                                'collection_type'          : 0},

                        'base price':{
                                'data_flag'                : 'P.B.T.',
                                'data_flag_inst'           : 1,
                                'direction'                : LEFT,
                                'raw_char_collect'         : 30,
                                'collection_method'        : 'space-delimited-refine-chars',
                                'collection_parameter_1'   : 1,
                                'collection_parameter_2'   : 0,
                                'include_in_final'         : 'NO',
                                'collection_type'          : 0}}}
                            

##Add this in once the others are working
##,[1,"Cost","ADD","Total-Discount","Total-Discount"])

## Character Lists for Certain types of collection methods
numbers_with_buffer_decimal_number=(',','.','1','2','3','4','5','6','7','8','9','0')
numbers_with_buffer_date=('/','|','1','2','3','4','5','6','7','8','9','0')

## Takes some text and looks for the desired instance of the flag, starting in the direction you choose
## I should add an optional argument to start at a desired index.
def get_index(text,flag,inst,direc):
    if direc==RIGHT:                ## If the direction is the right
        char_index=-1               ## Then you can start at the beginning of the text
        for i in range(inst):       ## Do this once for every instance (Probably a slow way to do this)
            try:                    ## See if you can find the desired string  
                char_index=text.index(flag,char_index+1)  ## if you can, get the index
            except:   
                char_index="Instance Not Found"     ## if you can't, make char_index a string
                
        ## If you're looking for the second instance, the starting char
        ## has now been reset and you look for the string again.
        ## if at any time you don't find the string, it doesn't exit the loop (would be smart)
        ## it just keeps assigning the same string to char_index because it won't be able to
        ## use .index properly. It then returns either a string or an index
        return char_index
    
    ## If the direction is LEFT
    ## I couldn't get the starting index of rindex to work properly so it's slightly different
    else:                           ## If the direction is left. 
        char_index=len(text)        ## Set the index to the end of the string
        for i in range(inst):       ## Do this once for every instance
            try:                    ## See if you can find the string (As char-index is reset,
                                    ##    the piece of string being looked at gets smaller)
                char_index=text[:char_index].rindex(flag)
            except:                 ## If you can't make the index a string
                char_index="Instance Not Found"  ## So that all subsequent searches fail. 
        return char_index           

## This is a printer I slapped together to see if I was collecting the right stuff,
## which is good, because I totally wasn't
## eventually I will replace this with a xlsx printer (from openpyxl)
def csv_printer(data_list,file_path):
    file_handle=file(file_path,'a')
    for item in data_list:
        file_handle.write('"'),
        file_handle.write(str(item[1])),
        file_handle.write('"'),
        file_handle.write(",")
    file_handle.write("\n")
    file_handle.close()

## This collects the desired number of characters to be collected for further analysis
## That way I can search for a string and if I don't find it, it doesn't have to go through
## The entire page text and maybe find an instance I don't want or something.
    
def get_raw_chars(page_text,data_flag,flag_inst,direction,num_chars):
    try:
        if direction==RIGHT:
            start_index=get_index(page_text,data_flag,flag_inst,RIGHT)+len(data_flag)
            end_index=start_index+num_chars
            raw_text=page_text[start_index:end_index].strip()
        elif direction==LEFT:
            end_index=get_index(page_text,data_flag,flag_inst,LEFT)
            start_index=end_index-num_chars-len(data_flag)
            raw_text=page_text[start_index:end_index].strip()
    except:
        raw_text="FLAG NOT FOUND"
    return raw_text

## ----------------- extraction functions for every case--------(yeah right)

## This takes the a library entry and some text and looks for a specific string
## which it uses as a flag to stop collecting
def stop_key_string(lib_entry,raw_text):
    #direction = lib_entry[4]
    direction = lib_entry['direction']
    #stop_key = lib_entry[7]
    stop_key = lib_entry['collection_parameter_1']
    #stop_inst = lib_entry[8]
    stop_inst = lib_entry['collection_parameter_2']
    if direction==RIGHT:
        end_index=get_index(raw_text,stop_key,stop_inst,RIGHT)
        if end_index=="Instance Not Found":
            end_index=None
        refined_text=raw_text[:end_index].strip()
    else:
        start_index=get_index(raw_text,stop_key,stop_inst,LEFT)
        if start_index=="Instance Not Found":
            start_index=None
        refined_text=raw_text[start_index:].strip()
    return refined_text

## This just gets a specific number of chars, this will probably only be used if
## I can't figure out any other way to extract something and it happens to be a
## consistent length
def stop_key_number_of_chars(lib_entry,raw_text):
    #direction = lib_entry[4]
    direction = lib_entry['direction']
    #stop_key = lib_entry[7]
    stop_key = lib_entry['collection_parameter_1']
    #stop_inst = lib_entry[8]
    stop_inst = lib_entry['collection_parameter_2']
    
    if direction==RIGHT:
        end_index=stop_key
        refined_text=raw_text[:end_index].strip()
    else:
        start_index=len(raw_text)-stop_key
        refined_text=raw_text[start_index:].strip()

    return refined_text

## This collects "words". I can say I want to collect that group of
## characters seperated by spaces on both sides that is x number of
## "words" away from the beginning/end of the raw text string
def stop_key_space_delimited(lib_entry, raw_text):
    #direction = lib_entry[4]
    direction = lib_entry['direction']
    #stop_key = lib_entry[7]
    stop_key = lib_entry['collection_parameter_1']
    #stop_inst = lib_entry[8]
    stop_inst = lib_entry['collection_parameter_2']

    if direction==RIGHT:
        start_index=get_index(" "+raw_text," ",stop_key,RIGHT)
        end_index=get_index(" "+raw_text," ",stop_inst,RIGHT)
        refined_text=raw_text[start_index:end_index].strip()
    else:
        start_index=get_index(raw_text," ",stop_key,LEFT)
        end_index=get_index(raw_text," ",stop_inst,LEFT)
        refined_text=raw_text[start_index:end_index].strip()
        
    return refined_text

## This takes a string and misleadingly, will collect only the characters
## in a character list (most of the time numbers periods and commas)
## with a specified buffer. Meaning that if it fails to find a character in
## the list after x characters it will stop collecting.
def stop_key_numbers_with_buffer(lib_entry, raw_text, character_list):
    #direction = lib_entry[4]
    direction = lib_entry['direction']
    #stop_key = lib_entry[7]
    stop_key = lib_entry['collection_parameter_1']
    #stop_inst = lib_entry[8]
    stop_inst = lib_entry['collection_parameter_2']
    
    collection_string=""
    buffer_length=stop_key
    
    if direction==RIGHT:
        i=0
        while (buffer_length>0 and i<len(raw_text)):
            current_char=raw_text[i]
            acceptable=0
            for acceptable_char in character_list:
                if current_char==acceptable_char:
                    acceptable=1
                else:
                    pass
            if acceptable==1:
                collection_string=collection_string+current_char
                buffer_length=stop_key
            else:
                buffer_length=buffer_length-1
            i=i+1

        refined_text=collection_string.strip()
        
    else:
        i=len(raw_text)
        while (buffer_length>0 and i>0):
            current_char=raw_text[i-1]
            acceptable=0
            for acceptable_char in character_list:
                if current_char==acceptable_char:
                    acceptable=1
                else:
                    pass
            if acceptable==1:
                collection_string=collection_string+current_char
                buffer_length=stop_key
            else:
                buffer_length=buffer_length-1
            i=i-1

        refined_text=collection_string.strip()
    return refined_text

## Calls the keyword method, and then appends the initial flag text to it
## I wrote this one specifically to look for the words "FUEL OIL" in the
## raw text from the pdf, then find '#4' based on looking for the # sign.
## then I thought #4 was too short so I added it on to make it "#4 FUEL OIL"
## maybe it will be useful for something else one day
def stop_key_keyword_include(lib_entry, raw_text):
    refined_text=stop_key_string(lib_entry,raw_text)+" "+lib_entry['data_flag']#lib_entry[2]
    return refined_text

## This gets a groupd of chars from the space method and then refines the chars
## based on a character list using the buffer method
## I should really add the refine case as on option to the library so I can do
## it to any refined text as one last refinment step.
## But I was too lazy to do it at the time of this writing.
def stop_key_space_delimited_refine_chars(lib_entry, raw_text, character_list, buffer_length):
    refined_text_inter=stop_key_space_delimited(lib_entry, raw_text)
####    lib_entry_copy=[]
####    for item in lib_entry:
####        lib_entry_copy.append(item)
####    lib_entry_copy[7]=buffer_length
####    lib_entry_copy[8]=1
####    lib_entry_copy[4]=RIGHT
    import copy
    lib_entry_copy=copy.deepcopy(lib_entry)
    lib_entry_copy['collection_parameter_1']=buffer_length
    lib_entry_copy['collection_parameter_2']=1
    lib_entry_copy['direction']=RIGHT
    refined_text=stop_key_numbers_with_buffer(lib_entry_copy, refined_text_inter, character_list)
    return refined_text

## Default, if there is no function written for the desired case just return the raw text
## as refined text
def stop_key_default(lib_entry, raw_text):
    return raw_text
    
##------------------------End extraction function section------------------
##-------------------------------------------------------------------------

## This function uses the library and the functions above to get the desired data
## found in the vicinity of each keyword. It is a huge if else if statement
def refined_extract(refined_lib,page_text):

    #raw_text_list=[]
    raw_text_list={}

## The raw text has to be put into a dict
## And the refined text should also be put into a dict.
    
    ## go through all of the entries in refined lib because it's what you need to get
    ## to do the utility analysis
    for item in refined_lib['library_info']['collection_order']:
        entry=refined_lib['extraction_parameters'][item]
        print item
        #if collection type is 0 then: (Collection type denotes wether you need to get a new string
        # or use already collected values (like summing two values)

        ##coll_type,data_type,data_flag,flag_inst,direction,num_chars,stop_mthd,stop_key,stop_inst,fin_tab=entry[:]

        coll_type=entry['collection_method']
        #data_type=entry['']
        data_flag=entry['data_flag']
        flag_inst=entry['data_flag_inst']
        direction=entry['direction']
        num_chars=entry['raw_char_collect']
        stop_mthd=entry['collection_method']
        stop_key=entry['collection_parameter_1']
        stop_inst=entry['collection_parameter_2']
        fin_tab=entry['collection_type']
        
        #This gets a number of characters near the flag to make analysis easier
        raw_text=get_raw_chars(page_text,data_flag,flag_inst,direction,num_chars)
        ## put all the raw text into a list
        #raw_text_list.append(raw_text)
        raw_text_list[item]=raw_text
    for item in raw_text_list.itervalues(): print item

    print "----------------------------------------------------------------------"
    print "PRINTING RAW TEXT"
    print "----------------------------------------------------------------------"
    
    for key in refined_lib['library_info']['collection_order']:
        print key+": "+raw_text_list[key]
    #key, value in raw_text_list.iteritems(): print key+": "+raw_text_list[i]

    #print "LENGTH OF RAW TEXT LIST: "+str(len(raw_text_list))

    print "----------------------------------------------------------------------"
    print "GETTING REFINED DATA"
    print "----------------------------------------------------------------------"

    refined_text_list={}
    ##for i in range(len(raw_text_list)):
    for key in refined_lib['library_info']['collection_order']:#.iterkeys():
        #print i
        print key
        #print refined_lib[key]
        if refined_lib['extraction_parameters'][key]['collection_method']=="number-of-chars":
            #print "Keyword matched, using number-of-chars method to retrieve data"
            refined_text=stop_key_number_of_chars(refined_lib['extraction_parameters'][key],raw_text_list[key])
            #print refined_text
            #refined_text_list.append(refined_text)
            refined_text_list[key]=refined_text
            
        elif refined_lib['extraction_parameters'][key]['collection_method']=="keyword":
            #print "Keyword matched, using keyword method to retrieve data"
            refined_text=stop_key_string(refined_lib['extraction_parameters'][key],raw_text_list[key])
            #print refined_text
            #refined_text_list.append(refined_text)
            refined_text_list[key]=refined_text
            
        elif refined_lib['extraction_parameters'][key]['collection_method']=="space-delimited":
            #print "Keyword matched, using space-delimited method to retrieve data"
            refined_text=stop_key_space_delimited(refined_lib['extraction_parameters'][key], raw_text_list[key])
            #refined_text_list.append(refined_text)
            refined_text_list[key]=refined_text

        elif refined_lib['extraction_parameters'][key]['collection_method']=="numbers-with-buffer-decimal-number":
            #print "Keyword matched, using numbers-with-buffer-decimal-number method to retrieve data"
            refined_text=stop_key_numbers_with_buffer(refined_lib['extraction_parameters'][key], raw_text_list[key],numbers_with_buffer_decimal_number)
            #refined_text_list.append(refined_text)
            refined_text_list[key]=refined_text
            
        elif refined_lib['extraction_parameters'][key]['collection_method']=="numbers-with-buffer-date":
            #print "Keyword matched, using numbers-with-buffer-date method to retrieve data"
            refined_text=stop_key_numbers_with_buffer(refined_lib['extraction_parameters'][key], raw_text_list[key],numbers_with_buffer_date)
            #refined_text_list.append(refined_text)
            refined_text_list[key]=refined_text
            
        elif refined_lib['extraction_parameters'][key]['collection_method']=="keyword-include":
            #print "Keyword matched, using keyword-include method to retrieve data"
            refined_text=stop_key_keyword_include(refined_lib['extraction_parameters'][key], raw_text_list[key])
            #refined_text_list.append(refined_text)
            refined_text_list[key]=refined_text

        elif refined_lib['extraction_parameters'][key]['collection_method']=="space-delimited-refine-chars":
            #print "Keyword matched, using space-delimited-refine-chars method to retrieve data"
            refined_text=stop_key_space_delimited_refine_chars(refined_lib['extraction_parameters'][key], raw_text_list[key], numbers_with_buffer_decimal_number, 3)
            #refined_text_list.append(refined_text)
            refined_text_list[key]=refined_text
            
        else:
            print "Keyword did not match any function, '"+refined_lib['extraction_parameters'][key]['collection_method']+"'"
            #refined_text_list.append(raw_text_list[i])
            refined_text_list[key]=refined_text

    print "----------------------------------------------------------------------"
    print "PRINTING REFINED TEXT"
    print "----------------------------------------------------------------------"
    for key in refined_lib['library_info']['heading_order']:
        print key+": "+refined_text_list[key]

    #for i in range(len(refined_text_list)): print str(i+1)+": "+ refined_text_list[i]

    return refined_text_list


###--------------------------------------------------------------------------------------------
###--------START OF PROGRAM---------------------------------------------------------------
import os
import useful

#Prompt User for text file
default_directory="C:\Users\James McGlynn\My Programs\Python Programs\pdf2txt\WorkRelated\Castle"
text_file=useful.getPath(default_directory)

## Open the text file and put every line in a list
with open(text_file,'r') as fh:
    lines=fh.readlines()

## Because of the way the document was created, I only want every other line
page_list=[]
document_list=[]
for i in range(0,len(lines),2):
    page_list.append(lines[i].rstrip('\n'))
    page_list.append(lines[i+1].rstrip('\n'))
    document_list.append(page_list)
    page_list=[]



## The collection process
refined_results=[]
for i in range(len(document_list)):
    raw_text=document_list[i][1]
    result=refined_extract(refined_Castle_Lib, raw_text)   
    refined_results.append(result)

    print refined_results


## write refined lib to an excel file
book_name='Castle Oil.xlsx'
from openpyxl import Workbook
from openpyxl import load_workbook
try:
    wb=load_workbook(book_name)
except:
    wb = Workbook()
    #ws=wb.get_active_sheet()

match=0
for entry in refined_results:
    
    sheet_names=wb.get_sheet_names()
    #print sheet_names
    for item in sheet_names:
        #print entry[1]
        if entry['account number']==item:
            match=1
        else:
            pass
    if match==1:
        ws=wb.get_sheet_by_name(entry['account number'])
        last_occ_row=ws.rows[-1][0].row
        #row=last_occ_row
        #col=0
        i=0
        for key in refined_Castle_Lib['library_info']['heading_order']:
            c=ws.cell(row=last_occ_row, column=i)
            c.value=entry[key]
            i=i+1
    else:
        newSheet=wb.create_sheet()
        newSheet.title = str(entry['account number'])
        i=0
        for key in refined_Castle_Lib['library_info']['heading_order']:
            c=newSheet.cell(row=0, column=i)
            d=newSheet.cell(row=1, column=i)
            c.value=key
            d.value=entry[key]
            i=i+1
    match=0
        

wb.save('Castle Oil.xlsx')













