import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Vehicle Damage Detection")



image2 =Image.open('a1.jpg')
image2 =image2.resize((w,h))

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 
lbl = tk.Label(root, text="Vehicle Damage Detection", font=('times', 35,' bold '), width=65,height=1,bg="brown",fg="white")
lbl.place(x=0, y=0)


frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350, bd=5, font=('times', 14, ' bold '),bg="orange")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=100)



def update_label1(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=650)
    
    
    
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
def update_cal(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=350, y=350)
    
    
    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModel.main()
    print(X)
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    update_label(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from keras.models import load_model


    
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
      
       
        model = load_model('vehicle_model.h5')
            
     
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        
        

        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        yoga=np.argmax(prediction)
        print(yoga)
        
        
        
                
        
        
        if yoga == 0:
            Cd=" damaged"
            
        if yoga == 1:
            Cd="  not damaged"
      
            
        A=Cd
        return A
    img = open(fn)    
    myfile = open("C:/Users/hsang/Downloads/vehicle damage detection 100% code (1)/vehicle damage detection 100% code/testing")
    if img == myfile:
          print(myfile)


def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=420)


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        X1="Selected Car is {0}".format(X)
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ X1 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
    
def openimage():
   
    global fn
    print(fn)
    fileName = askopenfilename(initialdir='C:/Users/hsang/Downloads/vehicle damage detection 100% code (1)/vehicle damage detection 100% code/testing', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName



    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)



    x1 = int(img.shape[0])
    y1 = int(img.shape[1])


    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root,text='Original',font=('times new roman', 20 ,'bold'), image=imgtk,compound='bottom', height=250, width=250)
    

    img.image = imgtk
    img.place(x=300, y=100)


def convert_grey():
    global fn 
    print(fn)
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
 
    img2 = tk.Label(root,text='Gray',font=('times new roman', 20 ,'bold'), image=imgtk,compound='bottom', height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)
  

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root,text='Binary',font=('times new roman', 20 ,'bold'), image=imgtk,compound='bottom', height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    


def window():

    root.destroy()
    




button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=50)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=120)


button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=190)




exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=260)



root.mainloop()