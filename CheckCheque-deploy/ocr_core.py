try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
from random import randint
import pandas as pd
def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename)) 
    val=str(filename)
    val=list(val)
    naam=""
    tt=0
    for i in range(15,len(val)):
    	    if(val[i]!="'"):
    	    	naam+=val[i]
    	    	if(val[i]=='g'):
    	    		tt=1
    	    if(tt==1):
    	    	break
    image = cv2.imread("/home/sahil/CheckCheque-deploy/static/uploads/"+str(naam))
    k=randint(0, 999999) 
    cropped1 = image[290:500, 320:1540]
    cv2.imwrite("/home/sahil/CheckCheque-deploy/static/extracted/name"+str(k)+".png", cropped1)
    name=pytesseract.image_to_string(Image.open("/home/sahil/CheckCheque-deploy/static/extracted/name"+str(k)+".png"))
    cropped2 = image[470:700, 670:2640]
    cv2.imwrite("/home/sahil/CheckCheque-deploy/static/extracted/amount"+str(k)+".png", cropped2)
    amount=pytesseract.image_to_string(Image.open("/home/sahil/CheckCheque-deploy/static/extracted/amount"+str(k)+".png"))
    cropped3 = image[850:1000, 480:1040]
    cv2.imwrite("/home/sahil/CheckCheque-deploy/static/extracted/acc_no"+str(k)+".png", cropped3)
    acc_no=pytesseract.image_to_string(Image.open("/home/sahil/CheckCheque-deploy/static/extracted/acc_no"+str(k)+".png"))
    # cropped4 = image[0:350, 2540:5000]
    # cv2.imwrite("/static/extracted/date"+str(k)+".png", cropped4)
    # date=pytesseract.image_to_string(Image.open("/home/sahil/CheckCheque-deploy/static/extracted/date"+str(k)+".png"))
    cropped5 = image[500:850, 2940:4500]
    cv2.imwrite("/home/sahil/CheckCheque-deploy/static/extracted/amt_num"+str(k)+".png", cropped5)
    amt_num=pytesseract.image_to_string(Image.open("/home/sahil/CheckCheque-deploy/static/extracted/amt_num"+str(k)+".png"))
    acc_no1=""
    lnum=["1","0","2","3","4","5","6","7","8","9"]
    for i in range(0,len(acc_no)):
    	if(str(acc_no[i]) in lnum):
    		acc_no1+=acc_no[i]
    l=[name,acc_no,amt_num]
    df = pd.read_csv("/home/sahil/CheckCheque-deploy/jobchahiye.csv")
    df.loc[df.Account== int(l[1]), 'Amount'] -=int(l[2])
    df.loc[df.Name== str(l[0]), 'Amount'] +=int(l[2])
    df.to_csv("/home/sahil/CheckCheque-deploy/jobchahiye.csv", index=False) 
    return l

	