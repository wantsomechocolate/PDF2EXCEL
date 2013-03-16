import os
import Tkinter, tkFileDialog

def getPath(default_directory):
    origDir=os.getcwd()
    os.chdir(default_directory)
    root=Tkinter.Tk()                           ##  Explicitly call the root window so that you can...
    root.withdraw()                             ##  withdraw it!
    filePath=tkFileDialog.askopenfilename()     ##  imageFile will store the filename of the image you choose   
    root.destroy()                              ##  Some overkill
    os.chdir(origDir)
    return filePath
    ## This returns a full path - not a filename
