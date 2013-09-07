# import Image and the graphics package Tkinter
import Tkinter 
import Image, ImageTk

# open a SPIDER image and convert to byte
format
im = Image.open('compare_8.png')
image_width=im.size[0]
image_height=im.size[1]

IAR=float(im.size[0])/float(im.size[1])
print IAR

from win32api import GetSystemMetrics
screen_width=GetSystemMetrics (0)
screen_height=GetSystemMetrics (1)

if screen_width<im.size[0]:
    print "Too Wide!"
    im=im.resize((screen_width-100,int((screen_width-100)/IAR)))

if screen_height<im.size[1]:
    print "Too Tall!"
    im=im.resize((int((screen_height-100)*IAR),screen_height-100))

root = Tkinter.Tk()  
# A root window for displaying objects

 # Convert the Image object into a TkPhoto 
object
tkimage = ImageTk.PhotoImage(im)

Tkinter.Label(root, image=tkimage).pack() 
# Put it in the display window

root.mainloop() # Start the GUI


##import pygtk as gtk
##
##class ScaleImage:
##    def __init__(self):
##        self.temp_height = 0
##        self.temp_width = 0
##
##        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
##
##        image = gtk.Image()
##        image.set_from_file('/home/my_test_image.jpg')
##        self.pixbuf = image.get_pixbuf()
##        image.connect('expose-event', self.on_image_resize, window)    
##
##        box = gtk.ScrolledWindow()
##        box.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
##        box.add(image)
##
##        window.add(box)
##        window.set_size_request(300, 300)
##        window.show_all()        
##
##    def on_image_resize(self, widget, event, window):
##        allocation = widget.get_allocation()
##        if self.temp_height != allocation.height or self.temp_width != allocation.width:
##            self.temp_height = allocation.height
##            self.temp_width = allocation.width
##            pixbuf = self.pixbuf.scale_simple(allocation.width, allocation.height, gtk.gdk.INTERP_BILINEAR)
##            widget.set_from_pixbuf(pixbuf)
##
##    def close_application(self, widget, event, data=None):
##        gtk.main_quit()
##        return False
##
##if __name__ == "__main__":
##    ScaleImage()
##    gtk.main()
##

##from Tkinter import *
##import tkFont
##import Image #This is the PIL Image library
##
##im_temp = Image.open('compare_8.png')
##im_temp = im_temp.resize((250, 250), Image.ANTIALIAS)
##im_temp.save("ArtWrk.ppm", "ppm") ## The only reason I included this was to convert
###The image into a format that Tkinter woulden't complain about
##self.photo = PhotoImage(file="artwrk.ppm")##Open the image as a tkinter.PhotoImage class()
##self.Artwork.destroy() #erase the last drawn picture (in the program the picture I used was changing)
##self.Artwork = Label(self.frame, image=self.photo) #Sets the image too the label
##self.Artwork.photo = self.photo ##Make the image actually display (If I dont include this it won't display an image)
##self.Artwork.pack() ##repack the image

##import os,sys
##from PyQt4 import QtGui
##
##app = QtGui.QApplication(sys.argv)
##window = QtGui.QMainWindow()
##window.setGeometry(0, 0, 400, 200)
##
##pic = QtGui.QLabel(window)
##pic.setGeometry(0, 0, 1000, 1000)
###use full ABSOLUTE path to the image, not relative
##pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/compare_8.png"))
##
##window.show()
##sys.exit(app.exec_())

###!/usr/bin/python
### -*- coding: utf-8 -*-
##
##"""
##ZetCode PyQt4 tutorial 
##
##This example shows a tooltip on 
##a window and a button
##
##author: Jan Bodnar
##website: zetcode.com 
##last edited: October 2011
##"""
##
###import sys
##from PyQt4 import QtGui
##
##
####class Example(QtGui.QWidget):
####    
####    def __init__(self):
####        super(Example, self).__init__()
####        
####        self.initUI()
####        
####    def initUI(self):
####        
####        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
####        
####        self.setToolTip('This is a <b>QWidget</b> widget')
####        
####        btn = QtGui.QPushButton('Button', self)
####        btn.setToolTip('This is a <b>QPushButton</b> widget')
####        btn.resize(btn.sizeHint())
####        btn.move(50, 50)       
####        
####        self.setGeometry(300, 300, 250, 150)
####        self.setWindowTitle('Tooltips')    
####        self.show()
####        
####def main():
####    
####    app = QtGui.QApplication(sys.argv)
####    ex = Example()
####    sys.exit(app.exec_())
####
####
####if __name__ == '__main__':
####    main()
##
####import cv2
####from PIL import Image as Img
####import numpy as np
####
####def on_mouse(event, x, y, flags, params):
####    if event == cv.CV_EVENT_LBUTTONDOWN:
####        print 'Start Mouse Position: '+str(x)+', '+str(y)
####        sbox = [x, y]
####        boxes.append(sbox)
####    elif event == cv.CV_EVENT_LBUTTONUP:
####        print 'End Mouse Position: '+str(x)+', '+str(y)
####        ebox = [x, y]
####        boxes.append(ebox)
####
####def testprint(val):
####    print val
####
####im = cv2.imread('compare_8.png')
####
####cv2.imshow('houghlines',im)
####
####cv2.createTrackbar("Slider",'houghlines',50,100,testprint)
####
####k = cv2.waitKey(0)
##
##
####
####count = 0
####while(1):
####    count += 1
####   # _,img = cap.read()
####    im = cv2.imread('compare_8.png')
####    img = cv2.blur(im, (3,3))
####
####    cv2.namedWindow('real image')
####    cv.SetMouseCallback('real image', on_mouse, 0)
####    cv2.imshow('real image', img)
####
####    if count < 50:
####        if cv2.waitKey(33) == 27:
####            cv2.destroyAllWindows()
####            break
####    elif count >= 50:
####        if cv2.waitKey(0) == 27:
####            cv2.destroyAllWindows()
####            break
####        count = 0
