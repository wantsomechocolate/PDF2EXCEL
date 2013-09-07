import cv2
import numpy as np
from PIL import Image as Img
import numpy as np

print " Hough Lines demo "
print " Press h to draw lines using cv2.HoughLines()"
print " Press p to draw lines using cv2.HoughLinesP()"
print " All the parameter values selected at random, Change it the way you like"

##im=Img.open('compare_8.png')
##
##im=im.resize((int(float(im.size[0])/1),int(float(im.size[1])/1)))
##
##im=np.array(im)

im = cv2.imread('compare_8.png')
try:
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
except:
    gray=im
edges = cv2.Canny(gray,150,200,apertureSize = 3)

cv2.imshow('houghlines',im)

while(True):
    img = im.copy()
    k = cv2.waitKey(0)

    if k == ord('h'):   # Press 'h' to enable cv2.HoughLines()
        lines = cv2.HoughLines(edges,1,np.pi/180,275)
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))   # Here i have used int() instead of rounding the decimal value, so 3.8 --> 3
            y1 = int(y0 + 1000*(a))    # But if you want to round the number, then use np.around() function, then 3.8 --> 4.0
            x2 = int(x0 - 1000*(-b))   # But we need integers, so use int() function after that, ie int(np.around(x))
            y2 = int(y0 - 1000*(a))
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.imshow('houghlines',img)

    elif k == ord('p'): # Press 'p' to enable cv2.HoughLinesP()
        
        lines = cv2.HoughLinesP(edges,1,np.pi/180,150, minLineLength = 100, maxLineGap = 10)


        slope_list=[]
        for x1,y1,x2,y2 in lines[0]:
            try:
                slope=float(y2-y1)/float(x2-x1)
                slope_list.append(slope)
            except: pass
            
        ave_slope=np.average(slope_list)
        #print ave_slope
        std_dev_slope=np.std(slope_list)
        #print std_dev_slope
        
        upper_bound=ave_slope+std_dev_slope
        #print upper_bound
        lower_bound=ave_slope-std_dev_slope
        #print lower_bound

        one_std_slope_list=[]
        for item in slope_list:
            if item < upper_bound:
                if item > lower_bound:
                    one_std_slope_list.append(item)

        one_std_ave_slope=np.average(one_std_slope_list)
        
        angle_deg=np.arctan(one_std_ave_slope)*180/np.pi
        
        print "Degree rotation is: " + str(angle_deg)

        image=Img.open('compare_8.png')
        image2=image.rotate(angle_deg)
        image2.save('compare_8_deskew.png')
        
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.imshow('houghlines',img)

    

    elif k == 27:    # Press 'ESC' to exit
        break

cv2.destroyAllWindows()
