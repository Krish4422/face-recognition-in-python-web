# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        # This part is image labels setting start 
        # first header image  
        img = Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\banner.jpg")
        img = img.resize((1366, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\synthetic-data-1024x640.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Panel",font=("verdana",28,"bold"),bg="black",fg="gray")
        title_lb1.place(x=0,y=0,width=1366,height=45)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\istockphoto-1166057711-612x612.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="gray",fg="black")
        std_b1_1.place(x=600,y=350,width=180,height=45)
    #=====================Attendance===================
    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")

    #================face recognition==================
    def face_recog(self):

        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, recognizer):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = recognizer.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100 * (1 - predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Krishnamkmk4422@", database="krish")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from stud where Student_ID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else ""  # Check if n is iterable before applying join()

                my_cursor.execute("select Roll_No from stud where Student_ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else ""  # Check if i is iterable before applying join()

                my_cursor.execute("select Department from stud where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if i else ""


                if confidence > 77:
                    cv2.putText(img,f"Roll_No:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{r}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,recognizer,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",recognizer)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,recognizer,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1)== 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
