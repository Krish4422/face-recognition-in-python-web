from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from training import Train
from attendance import Attendance
from helpsupport import Helpsupport
import os
from Face_id import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

        img=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\banner1.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        first_lb1 = Label(self.root,image=self.photoimg)
        first_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image

        bg1=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\face-off-banner.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        #title section
        title_lb1 = Label(bg_img,text="Face Recognition Attendance Management System ",font=("verdana",28,"bold"),bg="black",fg="gray")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # student button 
        std_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\studentm.jpg")
        std_img_btn=std_img_btn.resize((150,150),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,command=self.student_pannels,cursor="hand2")
        std_b1.place(x=180,y=100,width=180,height=150)

        std_b1_1 = Button(bg_img,text="Administration Panel",command=self.student_pannels,cursor="hand2",font=("tahoma",12,"bold"),bg="gray",fg="black")
        std_b1_1.place(x=180,y=250,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\download.jfif")
        det_img_btn=det_img_btn.resize((150,150),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",command=self.face_rec)
        det_b1.place(x=430,y=100,width=150,height=150)

        det_b1_1 = Button(bg_img,text="Face Detection",cursor="hand2",command=self.face_rec,font=("tahoma",12,"bold"),bg="gray",fg="black")
        det_b1_1.place(x=430,y=250,width=150,height=45)

        # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\images (2).jfif")
        att_img_btn=att_img_btn.resize((150,150),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",command=self.attendance_pannel)
        att_b1.place(x=685,y=100,width=150,height=150)

        att_b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_pannel,font=("tahoma",12,"bold"),bg="gray",fg="black")
        att_b1_1.place(x=685,y=250,width=150,height=45)

        
         # Train   button 5
        tra_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\download (1).jfif")
        tra_img_btn=tra_img_btn.resize((150,150),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,image=self.tra_img1,cursor="hand2",command=self.train_pannels)
        tra_b1.place(x=940,y=100,width=150,height=150)

        tra_b1_1 = Button(bg_img,text="Data Train",cursor="hand2",command=self.train_pannels,font=("tahoma",12,"bold"),bg="gray",fg="black")
        tra_b1_1.place(x=940,y=250,width=150,height=45)


        # Start below buttons.........
            # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\images (3).jfif")
        hlp_img_btn=hlp_img_btn.resize((150,150),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",command=self.Helpsupports)
        hlp_b1.place(x=300,y=330,width=150,height=150)

        hlp_b1_1 = Button(bg_img,text="Help Support",cursor="hand2",command=self.Helpsupports,font=("tahoma",12,"bold"),bg="gray",fg="black")
        hlp_b1_1.place(x=300,y=480,width=150,height=45)
        
        
        # Photo   button 6
        pho_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\pngtree.png")
        pho_img_btn=pho_img_btn.resize((150,150),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,image=self.pho_img1,cursor="hand2",command=self.open_img)
        pho_b1.place(x=550,y=330,width=150,height=150)

        pho_b1_1 = Button(bg_img,text="Data set",cursor="hand2",command=self.open_img,font=("tahoma",12,"bold"),bg="gray",fg="black")
        pho_b1_1.place(x=550,y=480,width=150,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"C:\Users\admin\Desktop\Face reg\GUI Images\exit.png")
        exi_img_btn=exi_img_btn.resize((150,150),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,image=self.exi_img1,cursor="hand2",command=self.Close)
        exi_b1.place(x=820,y=330,width=150,height=150)

        exi_b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.Close,font=("tahoma",12,"bold"),bg="gray",fg="black")
        exi_b1_1.place(x=820,y=480,width=150,height=45)

# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def Helpsupports(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Close(self):
        root.destroy()
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
