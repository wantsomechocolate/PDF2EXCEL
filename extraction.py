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
def get_index1(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
def get_index(text,flag,inst):
    index=0
    for i in range(inst):
        try:
            index=text.index(flag,index)
        except:
            index="Instance Not Found"
    return index
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
def stop_key_string(lib_entry,raw_text):
    if direction==RIGHT:
        end_index=get_index(raw_text,stop_key,stop_inst,RIGHT)
        refined_text=raw_text[:end_index].strip()
    else:
        start_index=get_index(raw_text,stop_key,stop_inst,LEFT)
        refined_text=raw_text[start_index:].strip()
def refined_extract(refined_lib,page_text):
    if raw_lib=="raw_Castle_Lib":
        raw_lib=raw_Castle_Lib
    else:
        raw_lib=raw_Castle_Lib   
    ##  Remove every '\n' and put everything back together with a space!    
    page_text=" ".join(page_text.splitlines())
    ##  Make room for all the stuff you'll be collecting
    raw_text_list=[]
    refinted_text_list=[]
    for entry in refined_lib:
        #if collection type is 0 then: 
            coll_type,data_type,data_flag,flag_inst,direction,num_chars,stop_mthd,stop_key,fin_tab=entry[:]
        raw_text=get_raw_chars(page_text,data_flag,flag_inst,direction,num_chars)
        raw_text_list.append(raw_text)
        #else:
    pretty_print=[]
    for i in range(len(raw_Castle_Lib)):
        pretty_print.append((raw_Castle_Lib[i][0],raw_text_list[i]))
    for item in pretty_print: print item
    return pretty_print
