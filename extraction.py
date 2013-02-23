## Extraction Algorithms
RIGHT=1
LEFT=-1
## Raw Extraction
## Raw Castle Library
raw_Castle_Lib = (["Address","RE:",1,RIGHT,50],
                  ["Account#","ACCOUNT",1,RIGHT,50],
                  ["Gallons","P.B.T.",1,LEFT,20],
                  ["Tax","NY SALES TAX",1,LEFT,20],
                  ["Sales Tax","NY SALES TAX",1,RIGHT,8],
                  ["Discount","COUNT =",1,RIGHT,10],
                  ["Total-Discount","PAY ONLY",1,RIGHT,10],
                  ["Delivery Date","AMOUNT",1,RIGHT,10],
                  ["Fuel Oil Type","FUEL OIL",1,LEFT,2])

#Collection type, data name, keyword, instance, direction, raw chars to collect,
#stop_method, stop_key, use in final table

refined_Castle_Lib = ([0,"Address","RE:",1,RIGHT,30,"keyword","DATE","NO"],
                  [0,"Account#","ACCOUNT",1,RIGHT,30,"numbers",3,"NO"],
                  [0,"Gallons","P.B.T.",1,LEFT,30,"space-delimited",2,"YES"],
                  [0,"Base Price","P.B.T.",1,LEFT,30,"space-delimited",1,"NO"],
                  [0,"Tax","NY SALES TAX",1,LEFT,30,"space-delimited",1,"NO"],
                  [0,"Sales Tax","NY SALES TAX",1,RIGHT,30,"space-delimited",1,"NO"],
                  [0,"Discount","COUNT =",1,RIGHT,30,"numbers",3,"NO"],
                  [0,"Total-Discount","PAY ONLY",1,RIGHT,30,"numbers",3,"NO"],
                  [0,"Delivery Date","AMOUNT",1,RIGHT,30,"date","mm/dd/yyyy","YES"],
                  [0,"Fuel Oil Type","FUEL OIL",1,LEFT,30,"keyword-include","#","YES"],
                  [1,"Cost","ADD","Total-Discount","Total-Discount"])


## Takes some text and looks for the desired instance of the flag, starting in the direction you choose
## I should add an optional argument to start at a desired index.
def get_index(text,flag,inst,direc):
## if the direction is the right
    if direc==RIGHT:
## Then you can start at the beginning of the text
        char_index=0
## Do this once for every instance (Probably a slow way to do this)
        for i in range(inst):
## See if you can find the desired string
            try:
            ## if you can, get the index
                char_index=text.index(flag,char_index)
            except:
            ## if you can't make, char_index a string
                char_index="Instance Not Found"
        ## If you're looking for the second instance, the starting char
        ## has now been reset and you look for the string again.
        ## if at any time you don't find the string, it doesn't exit the loop (would be smart)
        ## it just keeps assigning the same string to char_index because it won't be able to
        ## use .index properly. 
        return char_index
    ## If the direction is LEFT
    ## it works the same as above, but starts at the end of the string and goes left.
    else:
        char_index=len(text)
        for i in range(inst):
            try:
                char_index=text.rindex(flag,char_index)
            except:
                char_index="Instance Not Found"
        return char_index

## This is a printer I slapped together to see if I was collecting the right stuff,
## which is good, because I totally wasn't
## eventually I will replace this with a xlsx printer (from openpyxl)
def csv_printer(data_list,file_path):
    file_handle=file(file_path,'a')
    for item in data_list:
##        print item
##        print item[0]
        file_handle.write('"'),
        file_handle.write(str(item[1])),
        file_handle.write('"'),
        file_handle.write(",")
    file_handle.write("\n")
    file_handle.close()

## Place holder function?
def raw_extract(raw_lib,page_text):
    print "stuff"
    
def get_raw_chars(page_string,data_flag,flag_inst,direction,num_chars):
    try:
        if direction==RIGHT:
            start_index=get_index(page_text,data_flag,flag_inst)+len(data_flag)
            end_index=start_index+num_chars
            raw_text=page_text[start_index:end_index].strip()
        elif direction==LEFT:
            end_index=get_index(page_text,data_flag,flag_inst)
            start_index=end_index-num_chars-len(data_flag)
            raw_text=page_text[start_index:end_index].strip()
    except:
        raw_text="FLAG NOT FOUND"
    return raw_text

## ----------------- extraction functions for every case--------(yeah right)
##Should I have these return an index or a string?
def stop_key_string(lib_entry,raw_text):
    if direction==RIGHT:
        end_index=get_index(raw_text,stop_key,stop_inst,RIGHT)
        refined_text=raw_text[:end_index].strip()
    else:
        start_index=get_index(raw_text,stop_key,stop_inst,LEFT)
        refined_text=raw_text[start_index:].strip()
    return refined_text


def stop_key_number(lib_entry,raw_text):
    if direction==RIGHT:
        end_index=index+stop_key
        refined_text=raw_text[start_index:].strip()
    else:
        start_index=index-stop_key

##-------------------------------------------------------------------------
## This uses the library and the functions above to get the desired data
## Found in the vicinity of each keyword
def refined_extract(refined_lib,page_text):

    ##this if statement is pointless right now, because there is only on lib
    if raw_lib=="raw_Castle_Lib":
        raw_lib=raw_Castle_Lib
    else:
        raw_lib=raw_Castle_Lib
        
    ##  Remove every '\n' PUT IN BY TESS and put everything back together with a space!    
    page_text=" ".join(page_text.splitlines())
    
    ##  Make room for all the stuff you'll be collecting
    raw_text_list=[]
    refined_text_list=[]

    ## go through all of the entries in refined lib because it's what you need to get
    ## to do the utility analysis
    for entry in refined_lib:
        #if collection type is 0 then: (Collection type denotes wether you need to get a new string
        # or use already collected values (like summing two values)
        
        coll_type,data_type,data_flag,flag_inst,direction,num_chars,stop_mthd,stop_key,fin_tab=entry[:]
        
        raw_text=get_raw_chars(page_text,data_flag,flag_inst,direction,num_chars)
        raw_text_list.append(raw_text)
        #else:
    pretty_print=[]
    for i in range(len(raw_Castle_Lib)):
        pretty_print.append((raw_Castle_Lib[i][0],raw_text_list[i]))
    for item in pretty_print: print item
    return pretty_print
