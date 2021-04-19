from tkinter import *
import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter_custom_button import TkinterCustomButton
from datetime import date
from tkinter import ttk
import datetime
import sys
from fpdf import FPDF
import webbrowser
import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets  # uic
from PyQt5.QtWidgets import (QLabel)  # +++
from PyQt5.QtCore import QTimer
import shutil
from test2_ui import Ui_Form
import numpy as np
import time
import imutils
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageTk
import subprocess
import re

# Load Yolo
# net = cv2.dnn.readNet("yolov3-tiny_last.weights", "yolov3-tiny.cfg")
# classes = []
# with open("classes3.txt", "r") as f:
#     classes = [line.strip() for line in f.readlines()]
net = cv2.dnn.readNet("yolov3-tiny_final.weights", "yolov3Copy.cfg")
classes = []
with open("classes4.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()
frame_id = 0

today = date.today()
date = datetime.datetime.now().date()
# temporary lists like sessions
products_list = []
product_price = []
product_quantity = []
product_id = []
# list for labels
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()f
root = Tk()
# root1 = Tk()
# root2 = Tk()
# root.overrideredirect(True)
root.title("COMPANY BOSSCCOM")
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(),  root.winfo_screenheight() ))
newWindowaddf = Toplevel(root)
newWindowaddf.title("add infomation")
newWindowaddf.geometry("980x550+0+0")
#

addWindow = tk.Tk()
addWindow.title("Set form print")
addWindow.geometry("980x550+0+0")
#

labels_list = []
var = IntVar()
var1 = IntVar()
c = StringVar()
c1 = StringVar()
logic1 = 1
USERNAME = StringVar()
PASSWORD = StringVar()
n = tk.StringVar()
n1 = tk.StringVar()
v1 = root.winfo_screenheight() / 12
vi1 = int(v1)
v2 = root.winfo_screenwidth() / 10
vi2 = int(v2)
v3 = root.winfo_screenwidth() - vi2-100
vi3 = int(v3)
v4 = vi2 + 50
vi4 = int(v4)

class AutocompleteEntry(Entry):

    def set_completion_list(self, completion_list):
        self._completion_list = completion_list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def autocomplete(self, delta=0):
        if delta:
            self.delete(self.position,END)
        else:
            self.position = len(self.get())
        _hits = []
        for element in self._completion_list:
            if element.startswith(self.get().lower()):
                _hits.append(element)
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
        if _hits == self._hits and self._hits:
                self._hit_index = (self._hit_index + delta) % len(self._hits)
        if self._hits:
                self.delete(0,END)
                self.insert(0,self._hits[self._hit_index])
                self.select_range(self.position,END)

    def handle_keyrelease(self, event):
        if len(event.keysym)== 1:
            self.autocomplete()


class Application:

    def __init__(self, master):

        self.master = master
        self.logic1 = 1
        self.logic2 = 1
        self.logic3 = 1
        self.logic4 = 1
        self.logicc3 = 1
        load = Image.open("icon/nen.JPG")
        render = ImageTk.PhotoImage(load)
        img = Label(master, image=render)
        img.image = render
        img.place(x=0, y=0)
        # frame
        # self.left = Frame(master, width=220, height=root.winfo_screenheight(), bg='lightskyblue1')
        # self.left.place(x=0, y=0)
        # self.left.pack(side=LEFT)
        # # self.left.pack(fill=TOP)#, expand=1)


        imageb1 = ImageTk.PhotoImage(Image.open("icon/ic.JPG").resize(((5+vi2+5), vi1)))
        imageb2 = ImageTk.PhotoImage(Image.open("icon/benhnhan.JPG").resize((vi2, vi1)))
        imageb3 = ImageTk.PhotoImage(Image.open("icon/benhan.JPG").resize((vi2, vi1)))
        imageb4 = ImageTk.PhotoImage(Image.open("icon/noisoi.JPG").resize((vi2, vi1)))
        imageb5 = ImageTk.PhotoImage(Image.open("icon/chandoan.JPG").resize((vi2, vi1)))
        imageb6 = ImageTk.PhotoImage(Image.open("icon/ketqua.JPG").resize((vi2, vi1)))
        imageb7 = ImageTk.PhotoImage(Image.open("icon/timkiem.JPG").resize((vi2, vi1)))
        imageb8 = ImageTk.PhotoImage(Image.open("icon/danhmuc.JPG").resize((vi2, vi1)))
        imageb9 = ImageTk.PhotoImage(Image.open("icon/ttthietbi.JPG").resize((vi2,vi1)))
        imageb10 = ImageTk.PhotoImage(Image.open("icon/thoat.JPG").resize((vi2, vi1)))

        self.button_1 = TkinterCustomButton(image=imageb1, width=(5+vi2+5), height=vi1)
        self.button_1.place(x=25, y=5)

        self.button_2 = TkinterCustomButton(image=imageb2, width=vi2, height=vi1, command=self.ajax)
        self.button_2.place(x=30, y=(vi1)+5)

        self.bt_st_form = TkinterCustomButton(image=imageb3, width=vi2, height=vi1, command=self.aj111)  # get_itemsdatabase)
        self.bt_st_form.place(x=30, y=(vi1*2)+10)

        self.bt_patient = TkinterCustomButton(image=imageb4, width=vi2, height=vi1,command=self.endoscopy)
        self.bt_patient.place(x=30, y=(vi1*3)+15)

        self.bt_endoscop = TkinterCustomButton(image=imageb5, width=vi2, height=vi1, command=self.cd111)
        self.bt_endoscop.place(x=30, y=(vi1*4)+20)

        self.bt_exit1 = TkinterCustomButton(image=imageb6, width=vi2, height=vi1,command=self.quit)
        self.bt_exit1.place(x=30, y=(vi1*5)+25)

        self.bt = TkinterCustomButton(image=imageb7, width=vi2, height=vi1, command=self.timkiem)
        self.bt.place(x=30, y=(vi1*6)+30)

        self.bt = TkinterCustomButton(image=imageb8, width=vi2, height=vi1,command=self.infortab111)
        self.bt.place(x=30, y=(vi1*7)+35)

        self.bt_e= TkinterCustomButton(image=imageb9, width=vi2, height=vi1, command=self.add_to_bn)
        self.bt_e.place(x=30, y=(vi1*8)+40)

        self.bt_exi= TkinterCustomButton(image=imageb10, width=vi2, height=vi1,command=self.quit)
        self.bt_exi.place(x=30, y=(vi1*9)+45)

        imageb11 = ImageTk.PhotoImage(Image.open("icon/mo.JPG").resize((vi2, vi1)))
        imageb12 = ImageTk.PhotoImage(Image.open("icon/sua.JPG").resize((vi2, vi1)))
        imageb13 = ImageTk.PhotoImage(Image.open("icon/luu.JPG").resize((vi2, vi1)))
        imageb14 = ImageTk.PhotoImage(Image.open("icon/xoa.JPG").resize((vi2, vi1)))
        imageb15 = ImageTk.PhotoImage(Image.open("icon/dong.JPG").resize((vi2,vi1)))

        self.bt_add_patient = TkinterCustomButton(image=imageb11, width=vi2, height=vi1, command=self.get_itemsdatabase)
        self.bt_add_patient.place(x=vi2+100, y=30)
        self.bt_add_patient = TkinterCustomButton(image=imageb12, width=vi2, height=vi1, command=self.get_itemsdatabase)
        self.bt_add_patient.place(x=(vi2*2)+130, y=30)
        self.bt_add_patient = TkinterCustomButton(image=imageb13, width=vi2, height=vi1, command=self.get_itemsdatabase)
        self.bt_add_patient.place(x=(vi2*3)+160, y=30)
        self.bt_add_patient = TkinterCustomButton(image=imageb14, width=vi2, height=vi1, command=self.Deletedata)
        self.bt_add_patient.place(x=(vi2*4)+190, y=30)
        self.bt_add_patient = TkinterCustomButton(image=imageb15, width=vi2, height=vi1, command=self.add_to_cart)
        self.bt_add_patient.place(x=(vi2*5)+220, y=30)

        addWindow.withdraw()
        newWindowaddf.withdraw()

    def Search(self):
        # =====================================Table WIDGET=========================================
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM `member` WHERE `name` LIKE ? AND `job` LIKE ? AND `address` LIKE ? AND `age` LIKE ?",
            ('%' + str(self.name_infos.get()) + '%', '%' + str(self.from_jobs.get()) + '%',
             '%' + str(self.from_addss.get()) + '%', '%' + str(self.born_agess.get()) + '%'))
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        self.name_infos.delete(0, tk.END)
        self.from_jobs.delete(0, tk.END)
        self.from_addss.delete(0, tk.END)
        self.born_agess.delete(0, tk.END)

    def ajax(self):
        # self.add_to_cart()
        if (self.logic1 == 1):
            in1 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            in2 = int((root.winfo_screenwidth() - vi2 - 100) / 6)
            in3 = int((root.winfo_screenwidth() - vi2 - 100) / 10)
            in4 = int((root.winfo_screenwidth() - vi2 - 100) / 10)
            in5 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            in6 = int(root.winfo_screenheight() - vi1+380- (vi2*5)-220)
            in7 = int(((vi1*9)+45)/30)

            self.bottom = Frame(root, width=vi3, height=250)#, bg='lightblue')
            # self.bottom.pack(side=TOP)
            self.bottom.place(x=vi4, y=vi1+50)

            # self.bottom1 = Frame(root, width=vi3, height=80, bg='yellow')
            # self.bottom1.place(x=vi4, y=400)

            self.bottom2 = Frame(root, width=vi3, height=in6, bg='lightblue')
            self.bottom2.place(x=vi4, y=vi1+310)

            load = Image.open("icon/nen.JPG")
            render = ImageTk.PhotoImage(load)
            img = Label(self.bottom2, image=render)
            img.image = render
            img.place(x=0, y=0)

            self.Top = Frame(self.bottom2, width=vi3, bd=2, relief=SOLID)
            self.Top.pack(side=TOP)
            self.MidFrame = Frame(self.bottom2, width=vi3)
            self.MidFrame.pack(side=TOP)
            self.RightForm = Frame(self.MidFrame, width=vi3)
            self.RightForm.pack(side=RIGHT)

            img = Label(self.bottom, image=render)
            img.image = render
            img.place(x=0, y=0)


            # img = Label(self.bottom1, image=render)
            # img.image = render
            # img.place(x=0, y=0)

            self.tenbenhnhan = Label(self.bottom, text="THÔNG TIN BỆNH NHÂN:", font=('arial 12 bold'), fg='black')
            self.tenbenhnhan.place(x=0, y=0)

            self.hoten = Label(self.bottom, text="Họ và tên     :", font=('arial 10 bold'), fg='black',
                                     bg='lightblue')
            self.hoten.place(x=10, y=30)

            self.hoten_p = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.hoten_p.place(x=100, y=30)
            self.hoten_p.focus()

            self.adr = Label(self.bottom, text="Địa chỉ         :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.adr.place(x=10, y=65)

            self.diachi_p = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.diachi_p.place(x=100, y=65)

            self.tel = Label(self.bottom, text="Điện thoại    :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.tel.place(x=10, y=100)
            self.sdtw = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.sdtw.place(x=100, y=100)

            self.mbn = Label(self.bottom, text="Mã BN          :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.mbn.place(x=10, y=135)

            self.mbn_bn = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.mbn_bn.place(x=100, y=135)

            self.sbh = Label(self.bottom, text="Số bảo hiểm:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.sbh.place(x=10, y=170)
            self.nbh = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.nbh.place(x=100, y=170)

            self.ghi = Label(self.bottom, text="Ghi chú   :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.ghi.place(x=10, y=205)
            self.ghich = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.ghich.place(x=100, y=205)

            self.year_b = Label(self.bottom, text="Năm sinh     :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.year_b.place(x=340, y=30)

            self.nam_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.nam_b.place(x=435, y=30)

            self.job = Label(self.bottom, text="Nghề nghiệp:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.job.place(x=340, y=65)
            # self.jobw = Entry(self.bottom, font=('arial 20 bold'), width=18)
            # self.jobw.place(x=320, y=30)
            test_list = ('tự do', 'sinh viên', 'học sinh', 'nông dân', 'bác sĩ', 'kĩ sư', 'công nhân', 'kĩ sư', 'giáo viên', 'nội trợ', 'kinh doanh','nhân viên văn phòng', 'kế toán')

            self.nghenghiep = AutocompleteEntry(self.bottom, font=('arial 14 bold'), width=10,textvariable=n)
            self.nghenghiep.set_completion_list(test_list)
            self.nghenghiep.place(x=435, y=65)

            self.gt = Label(self.bottom, text="Giới tính       :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.gt.place(x=340, y=100)

            self.gt_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.gt_b.place(x=435, y=100)

            self.nm = Label(self.bottom, text="Nhóm máu   :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.nm.place(x=340, y=135)

            self.nm_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.nm_b.place(x=435, y=135)

            self.ditruyen = Label(self.bottom, text="Di truyền      :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.ditruyen.place(x=340, y=170)

            self.ditruyen_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.ditruyen_b.place(x=435, y=170)

            self.bamsinh = Label(self.bottom, text="Bẩm sinh      :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.bamsinh.place(x=340, y=205)

            self.bamsinh_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.bamsinh_b.place(x=435, y=205)

            self.tsb = Label(self.bottom, text="Tiền sử bệnh :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.tsb.place(x=560, y=30)

            self.tsb_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.tsb_b.place(x=660, y=30)

            self.bhmac = Label(self.bottom, text="Bệnh hay mắc:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.bhmac.place(x=560, y=65)
            # self.jobw = Entry(self.bottom, font=('arial 20 bold'), width=18)
            # self.jobw.place(x=320, y=30)
            test_list = ('tự do', 'sinh viên', 'học sinh', 'nông dân', 'bác sĩ', 'kĩ sư', 'công nhân', 'kĩ sư', 'giáo viên','nội trợ', 'kinh doanh', 'nhân viên văn phòng', 'kế toán')

            self.bhmac_m = AutocompleteEntry(self.bottom, font=('arial 14 bold'), width=10, textvariable=n)
            self.bhmac_m.set_completion_list(test_list)
            self.bhmac_m.place(x=660, y=65)

            self.d_ung = Label(self.bottom, text="Dị ứng     :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.d_ung.place(x=560, y=100)

            self.d_ung_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.d_ung_b.place(x=660, y=100)

            self.tq = Label(self.bottom, text="Thói quen SH  :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.tq.place(x=560, y=135)

            self.thoiquen_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.thoiquen_b.place(x=660, y=135)

            self.lsk = Label(self.bottom, text="Lịch sử KCB :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.lsk.place(x=560, y=170)

            self.lsk_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.lsk_b.place(x=660, y=170)

            self.ppdk = Label(self.bottom, text="PP điều trị:", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.ppdk.place(x=560, y=205)

            self.ppdk_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.ppdk_b.place(x=660, y=205)

            self.scrollbarx = Scrollbar(self.RightForm, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.RightForm, orient=VERTICAL)
            self.tree = ttk.Treeview(self.RightForm, columns=("TT", "Tên bệnh nhân","Điện Thoại",  "Nghề nghiệp",  "Năm sinh","Bệnh án", "Nội Soi", "Chẩn Đoán", "Ngày Khám", "Chọn"),
                                     height=in7,selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
            self.scrollbary.config(command=self.tree.yview)
            self.scrollbary.pack(side=RIGHT, fill=Y)
            self.scrollbarx.config(command=self.tree.xview)
            self.scrollbarx.pack(side=TOP, fill=X)

            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=in1)
            self.tree.column('#2', stretch=NO, minwidth=0, width=in2)
            self.tree.column('#3', stretch=NO, minwidth=0, width=in3)
            self.tree.column('#4', stretch=NO, minwidth=0, width=in4)
            self.tree.column('#5', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#6', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#7', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#8', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#9', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#10', stretch=NO, minwidth=0, width=in5)

            self.tree.pack()
            self.tree.heading('TT', text="TT", anchor=W)
            self.tree.heading('Tên bệnh nhân', text="Tên bệnh nhân", anchor=W)
            self.tree.heading('Điện Thoại', text="Điện Thoại", anchor=W)
            self.tree.heading('Nghề nghiệp', text="Nghề nghiệp", anchor=W)
            self.tree.heading('Năm sinh', text="Năm sinh", anchor=W)
            self.tree.heading('Bệnh án', text="Bệnh án", anchor=W)
            self.tree.heading('Nội Soi', text="Nội Soi", anchor=W)
            self.tree.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
            self.tree.heading('Ngày Khám', text="Ngày Khám", anchor=W)
            self.tree.heading('Chọn', text="Chọn", anchor=W)

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `member`")
            fetch = cursor.fetchall()
            for data in fetch:
                self.tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            self.logic1 = 2

    def timkiem(self):
        # self.add_to_cart()
        if (self.logic2 == 1):
            in1 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            in2 = int((root.winfo_screenwidth() - vi2 - 100) / 6)
            in3 = int((root.winfo_screenwidth() - vi2 - 100) / 10)
            in4 = int((root.winfo_screenwidth() - vi2 - 100) / 10)
            in5 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            in6 = int(root.winfo_screenheight() - vi1+380- (vi2*5)-220)
            in7 = int(((vi1*9)+45)/30)

            self.bottom = Frame(root, width=vi3, height=500)#, bg='lightblue')
            # self.bottom.pack(side=TOP)
            self.bottom.place(x=vi4, y=vi1+50)

            # self.bottom1 = Frame(root, width=vi3, height=80, bg='yellow')
            # self.bottom1.place(x=vi4, y=400)

            self.bottom2 = Frame(root, width=vi3, height=in6, bg='lightblue')
            self.bottom2.place(x=vi4, y=vi1+310)

            load = Image.open("icon/nen.JPG")
            render = ImageTk.PhotoImage(load)
            img = Label(self.bottom2, image=render)
            img.image = render
            img.place(x=0, y=0)

            self.Top = Frame(self.bottom2, width=vi3, bd=2, relief=SOLID)
            self.Top.pack(side=TOP)
            self.MidFrame = Frame(self.bottom2, width=vi3)
            self.MidFrame.pack(side=TOP)
            self.RightForm = Frame(self.MidFrame, width=vi3)
            self.RightForm.pack(side=RIGHT)

            img = Label(self.bottom, image=render)
            img.image = render
            img.place(x=0, y=0)

            self.tenbenhnhan = Label(self.bottom, text="Họ và tên     :", font=('arial 10 bold'), fg='black',
                                     bg='lightblue')
            self.tenbenhnhan.place(x=10, y=30)

            self.name_p = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.name_p.place(x=100, y=30)
            self.name_p.focus()

            self.adr = Label(self.bottom, text="Địa chỉ      :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.adr.place(x=10, y=65)

            self.adr_p = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.adr_p.place(x=100, y=65)

            self.tel = Label(self.bottom, text="Điện thoại    :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.tel.place(x=10, y=100)
            self.telw = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.telw.place(x=100, y=100)

            self.mbn = Label(self.bottom, text="Nghề nghiệp:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.mbn.place(x=10, y=135)

            self.y_bn = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.y_bn.place(x=100, y=135)

            self.sbh = Label(self.bottom, text="Đơn vị C.tác", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.sbh.place(x=10, y=170)
            self.nbh = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.nbh.place(x=100, y=170)

            self.ghic = Label(self.bottom, text=" Bs.chỉ định  :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.ghic.place(x=10, y=205)
            self.ghich = Entry(self.bottom, font=('arial 14 bold'), width=20)
            self.ghich.place(x=100, y=205)

            self.year_b = Label(self.bottom, text="Số phiếu     :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.year_b.place(x=340, y=30)

            self.y_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.y_b.place(x=435, y=30)

            self.job = Label(self.bottom, text="Số bảo hiểm:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.job.place(x=340, y=65)
            # self.jobw = Entry(self.bottom, font=('arial 20 bold'), width=18)
            # self.jobw.place(x=320, y=30)
            test_list = ('tự do', 'sinh viên', 'học sinh', 'nông dân', 'bác sĩ', 'kĩ sư', 'công nhân', 'kĩ sư', 'giáo viên', 'nội trợ', 'kinh doanh','nhân viên văn phòng', 'kế toán')

            self.enter = AutocompleteEntry(self.bottom, font=('arial 14 bold'), width=10,textvariable=n)
            self.enter.set_completion_list(test_list)
            self.enter.place(x=435, y=65)

            self.gt = Label(self.bottom, text="tiền sử bệnh :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.gt.place(x=340, y=100)

            self.gt_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.gt_b.place(x=435, y=100)

            self.nm = Label(self.bottom, text="Dị ứng  :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.nm.place(x=340, y=135)

            self.nm_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.nm_b.place(x=435, y=135)

            self.ditruyen = Label(self.bottom, text="Lí do khám :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.ditruyen.place(x=340, y=170)

            self.ditruyen_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.ditruyen_b.place(x=435, y=170)

            self.nm = Label(self.bottom, text="Ghi chú   :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.nm.place(x=340, y=205)

            self.nm_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.nm_b.place(x=435, y=205)

            self.tsb = Label(self.bottom, text="Năm sinh :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.tsb.place(x=560, y=30)

            self.tsb_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.tsb_b.place(x=660, y=30)

            self.bhm = Label(self.bottom, text="Giới tính:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.bhm.place(x=560, y=65)
            # self.jobw = Entry(self.bottom, font=('arial 20 bold'), width=18)
            # self.jobw.place(x=320, y=30)
            test_list = (
            'tự do', 'sinh viên', 'học sinh', 'nông dân', 'bác sĩ', 'kĩ sư', 'công nhân', 'kĩ sư', 'giáo viên',
            'nội trợ', 'kinh doanh', 'nhân viên văn phòng', 'kế toán')

            self.bhn_m = AutocompleteEntry(self.bottom, font=('arial 14 bold'), width=10, textvariable=n)
            self.bhn_m.set_completion_list(test_list)
            self.bhn_m.place(x=660, y=65)

            self.du = Label(self.bottom, text="Nhóm máu   :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.du.place(x=560, y=100)

            self.du_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.du_b.place(x=660, y=100)

            self.tq = Label(self.bottom, text="Di truyền  :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.tq.place(x=560, y=135)

            self.tq_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.tq_b.place(x=660, y=135)

            self.lsk = Label(self.bottom, text="Lần khám :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.lsk.place(x=560, y=170)

            self.lsk_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.lsk_b.place(x=660, y=170)

            self.ppdk = Label(self.bottom, text="T lần khám:", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.ppdk.place(x=560, y=205)

            self.ppdk_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.ppdk_b.place(x=660, y=205)


            self.ppdk = Label(self.bottom, text="T lần khám:", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.ppdk.place(x=560, y=205)

            self.ppdk_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.ppdk_b.place(x=660, y=205)


            self.ppdk = Label(self.bottom, text="T lần khám:", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.ppdk.place(x=10, y=250)

            self.ppdk_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.ppdk_b.place(x=100, y=250)


            self.scrollbarx = Scrollbar(self.RightForm, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.RightForm, orient=VERTICAL)
            self.tree = ttk.Treeview(self.RightForm, columns=("TT", "Tên bệnh nhân","Điện Thoại",  "Nghề nghiệp",  "Năm sinh","Bệnh án", "Nội Soi", "Chẩn Đoán", "Ngày Khám", "Chọn"),
                                     height=in7,selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
            self.scrollbary.config(command=self.tree.yview)
            self.scrollbary.pack(side=RIGHT, fill=Y)
            self.scrollbarx.config(command=self.tree.xview)
            self.scrollbarx.pack(side=TOP, fill=X)

            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=in1)
            self.tree.column('#2', stretch=NO, minwidth=0, width=in2)
            self.tree.column('#3', stretch=NO, minwidth=0, width=in3)
            self.tree.column('#4', stretch=NO, minwidth=0, width=in4)
            self.tree.column('#5', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#6', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#7', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#8', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#9', stretch=NO, minwidth=0, width=in5)
            self.tree.column('#10', stretch=NO, minwidth=0, width=in5)

            self.tree.pack()
            self.tree.heading('TT', text="TT", anchor=W)
            self.tree.heading('Tên bệnh nhân', text="Tên bệnh nhân", anchor=W)
            self.tree.heading('Điện Thoại', text="Điện Thoại", anchor=W)
            self.tree.heading('Nghề nghiệp', text="Nghề nghiệp", anchor=W)
            self.tree.heading('Năm sinh', text="Năm sinh", anchor=W)
            self.tree.heading('Bệnh án', text="Bệnh án", anchor=W)
            self.tree.heading('Nội Soi', text="Nội Soi", anchor=W)
            self.tree.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
            self.tree.heading('Ngày Khám', text="Ngày Khám", anchor=W)
            self.tree.heading('Chọn', text="Chọn", anchor=W)

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `member`")
            fetch = cursor.fetchall()
            for data in fetch:
                self.tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            self.logic2 = 2


    def cd111(self):
        # self.add_to_cart()
        if (self.logic3 == 1):
            in1 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            in2 = int((root.winfo_screenwidth() - vi2 - 100) / 6)
            in3 = int((root.winfo_screenwidth() - vi2 - 100) / 10)
            in4 = int((root.winfo_screenwidth() - vi2 - 100) / 10)
            in5 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            in6 = int(root.winfo_screenheight() - vi1 + 380 - (vi2 * 5) - 220)
            in7 = int(((vi1 * 9) + 45) / 30)

            self.bottom = Frame(root, width=vi3, height=root.winfo_screenheight())  # , bg='lightblue')
            # self.bottom.pack(side=TOP)
            self.bottom.place(x=vi4, y=vi1 + 50)


            load = Image.open("icon/nen.JPG")
            render = ImageTk.PhotoImage(load)

            img = Label(self.bottom, image=render)
            img.image = render
            img.place(x=0, y=0)

            # img = Label(self.bottom1, image=render)
            # img.image = render
            # img.place(x=0, y=0)

            self.tenbenhnhan = Label(self.bottom, text="Chẩn đoán :", font=('arial 10 bold'), fg='black',
                                     bg='lightblue')
            self.tenbenhnhan.place(x=20, y=40)

            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=140, y=30)
            self.name_p.focus()
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=30)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=30)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68,height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=55)

            self.adr = Label(self.bottom, text="Đánh giá :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.adr.place(x=20, y=90)
            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=90)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=90)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=90)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black',bg='gray70')
            self.adr.place(x=140, y=115)

            self.adr = Label(self.bottom, text="Hướng diều trị:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.adr.place(x=20, y=150)
            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=150)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=150)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=150)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=175)

            self.adr = Label(self.bottom, text="Lời dặn bác sĩ:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.adr.place(x=20, y=210)
            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=210)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=210)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=210)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=235)

            self.adr = Label(self.bottom, text="Đơn thuốc:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.adr.place(x=20, y=270)
            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=270)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=270)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=270)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=295)

            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=325)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=325)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=325)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=350)

            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=380)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=380)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=380)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=405)

            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=435)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=435)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=435)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=460)

            self.adr_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.adr_p.place(x=140, y=490)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=380, y=490)
            self.name_p = Entry(self.bottom, font=('arial 12 bold'), width=24)
            self.name_p.place(x=620, y=490)
            self.adr = Label(self.bottom, font=('arial 12 bold'), width=68, height=1, fg='black', bg='gray70')
            self.adr.place(x=140, y=515)

            self.logicc3 = 2

    def aj111(self):
        # self.add_to_cart()
        if (self.logic4 == 1):
            i1 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            i2 = int((root.winfo_screenwidth() - vi2 - 100) / 6)
            i3 = int((root.winfo_screenwidth() - vi2 - 100) / 10)
            i4 = int((root.winfo_screenwidth() - vi2 - 100) / 12)
            i5 = int(root.winfo_screenheight() - vi1+380 - (vi2*5)-220)
            i6 = int(((vi1*9)+45)/30)

            self.bottom = Frame(root, width=vi3, height=180)#, bg='lightblue')
            # self.bottom.pack(side=TOP)
            self.bottom.place(x=vi4, y=vi1+50)

            # self.bottom1 = Frame(root, width=vi3, height=80, bg='yellow')
            # self.bottom1.place(x=vi4, y=400)

            self.bottom2 = Frame(root, width=vi3, height=i5, bg='lightblue')
            self.bottom2.place(x=vi4, y=vi1+240)

            load = Image.open("icon/nen.JPG")
            render = ImageTk.PhotoImage(load)
            img = Label(self.bottom2, image=render)
            img.image = render
            img.place(x=0, y=0)

            self.Top = Frame(self.bottom2, width=vi3, bd=2, relief=SOLID)
            self.Top.pack(side=TOP)
            self.MidFrame = Frame(self.bottom2, width=vi3)
            self.MidFrame.pack(side=TOP)
            self.RightForm = Frame(self.MidFrame, width=vi3)
            self.RightForm.pack(side=RIGHT)

            img = Label(self.bottom, image=render)
            img.image = render
            img.place(x=0, y=0)

            self.tenbenhnhan = Label(self.bottom, text="THÔNG TIN BỆNH NHÂN:", font=('arial 12 bold'), fg='black')
            self.tenbenhnhan.place(x=0, y=0)

            self.tenbenhnhan = Label(self.bottom, text="Họ và tên     :", font=('arial 10 bold'), fg='black',
                                     bg='lightblue')
            self.tenbenhnhan.place(x=10, y=30)

            self.name_p = Entry(self.bottom, font=('arial 14 bold'), width=25)
            self.name_p.place(x=100, y=30)
            self.name_p.focus()

            self.adr = Label(self.bottom, text="Địa chỉ         :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.adr.place(x=10, y=65)

            self.adr_p = Entry(self.bottom, font=('arial 14 bold'), width=25)
            self.adr_p.place(x=100, y=65)

            self.tel = Label(self.bottom, text="Điện thoại    :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.tel.place(x=10, y=100)
            self.telw = Entry(self.bottom, font=('arial 14 bold'), width=25)
            self.telw.place(x=100, y=100)

            self.mbn = Label(self.bottom, text="Mã BN          :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.mbn.place(x=10, y=135)

            self.y_bn = Entry(self.bottom, font=('arial 14 bold'), width=25)
            self.y_bn.place(x=100, y=135)

            self.year_b = Label(self.bottom, text="Năm sinh       :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.year_b.place(x=400, y=30)

            self.y_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.y_b.place(x=495, y=30)

            self.year_b = Label(self.bottom, text="Số phiếu:", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.year_b.place(x=400, y=30)

            self.y_b = Entry(self.bottom, font=('arial 14 bold'), width=10)
            self.y_b.place(x=495, y=30)
            self.year_b = Label(self.bottom, text="Khám lần :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.year_b.place(x=615, y=30)
            self.y_b3 = Entry(self.bottom, font=('arial 14 bold'), width=7)
            self.y_b3.place(x=690, y=30)

            self.job = Label(self.bottom, text="Nghề nghiệp :", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.job.place(x=400, y=65)
            # self.jobw = Entry(self.bottom, font=('arial 20 bold'), width=18)
            # self.jobw.place(x=320, y=30)
            test_list = ('tự do', 'sinh viên', 'học sinh', 'nông dân', 'bác sĩ', 'kĩ sư', 'công nhân', 'kĩ sư', 'giáo viên', 'nội trợ', 'kinh doanh','nhân viên văn phòng', 'kế toán')

            self.enter = AutocompleteEntry(self.bottom, font=('arial 14 bold'), width=25,textvariable=n)
            self.enter.set_completion_list(test_list)
            self.enter.place(x=495, y=65)

            self.gt = Label(self.bottom, text="Giới tính        :", font=('arial 10 bold'), fg='black',
                                bg='lightblue')
            self.gt.place(x=400, y=100)

            self.gt_b = Entry(self.bottom, font=('arial 14 bold'), width=25)
            self.gt_b.place(x=495, y=100)

            self.gt = Label(self.bottom, text="Giới tính        :", font=('arial 10 bold'), fg='black',
                            bg='lightblue')
            self.gt.place(x=400, y=135)

            self.gt_b = Entry(self.bottom, font=('arial 14 bold'), width=25)
            self.gt_b.place(x=495, y=135)

            self.scrollbarx = Scrollbar(self.RightForm, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.RightForm, orient=VERTICAL)
            self.tree = ttk.Treeview(self.RightForm, columns=("TT", "Tên bệnh nhân","Điện Thoại",  "Nghề nghiệp",  "Năm sinh","Bệnh án", "Nội Soi", "Chẩn Đoán", "Ngày Khám", "Chọn"),
                                     height=i6,selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
            self.scrollbary.config(command=self.tree.yview)
            self.scrollbary.pack(side=RIGHT, fill=Y)
            self.scrollbarx.config(command=self.tree.xview)
            self.scrollbarx.pack(side=TOP, fill=X)

            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=i1)
            self.tree.column('#2', stretch=NO, minwidth=0, width=i2)
            self.tree.column('#3', stretch=NO, minwidth=0, width=i3)
            self.tree.column('#4', stretch=NO, minwidth=0, width=i4)
            self.tree.column('#5', stretch=NO, minwidth=0, width=i4)
            self.tree.column('#6', stretch=NO, minwidth=0, width=i4)
            self.tree.column('#7', stretch=NO, minwidth=0, width=i4)
            self.tree.column('#8', stretch=NO, minwidth=0, width=i4)
            self.tree.column('#9', stretch=NO, minwidth=0, width=i4)
            self.tree.column('#10', stretch=NO, minwidth=0, width=i4)

            self.tree.pack()
            self.tree.heading('TT', text="TT", anchor=W)
            self.tree.heading('Tên bệnh nhân', text="Tên bệnh nhân", anchor=W)
            self.tree.heading('Điện Thoại', text="Điện Thoại", anchor=W)
            self.tree.heading('Nghề nghiệp', text="Nghề nghiệp", anchor=W)
            self.tree.heading('Năm sinh', text="Năm sinh", anchor=W)
            self.tree.heading('Bệnh án', text="Bệnh án", anchor=W)
            self.tree.heading('Nội Soi', text="Nội Soi", anchor=W)
            self.tree.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
            self.tree.heading('Ngày Khám', text="Ngày Khám", anchor=W)
            self.tree.heading('Chọn', text="Chọn", anchor=W)

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `member`")
            fetch = cursor.fetchall()
            for data in fetch:
                self.tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            self.logic4 = 2

    def Deletedata(self):

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item in self.tree.selection():
            # print(selected_item)  # it prints the selected row id
            cursor.execute("DELETE FROM member WHERE id=?", (self.tree.set(selected_item, '#1'),))
            self.tree.delete(selected_item)
        conn.commit()
        conn.close()

    def Deletealldata(self):
        shutil.rmtree("anh")
        conn = sqlite3.connect("db_member.db")
        cur = conn.cursor()
        sql = 'DELETE FROM member'
        cur.execute(sql)
        conn.commit()

    def get_itemsdatabase(self):

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()

        if self.logic1 == 1 or self.name_p.get() == '' or self.adr_p.get() == '' or self.y_b.get() == '' or self.jobw.get() == '' or self.stom.get() == '' or self.nbh.get() == '' or c.get() == '' or self.telw.get() == '':
            tkinter.messagebox.showinfo("Error", "Điền đầy đủ thông tin bệnh nhân.")
        else:

            cursor.execute('INSERT INTO member (name, address, age, job, symptom,sbh,sex,tel ) VALUES(?,?,?,?,?,?,?,?)',
                           (
                               self.name_p.get(), self.adr_p.get(), self.y_b.get(), self.jobw.get(), self.stom.get(),
                               self.nbh.get(),
                               c.get(), self.telw.get()))
            conn.commit()
            self.name_p.delete(0, END)
            self.adr_p.delete(0, END)
            self.y_b.delete(0, END)
            self.jobw.delete(0, END)
            self.stom.delete(0, END)
            self.nbh.delete(0, END)
            self.telw.delete(0, END)
            self.endoscopy()
            # textbox insert
            # tkinter.messagebox.showinfo("Success", "Successfully added to the database")

    def add_to_cart(self):

        # self.right.destroy()
        self.bottom.destroy()
        # self.bottom1.destroy()
        self.bottom2.destroy()
        self.logic1 = 1
        # self.logic2 = 1
        # self.logic3 = 1
        # self.logic4 = 1

    def delete_text(self, *args, **kwargs):

        self.name_p.delete(0, END)
        self.adr_p.delete(0, END)
        self.y_b.delete(0, END)
        self.jobw.delete(0, END)
        self.stom.delete(0, END)
        self.nbh.delete(0, END)

    def database_print(self, *args, **kwargs):

        namepk = self.adr2_p.get()
        name_dt = self.doctor_p.get()
        address_pk = self.n2_p.get()
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if namepk == '' or name_dt == '' or address_pk == '':
            # self.logic2 = 2
            # tkinter.messagebox.showinfo("Error", "Điền đầy đủ thông tin.")
            self.addrn = Label(self.rightw3, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=200, y=520)
        else:

            cursor.execute("DELETE FROM print_dt WHERE id=1")
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt (name_pk TEXT,dt_name TEXT,address TEXT)')
            cursor.execute('INSERT INTO print_dt (name_pk,dt_name,address) VALUES(?,?,?)',
                           (namepk, name_dt, address_pk))
            # tkinter.messagebox.showinfo("Success", "Đã thêm thông tin")

            conn.commit()
            cursor.close()
            self.adr2_p.delete(0, END)
            self.doctor_p.delete(0, END)
            self.n2_p.delete(0, END)

            self.rightw2.destroy()
            self.rightw3.destroy()
            addWindow.update()
            addWindow.deiconify()
            self.rightw2 = Frame(addWindow, width=550, height=600, bg='lightblue')
            self.rightw2.pack(side=RIGHT)
            self.rightw3 = Frame(addWindow, width=600, height=600, bg='lightblue')
            self.rightw3.pack(side=LEFT)

            self.adr2 = Label(self.rightw3, text="Phòng khám:", font=('arial 16 bold'), fg='black', bg='lightblue')
            self.adr2.place(x=10, y=10)
            self.adr2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
            self.adr2_p.place(x=150, y=10)

            self.doctor = Label(self.rightw3, text=" Bác sĩ :", font=('arial 16 bold'), fg='black', bg='lightblue')
            self.doctor.place(x=10, y=85)

            self.doctor_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
            self.doctor_p.place(x=150, y=75)

            self.n2 = Label(self.rightw3, text="Địa chỉ:", font=('arial 16 bold'), fg='black', bg='lightblue')
            self.n2.place(x=10, y=155)

            self.n2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
            self.n2_p.place(x=150, y=150)

            self.add_dt = Button(self.rightw3, text="Cập nhật", width=15, height=3, font=('arial 18 bold'),
                                 bg='orange',
                                 command=self.database_print)
            self.add_dt.place(x=40, y=220)

            self.add_dltd = Button(self.rightw3, text="Xóa", width=15, height=3, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.Deletedata_print)  # command=self.quit_print2)
            self.add_dltd.place(x=275, y=220)

            self.addrn = Label(self.rightw3, text="Icon Addr:", font=('arial 18 bold'), fg='black', bg='lightblue')
            self.addrn.place(x=10, y=360)

            self.addrn_p = Entry(self.rightw3, font=('arial 22 bold'), width=25)
            self.addrn_p.place(x=130, y=360)

            self.add_dl = Button(self.rightw3, text="Thêm Icon", width=15, height=3, font=('arial 18 bold'),
                                 bg='orange', command=self.openfile)
            self.add_dl.place(x=35, y=410)
            self.add_dl = Button(self.rightw3, text="Đóng", width=15, height=3, font=('arial 18 bold'),
                                 bg='orange', command=self.quit11)
            self.add_dl.place(x=260, y=410)
            self.addrn = Label(self.rightw3, text="Đã thêm đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=200, y=520)

            self.scrollbarx = Scrollbar(self.rightw2, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.rightw2, orient=VERTICAL)
            self.tree1 = ttk.Treeview(self.rightw2, columns=("Id", "Phòng khám", "Bác sĩ", "Địa chỉ"),
                                      selectmode="extended", yscrollcommand=self.scrollbary.set,xscrollcommand=self.scrollbarx.set)
            self.scrollbary.config(command=self.tree1.yview)
            self.scrollbary.pack(side=RIGHT, fill=Y)
            self.scrollbarx.config(command=self.tree1.xview)
            self.scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree1.column('#0', stretch=NO, minwidth=0, width=50)
            self.tree1.column('#1', stretch=NO, minwidth=0, width=20)
            self.tree1.column('#2', stretch=NO, minwidth=0, width=180)
            self.tree1.column('#3', stretch=NO, minwidth=0, width=120)
            self.tree1.column('#4', stretch=NO, minwidth=0, width=80)

            self.tree1.pack()
            self.tree1.heading('Id', text="Id", anchor=W)
            self.tree1.heading('Phòng khám', text="Phòng khám", anchor=W)
            self.tree1.heading('Bác sĩ', text="Bác sĩ", anchor=W)
            self.tree1.heading('Địa chỉ', text="Địa chỉ", anchor=W)
            self.tree1.pack()

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `print_dt`")
            fetch = cursor.fetchall()
            for data in fetch:
                self.tree1.insert('', 'end', values=(data))
            cursor.close()
            conn.close()

    def Deletedata_print(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree1.selection():
            print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt WHERE id=?", (self.tree1.set(selected_item1, '#1'),))
            conn.commit()
            self.tree1.delete(selected_item1)
        conn.commit()
        cursor.close()

    def Chosedata_print(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree1.selection():
            # print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt WHERE id=?", (self.tree1.set(selected_item1, '#1'),))
            conn.commit()
            self.tree1.delete(selected_item1)
        conn.commit()
        cursor.close()

    def database_print111(self):
        nameadd22 = c1.get() + " " + self.ad_if2.get()
        name_dt22 = self.ad_if2.get()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if nameadd22 == '' or name_dt22 == '':

            self.addrn = Label(self.rightw333, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

        else:
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt22 (name_pk22 TEXT,dt_name22 TEXT)')
            cursor.execute('INSERT INTO print_dt22 (name_pk22,dt_name22) VALUES(?,?)', (nameadd22, name_dt22))

            # tkinter.messagebox.showinfo("Success", "Đã thêm thông tin")
            conn.commit()
            cursor.close()

            self.ad_if2.delete(0, END)

            self.rightw222.destroy()
            self.rightw444.destroy()
            self.rightw333.destroy()
            newWindowaddf.update()
            newWindowaddf.deiconify()

            self.rightw222 = Frame(newWindowaddf, width=205, height=500, bg='lightblue')
            self.rightw222.pack(side=RIGHT)
            self.rightw444 = Frame(newWindowaddf, width=205, height=500, bg='lightyellow')
            self.rightw444.pack(side=RIGHT)
            self.rightw333 = Frame(newWindowaddf, width=540, height=500, bg='lightblue')
            self.rightw333.pack(side=LEFT)

            self.n3 = Label(self.rightw333, text="Danh Mục Chẩn Đoán:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n3.place(x=10, y=10)

            self.ad_if2 = Entry(self.rightw333, font=('arial 28 bold'), width=16)
            self.ad_if2.place(x=188, y=39)

            # self.n4 = Label(self.rightw3, text="Danh Mục:", font=('arial 14 bold'), fg='black', bg='lightblue')
            # self.n4.place(x=10, y=90)

            self.droplist1 = OptionMenu(self.rightw333, c1, 'TAI', 'MŨI', 'HỌNG')
            self.droplist1.pack()

            self.menu = self.droplist1.nametowidget(self.droplist1.menuname)
            self.menu.configure(font=('arial 28 bold'))
            c1.set('HỌNG')

            self.droplist1.config(width=9, height=1, font=('arial 20 bold'))
            self.droplist1.place(x=5, y=40)

            self.add_ifmt = Button(self.rightw333, text="Cập Nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_print111)
            self.add_ifmt.place(x=5, y=90)

            self.n4 = Label(self.rightw333, text="Phương Pháp Điều Trị:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n4.place(x=10, y=185)

            self.ad_j2 = Entry(self.rightw333, font=('arial 28 bold'), width=24)
            self.ad_j2.place(x=10, y=215)

            self.add_ifmj = Button(self.rightw333, text="Cập nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_printnn1)
            self.add_ifmj.place(x=5, y=270)

            self.add_dltifmtjj = Button(self.rightw333, text="Xóa", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.Deletedata_NewWindow)
            self.add_dltifmtjj.place(x=25, y=375)
            self.add_dltifmtjj = Button(self.rightw333, text="Đóng", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.quit22)
            self.add_dltifmtjj.place(x=260, y=375)
            self.addrn = Label(self.rightw333, text="Đã thêm đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

            # self.add_dltd = Button(self.rightw3, text="Đóng", width=14, height=2, font=('arial 20 bold'),
            #                        bg='orange', command=self.quit_print1)
            # self.add_dltd.place(x=5, y=400)
            scrollbary = Scrollbar(self.rightw222, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw222, orient=HORIZONTAL)
            self.tree2 = ttk.Treeview(self.rightw222, columns=("Danh Mục", "Chẩn Đoán"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree2.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree2.heading('Danh Mục', text="Danh Mục", anchor=W)
            self.tree2.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
            self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree2.column('#1', stretch=NO, minwidth=0, width=200)
            self.tree2.column('#2', stretch=NO, minwidth=0, width=0)
            self.tree2.pack()

            scrollbary = Scrollbar(self.rightw444, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw444, orient=HORIZONTAL)
            self.tree4 = ttk.Treeview(self.rightw444, columns=("Danh Mục Chẩn Đoán", "Chỉ Định"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree4.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree4.heading('Danh Mục Chẩn Đoán', text="Danh Mục Chẩn Đoán", anchor=W)
            self.tree4.heading('Chỉ Định', text="Chỉ Định", anchor=W)
            self.tree4.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#1', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#2', stretch=NO, minwidth=0, width=195)
            self.tree4.pack()

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor1 = conn.cursor()
            cursor.execute("SELECT * FROM `print_dt22`")
            fetch = cursor.fetchall()
            cursor1.execute("SELECT * FROM `print_jb22`")
            fetch1 = cursor1.fetchall()
            for data in fetch:
                self.tree2.insert('', 'end', values=(data))
            for data1 in fetch1:
                self.tree4.insert('', 'end', values=(data1))
            cursor.close()
            conn.close()
            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            # addWindow.withdraw()
            # self.createNewWindow()

    def database_printnn1(self):
        name_dtn222 = self.ad_j2.get()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if name_dtn222 == '':
            self.addrn = Label(self.rightw333, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

        else:
            # cursor.execute('CREATE TABLE IF NOT EXISTS print_jb22 (name_pjb22 TEXT)')
            # cursor.execute('INSERT INTO print_jb22 (name_pjb22) VALUES(?)',(name_dtn222))
            cursor.execute('CREATE TABLE IF NOT EXISTS print_jb22 (name_j22 TEXT,dt_namej TEXT)')
            cursor.execute('INSERT INTO print_jb22 (name_j22,dt_namej) VALUES(?,?)', (name_dtn222, name_dtn222))

            conn.commit()
            cursor.close()

            self.ad_j2.delete(0, END)

            self.rightw222.destroy()
            self.rightw444.destroy()
            self.rightw333.destroy()
            newWindowaddf.update()
            newWindowaddf.deiconify()

            self.rightw222 = Frame(newWindowaddf, width=205, height=500, bg='lightblue')
            self.rightw222.pack(side=RIGHT)
            self.rightw444 = Frame(newWindowaddf, width=205, height=500, bg='lightyellow')
            self.rightw444.pack(side=RIGHT)
            self.rightw333 = Frame(newWindowaddf, width=540, height=500, bg='lightblue')
            self.rightw333.pack(side=LEFT)

            self.n3 = Label(self.rightw333, text="Danh Mục Chẩn Đoán:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n3.place(x=10, y=10)

            self.ad_if2 = Entry(self.rightw333, font=('arial 28 bold'), width=16)
            self.ad_if2.place(x=188, y=39)

            # self.n4 = Label(self.rightw3, text="Danh Mục:", font=('arial 14 bold'), fg='black', bg='lightblue')
            # self.n4.place(x=10, y=90)

            self.droplist1 = OptionMenu(self.rightw333, c1, 'TAI', 'MŨI', 'HỌNG')
            self.droplist1.pack()

            self.menu = self.droplist1.nametowidget(self.droplist1.menuname)
            self.menu.configure(font=('arial 28 bold'))
            c1.set('HỌNG')

            self.droplist1.config(width=9, height=1, font=('arial 20 bold'))
            self.droplist1.place(x=5, y=40)

            self.add_ifmt = Button(self.rightw333, text="Cập Nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_print111)
            self.add_ifmt.place(x=5, y=90)

            self.n4 = Label(self.rightw333, text="Phương Pháp Điều Trị:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n4.place(x=10, y=185)

            self.ad_j2 = Entry(self.rightw333, font=('arial 28 bold'), width=24)
            self.ad_j2.place(x=10, y=215)

            self.add_ifmj = Button(self.rightw333, text="Cập nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_printnn1)
            self.add_ifmj.place(x=5, y=270)

            self.add_dltifmtjj = Button(self.rightw333, text="Xóa", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.Deletedata_NewWindow)
            self.add_dltifmtjj.place(x=25, y=375)
            self.add_dltifmtjj = Button(self.rightw333, text="Đóng", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.quit22)
            self.add_dltifmtjj.place(x=260, y=375)
            self.addrn = Label(self.rightw333, text="Đã thêm đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

            # self.add_dltd = Button(self.rightw3, text="Đóng", width=14, height=2, font=('arial 20 bold'),
            #                        bg='orange', command=self.quit_print1)
            # self.add_dltd.place(x=5, y=400)
            scrollbary = Scrollbar(self.rightw222, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw222, orient=HORIZONTAL)
            self.tree2 = ttk.Treeview(self.rightw222, columns=("Danh Mục", "Chẩn Đoán"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree2.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree2.heading('Danh Mục', text="Danh Mục", anchor=W)
            self.tree2.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
            self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree2.column('#1', stretch=NO, minwidth=0, width=200)
            self.tree2.column('#2', stretch=NO, minwidth=0, width=0)
            self.tree2.pack()

            scrollbary = Scrollbar(self.rightw444, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw444, orient=HORIZONTAL)
            self.tree4 = ttk.Treeview(self.rightw444, columns=("Danh Mục Chẩn Đoán", "Chỉ Định"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree4.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree4.heading('Danh Mục Chẩn Đoán', text="Danh Mục Chẩn Đoán", anchor=W)
            self.tree4.heading('Chỉ Định', text="Chỉ Định", anchor=W)
            self.tree4.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#1', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#2', stretch=NO, minwidth=0, width=195)
            self.tree4.pack()

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor1 = conn.cursor()
            cursor.execute("SELECT * FROM `print_dt22`")
            fetch = cursor.fetchall()
            cursor1.execute("SELECT * FROM `print_jb22`")
            fetch1 = cursor1.fetchall()
            for data in fetch:
                self.tree2.insert('', 'end', values=(data))
            for data1 in fetch1:
                self.tree4.insert('', 'end', values=(data1))
            cursor.close()
            conn.close()
            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            # addWindow.withdraw()
            # self.createNewWindow()

    def openfile(self):  # open the file\
        # namepk = self.adr2_p.get()
        # name_dt = self.doctor_p.get()
        # address_pk = self.n2_p.get()

        address_addrn = self.addrn_p.get()
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if address_addrn == '':
            self.addrn = Label(self.rightw3, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='blue',
                               bg='white')
            self.addrn.place(x=200, y=520)
        else:
            cursor.execute("DELETE FROM print_dtadd WHERE addressadd=1")
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dtadd (name_pkadd TEXT,dt_nameadd TEXT)')
            cursor.execute('INSERT INTO print_dtadd (name_pkadd,dt_nameadd) VALUES(?,?)',
                           (address_addrn, address_addrn))
            self.addrn = Label(self.rightw3, text="Đã thêm biểu tượng   ! ", font=('arial 18 bold'), fg='blue',
                               bg='white')
            self.addrn.place(x=200, y=520)
            conn.commit()
            cursor.close()

    def createNewWindow(self, *args, **kwargs):
        # root.withdraw()

        newWindowaddf.update()
        newWindowaddf.deiconify()
        self.rightw222 = Frame(newWindowaddf, width=205, height=500, bg='lightblue')
        self.rightw222.pack(side=RIGHT)
        self.rightw444 = Frame(newWindowaddf, width=205, height=500, bg='lightyellow')
        self.rightw444.pack(side=RIGHT)
        self.rightw333 = Frame(newWindowaddf, width=540, height=500, bg='lightblue')
        self.rightw333.pack(side=LEFT)

        self.n3 = Label(self.rightw333, text="Danh Mục Chẩn Đoán:", font=('arial 14 bold'), fg='black', bg='lightblue')
        self.n3.place(x=10, y=10)

        self.ad_if2 = Entry(self.rightw333, font=('arial 28 bold'), width=16)
        self.ad_if2.place(x=188, y=39)

        # self.n4 = Label(self.rightw3, text="Danh Mục:", font=('arial 14 bold'), fg='black', bg='lightblue')
        # self.n4.place(x=10, y=90)

        self.droplist1 = OptionMenu(self.rightw333, c1, 'TAI', 'MŨI', 'HỌNG')
        self.droplist1.pack()

        self.menu = self.droplist1.nametowidget(self.droplist1.menuname)
        self.menu.configure(font=('arial 28 bold'))
        c1.set('HỌNG')

        self.droplist1.config(width=9, height=1, font=('arial 20 bold'))
        self.droplist1.place(x=5, y=40)

        self.add_ifmt = Button(self.rightw333, text="Cập Nhật", width=12, height=2, font=('arial 18 bold'), bg='orange',
                               command=self.database_print111)
        self.add_ifmt.place(x=5, y=90)

        self.n4 = Label(self.rightw333, text="Phương Pháp Điều Trị:", font=('arial 14 bold'), fg='black',
                        bg='lightblue')
        self.n4.place(x=10, y=185)

        self.ad_j2 = Entry(self.rightw333, font=('arial 28 bold'), width=24)
        self.ad_j2.place(x=10, y=215)

        self.add_ifmj = Button(self.rightw333, text="Cập nhật", width=12, height=2, font=('arial 18 bold'), bg='orange',
                               command=self.database_printnn1)
        self.add_ifmj.place(x=5, y=270)

        self.add_dltifmtjj = Button(self.rightw333, text="Xóa", width=16, height=2, font=('arial 18 bold'),
                                    bg='orange', command=self.Deletedata_NewWindow)
        self.add_dltifmtjj.place(x=25, y=375)
        self.add_dltifmtjj = Button(self.rightw333, text="Đóng", width=16, height=2, font=('arial 18 bold'),
                                    bg='orange', command=self.quit22)
        self.add_dltifmtjj.place(x=260, y=375)

        # self.add_dltd = Button(self.rightw3, text="Đóng", width=14, height=2, font=('arial 20 bold'),
        #                        bg='orange', command=self.quit_print1)
        # self.add_dltd.place(x=5, y=400)
        scrollbary = Scrollbar(self.rightw222, orient=VERTICAL)
        scrollbarx = Scrollbar(self.rightw222, orient=HORIZONTAL)
        self.tree2 = ttk.Treeview(self.rightw222, columns=("Danh Mục", "Chẩn Đoán"),
                                  selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                  xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree2.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree2.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree2.heading('Danh Mục', text="Danh Mục", anchor=W)
        self.tree2.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
        self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree2.column('#2', stretch=NO, minwidth=0, width=0)
        self.tree2.pack()

        scrollbary = Scrollbar(self.rightw444, orient=VERTICAL)
        scrollbarx = Scrollbar(self.rightw444, orient=HORIZONTAL)
        self.tree4 = ttk.Treeview(self.rightw444, columns=("Danh Mục Chẩn Đoán", "Chỉ Định"),
                                  selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                  xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree4.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree2.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree4.heading('Danh Mục Chẩn Đoán', text="Danh Mục Chẩn Đoán", anchor=W)
        self.tree4.heading('Chỉ Định', text="Chỉ Định", anchor=W)
        self.tree4.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree4.column('#1', stretch=NO, minwidth=0, width=0)
        self.tree4.column('#2', stretch=NO, minwidth=0, width=195)
        self.tree4.pack()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("SELECT * FROM `print_dt22`")
        fetch = cursor.fetchall()
        cursor1.execute("SELECT * FROM `print_jb22`")
        fetch1 = cursor1.fetchall()
        for data in fetch:
            self.tree2.insert('', 'end', values=(data))
        for data1 in fetch1:
            self.tree4.insert('', 'end', values=(data1))
        cursor.close()
        conn.close()


        # # root.withdraw()

    def add_to_bn(self, *args, **kwargs):
        # root.withdraw()

        addWindow.update()
        addWindow.deiconify()
        self.rightw2 = Frame(addWindow, width=550, height=600, bg='lightblue')
        self.rightw2.pack(side=RIGHT)
        self.rightw3 = Frame(addWindow, width=600, height=600, bg='lightblue')
        self.rightw3.pack(side=LEFT)

        self.adr2 = Label(self.rightw3, text="Phòng khám:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.adr2.place(x=10, y=10)
        self.adr2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
        self.adr2_p.place(x=150, y=10)

        self.doctor = Label(self.rightw3, text=" Bác sĩ :", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.doctor.place(x=10, y=85)

        self.doctor_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
        self.doctor_p.place(x=150, y=75)

        self.n2 = Label(self.rightw3, text="Địa chỉ:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.n2.place(x=10, y=155)

        self.n2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
        self.n2_p.place(x=150, y=150)

        self.add_dt = Button(self.rightw3, text="Cập nhật", width=15, height=3, font=('arial 18 bold'), bg='orange',
                             command=self.database_print)
        self.add_dt.place(x=40, y=220)

        self.add_dltd = Button(self.rightw3, text="Xóa", width=15, height=3, font=('arial 18 bold'), bg='orange',
                               command=self.Deletedata_print)  # command=self.quit_print2)
        self.add_dltd.place(x=275, y=220)

        self.addrn = Label(self.rightw3, text="Icon Addr:", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.addrn.place(x=10, y=360)

        self.addrn_p = Entry(self.rightw3, font=('arial 22 bold'), width=25)
        self.addrn_p.place(x=130, y=360)

        self.add_dl = Button(self.rightw3, text="Thêm Icon", width=15, height=3, font=('arial 18 bold'),
                             bg='orange', command=self.openfile)
        self.add_dl.place(x=35, y=410)
        self.add_dl = Button(self.rightw3, text="Đóng", width=15, height=3, font=('arial 18 bold'),
                             bg='orange', command=self.quit11)
        self.add_dl.place(x=260, y=410)

        self.scrollbarx = Scrollbar(self.rightw2, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.rightw2, orient=VERTICAL)
        self.tree1 = ttk.Treeview(self.rightw2, columns=("Id", "Phòng khám", "Bác sĩ", "Địa chỉ"),
                                  selectmode="extended",
                                  height=400, yscrollcommand=self.scrollbary.set,
                                  xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree1.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree1.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree1.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree1.column('#1', stretch=NO, minwidth=0, width=20)
        self.tree1.column('#2', stretch=NO, minwidth=0, width=180)
        self.tree1.column('#3', stretch=NO, minwidth=0, width=120)
        self.tree1.column('#4', stretch=NO, minwidth=0, width=80)

        self.tree1.pack()
        self.tree1.heading('Id', text="Id", anchor=W)
        self.tree1.heading('Phòng khám', text="Phòng khám", anchor=W)
        self.tree1.heading('Bác sĩ', text="Bác sĩ", anchor=W)
        self.tree1.heading('Địa chỉ', text="Địa chỉ", anchor=W)
        self.tree1.pack()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `print_dt`")
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree1.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def infortab111(self, *args, **kwargs):
        class Window2(QtWidgets.QDialog, Ui_Form):  # <===


            def __init__(self):
                super().__init__()
                # root.winfo_screenwidth(),  root.winfo_screenheight()
                self.title = "Print Window"
                self.top = 0
                self.left = 0
                self.width = int(root.winfo_screenwidth())
                self.height = int(root.winfo_screenheight())

                label = QLabel(self)
                pixmap = QPixmap('icon/nen.JPG')
                label.setPixmap(pixmap)
                self.resize(pixmap.width(), pixmap.height())

                self.pushButton = QPushButton('', self)
                self.pushButton.setGeometry(QtCore.QRect(25, 10, 180, 60))
                self.pushButton.setIcon(QIcon('icon/ic.JPG'))
                self.pushButton.setIconSize(QtCore.QSize(180, 70))

                self.pushButton = QPushButton('', self)
                self.pushButton.setGeometry(QtCore.QRect(35, (vi1)+20, 150,55))
                # self.pushButton.setToolTip("<h3>Start Print</h3>")
                self.pushButton.setIcon(QIcon('icon/tenthietbi.JPG'))
                self.pushButton.setIconSize(QtCore.QSize(150, 70))

                font = QFont('Times', 16)
                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1)+25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)

                self.pushButton2 = QPushButton("", self)
                self.pushButton2.setGeometry(QtCore.QRect(35, (vi1*2)+20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButton2.setIcon(QIcon('icon/mode.JPG'))
                self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1*2) + 25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)

                self.pushButton2 = QPushButton("", self)
                self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 3) + 20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButton2.setIcon(QIcon('icon/version.JPG'))
                self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 3) + 25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)

                self.pushButton2 = QPushButton("", self)
                self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 4) + 20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButton2.setIcon(QIcon('icon/soserial.JPG'))
                self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 4) + 25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)

                self.pushButton2 = QPushButton("", self)
                self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 5) + 20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButton2.setIcon(QIcon('icon/khachhang.JPG'))
                self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 5) + 25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)


                self.pushButton2 = QPushButton("", self)
                self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 6) + 20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButton2.setIcon(QIcon('icon/ngaybatdau.JPG'))
                self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 6) + 25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)

                self.pushButton2 = QPushButton("", self)
                self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 7) + 20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButton2.setIcon(QIcon('icon/update.JPG'))
                self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 7) + 25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)

                self.pushButtoncdk = QPushButton("", self)
                self.pushButtoncdk.setGeometry(QtCore.QRect(35, (vi1 * 8) + 20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButtoncdk.setIcon(QIcon('icon/caidatkhac.JPG'))
                self.pushButtoncdk.setIconSize(QtCore.QSize(150, 70))

                self.pushButton = QPushButton("", self)
                self.pushButton.setGeometry(QtCore.QRect(35, (vi1 * 9) + 20, 150, 55))
                # self.pushButton2.setToolTip("<h3>Close</h3>")
                self.pushButton.setIcon(QIcon('icon/thoat.JPG'))
                self.pushButton.setIconSize(QtCore.QSize(150, 70))

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 8) + 25, 550, 45))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)
                self.main_window()
                self.pushButtoncdk.clicked.connect(self.caidatkhac)
            def main_window(self):
                self.setWindowTitle(self.title)
                self.setGeometry(self.top, self.left, self.width, self.height)
                self.show()



            def caidatkhac(self, *args, **kwargs):
                class Window4(QtWidgets.QDialog, Ui_Form):  # <===

                    def __init__(self):
                        super().__init__()
                        # root.winfo_screenwidth(),  root.winfo_screenheight()
                        self.title = "Print Window"
                        self.top = 0
                        self.left = 0
                        self.width = int(root.winfo_screenwidth())
                        self.height = int(root.winfo_screenheight())

                        label = QLabel(self)
                        pixmap = QPixmap('icon/nen.JPG')
                        label.setPixmap(pixmap)
                        self.resize(pixmap.width(), pixmap.height())

                        self.pushButton = QPushButton('', self)
                        self.pushButton.setGeometry(QtCore.QRect(25, 10, 180, 60))
                        self.pushButton.setIcon(QIcon('icon/ic.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(180, 70))

                        self.pushButton = QPushButton('', self)
                        self.pushButton.setGeometry(QtCore.QRect(35, (vi1) + 20, 150, 55))
                        # self.pushButton.setToolTip("<h3>Start Print</h3>")
                        self.pushButton.setIcon(QIcon('icon/tendonvi.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(150, 70))

                        font = QFont('Times', 16)
                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1) + 25, 695, 45))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 2) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/diachi.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 2) + 25, 695, 45))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 3) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/dienthoai.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 3) + 25, 300, 45))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(550, (vi1 * 3) + 20, 100, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/mail.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(100, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(670, (vi1 * 3) + 25, 250, 45))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 4) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/ngd1.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 4) + 25, 250, 55))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 5) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/nd2.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 5) + 25, 250, 55))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(500, (vi1 * 4) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/passwo.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(670, (vi1 * 4) + 25, 250, 55))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(500, (vi1 * 5) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/passwo.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(670, (vi1 * 5) + 25, 250, 55))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 6) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/t.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 6) + 25, 550, 45))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton2 = QPushButton("", self)
                        self.pushButton2.setGeometry(QtCore.QRect(35, (vi1 * 7) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton2.setIcon(QIcon('icon/t.JPG'))
                        self.pushButton2.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 7) + 25, 550, 45))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButtoncdk = QPushButton("", self)
                        self.pushButtoncdk.setGeometry(QtCore.QRect(35, (vi1 * 8) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButtoncdk.setIcon(QIcon('icon/caidatkhac.JPG'))
                        self.pushButtoncdk.setIconSize(QtCore.QSize(150, 70))

                        self.pushButton = QPushButton("", self)
                        self.pushButton.setGeometry(QtCore.QRect(35, (vi1 * 9) + 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton.setIcon(QIcon('icon/thoat.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(150, 70))

                        self.lineEdit_3 = QtWidgets.QLineEdit(self)
                        self.lineEdit_3.setGeometry(QtCore.QRect(220, (vi1 * 8) + 25, 550, 45))
                        self.lineEdit_3.setObjectName("lineEdit_3")
                        self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                        self.lineEdit_3.setFont(font)

                        self.pushButton = QPushButton("", self)
                        self.pushButton.setGeometry(QtCore.QRect(220,  20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton.setIcon(QIcon('icon/mo.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(150, 70))

                        self.pushButton = QPushButton("", self)
                        self.pushButton.setGeometry(QtCore.QRect(390, 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton.setIcon(QIcon('icon/sua1.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(150, 70))

                        self.pushButton = QPushButton("", self)
                        self.pushButton.setGeometry(QtCore.QRect(560,  20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton.setIcon(QIcon('icon/luu.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(150, 70))

                        self.pushButton = QPushButton("", self)
                        self.pushButton.setGeometry(QtCore.QRect(730,20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton.setIcon(QIcon('icon/xoa.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(150, 70))

                        self.pushButton = QPushButton("", self)
                        self.pushButton.setGeometry(QtCore.QRect(900, 20, 150, 55))
                        # self.pushButton2.setToolTip("<h3>Close</h3>")
                        self.pushButton.setIcon(QIcon('icon/dong1.JPG'))
                        self.pushButton.setIconSize(QtCore.QSize(150, 70))

                        self.main_window2()

                    def main_window2(self):
                        self.setWindowTitle(self.title)
                        self.setGeometry(self.top, self.left, self.width, self.height)
                        self.show()

                self.w = Window4()
                self.w.show()

        self.w = Window2()
        self.w.show()


    def Deletedata_NewWindow(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree2.selection():
            # print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt22 WHERE name_pk22=?", (self.tree2.set(selected_item1, '#1'),))
            conn.commit()
            self.tree2.delete(selected_item1)
        for selected_item3 in self.tree4.selection():
            # print(selected_item3)  # it prints the selected row id
            cursor.execute("DELETE FROM print_jb22 WHERE name_j22=?", (self.tree4.set(selected_item3, '#1'),))
            conn.commit()
            self.tree4.delete(selected_item3)
        conn.commit()
        cursor.close()

    def quit(self):
        #  addWindow.destroy()
        #  #addWindow.deiconify()
        # # root.withdraw()
        # # newWindowaddf.update()
        #  newWindowaddf.destroy()
        # root.withdraw()

        root.withdraw()
        root.destroy()
        addWindow.destroy()

        # newWindowaddf.withdraw()
        # newWindowaddf.destroy()
        # root1.destroy()
        # root2.destroy

    def quit11(self):
        self.rightw2.destroy()
        self.rightw3.destroy()

        addWindow.withdraw()
        # root.deiconify()
        # root.update()
        # root1.destroy()
        # root2.destroy()

    def quit22(self):
        # root.deiconify()
        # root.update()
        self.rightw222.destroy()
        self.rightw444.destroy()
        self.rightw333.destroy()

        newWindowaddf.withdraw()
        # root.deiconify()
        # root.update()
        # root1.destroy()
        # root2.destroy()

    # def quit_print1(self):
    #
    #     tkinter.messagebox.showinfo("Success", "Thoát cài đặt danh mục")
    #     # root1.withdraw()
    #
    # def quit_print2(self):
    #     # root2.withdraw()
    #     tkinter.messagebox.showinfo("Success", "Thoát cài đặt biểu mẫu")
    #
    # def hide(self):
    #     root.withdraw()
    #
    # def show(self):
    #     root.update()
    #     root.deiconify()

    def create_pdf1(self):
        # Set up a logo
        conn = sqlite3.connect("db_member.db")
        conn.row_factory = sqlite3.Row
        for selected_item in self.tree.selection():
            print(selected_item)
        cur = conn.cursor()
        cur.execute("SELECT * FROM `member` WHERE id=?", (self.tree.set(selected_item, '#1'),))
        rows = cur.fetchall()
        for row in rows:
            row["id"]
        # webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["id"])))
        webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["id"])))

    def endoscopy(self):
        #         root.overrideredirect(False)
        #
        class Window2(QMainWindow):  # <===

            def __init__(self):
                super().__init__()
                self.anh1 = 1
                self.anh2 = 2
                self.anh3 = 3
                self.anh4 = 4
                self.anh5 = 5
                self.anh6 = 6
                self.cou = 0
                self.title = "Print Window"
                self.top = 0
                self.left = 0
                self.width = 1000
                self.height = 560

                self.listWidget = QtWidgets.QListWidget(self)
                self.listWidget.setGeometry(QtCore.QRect(680, 5, 300, 545))  # (2, 115, 213, 475))
                self.listWidget.setObjectName("ListWidgetItem")
                self.listWidget.setIconSize(QtCore.QSize(270, 180))
                self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
                self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)

                self.it = QtWidgets.QListWidgetItem(self.listWidget)
                self.it1 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it2 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it3 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it4 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it5 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it6 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it7 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it8 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it9 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it10 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it11 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it12 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it13 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it14 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it15 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it16 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it17 = QtWidgets.QListWidgetItem(self.listWidget)
                conn = sqlite3.connect("db_member.db")
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT max(id) FROM member")
                rows = cur.fetchall()
                # INSERT
                # INTO
                # print_jb22(name_j22, dt_namej)
                # VALUES(?, ?)

                # cur2 = conn.cursor()
                # cur2.execute("SELECT name_j22 FROM print_jb22")
                # rows2 = cur2.fetchall()
                # for row2 in rows2:
                #     row2["name_j22"]
                #     # print("%s" % (row2["name_j22(1)"]))
                # # completer = QCompleter(row2["name_j22"])
                directory = "anh/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                for row in rows:
                    # print("%s" % (row["max(id)"]))
                    row["max(id)"]

                font = QFont('Times', 16)

                self.it.setFont(font)
                self.it.setText("1  ")
                self.it1.setFont(font)
                self.it1.setText("2  ")
                self.it2.setFont(font)
                self.it2.setText("3  ")
                self.it3.setFont(font)
                self.it3.setText("4  ")
                self.it4.setFont(font)
                self.it4.setText("5  ")
                self.it5.setFont(font)
                self.it5.setText("6  ")
                self.it6.setFont(font)
                self.it6.setText("7  ")
                self.it7.setFont(font)
                self.it7.setText("8  ")
                self.it8.setFont(font)
                self.it8.setText("9  ")
                self.it9.setFont(font)
                self.it9.setText("10  ")
                self.it10.setFont(font)
                self.it10.setText("11  ")
                self.it11.setFont(font)
                self.it11.setText("12  ")
                self.it12.setFont(font)
                self.it12.setText("13  ")
                self.it13.setFont(font)
                self.it13.setText("14  ")
                self.it14.setFont(font)
                self.it14.setText("15  ")
                self.it15.setFont(font)
                self.it15.setText("16  ")
                self.it16.setFont(font)
                self.it16.setText("17  ")
                self.it17.setFont(font)
                self.it17.setText("18 ")

                self.TEXT = QtWidgets.QTextBrowser(self)
                self.TEXT.setGeometry(QtCore.QRect(100, 480, 450, 60))
                self.TEXT.setObjectName("TEXT")
                font1 = QFont('Times', 24)
                self.TEXT.setFont(font1)
                self.TEXT.setText('%s : png' % (
                        str(self.anh1) + ":" + str(self.anh2) + ":" + str(self.anh3) + ":" + str(
                    self.anh4) + ":" + str(self.anh5) + ":" + str(self.anh6)))

                self.it.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(1))))
                self.it1.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(2))))
                self.it2.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(3))))
                self.it3.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(4))))
                self.it4.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(5))))
                self.it5.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(6))))
                self.it6.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(7))))
                self.it7.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(8))))
                self.it8.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(9))))
                self.it9.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(10))))
                self.it10.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(11))))
                self.it11.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(12))))
                self.it12.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(13))))
                self.it13.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(14))))
                self.it14.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(15))))
                self.it15.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(16))))
                self.it16.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(17))))
                self.it17.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(18))))

                self.pushButton = QPushButton("In Phiếu Khám", self)
                self.pushButton.setGeometry(QtCore.QRect(80, 360, 250, 100))
                self.pushButton.setToolTip("<h3>Start Print</h3>")

                # self.pushButton1 = QPushButton("Chọn Ảnh Thủ Công", self)
                # self.pushButton1.setGeometry(QtCore.QRect(250, 360, 200, 100))
                # self.pushButton1.setToolTip("<h3>Start Print</h3>")

                self.pushButton2 = QPushButton("Đóng", self)
                self.pushButton2.setGeometry(QtCore.QRect(332, 360, 250, 100))
                self.pushButton2.setToolTip("<h3>Close</h3>")

                font = QtGui.QFont()
                font.setPointSize(20)
                font1 = QtGui.QFont()
                font1.setPointSize(16)

                self.text2 = QtWidgets.QLabel("Chẩn Đoán : ", self)
                self.text2.setGeometry(QtCore.QRect(90, 20, 225, 50))
                self.text2.setFont(font1)
                self.text1 = QtWidgets.QLabel("Điều Trị : ", self)
                self.text1.setGeometry(QtCore.QRect(90, 125, 200, 50))
                self.text1.setFont(font1)

                self.text2 = QtWidgets.QLabel("Chỉ Định : ", self)
                self.text2.setGeometry(QtCore.QRect(90, 225, 200, 50))
                self.text2.setFont(font1)

                # names = ["Apple", "Alps", "Berry", "Cherry"]
                # completer = QCompleter(names)

                self.lineEdit = QtWidgets.QLineEdit(self)
                self.lineEdit.setGeometry(QtCore.QRect(70, 70, 530, 50))
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit.setPlaceholderText('chẩn đoán')
                # self.lineEdit.setCompleter(completer)
                self.lineEdit.setFont(font)

                self.completer = QCompleter()
                self.lineEdit.setCompleter(self.completer)
                self.model = QStringListModel()
                self.completer.setModel(self.model)

                self.lineEdit_2 = QtWidgets.QLineEdit(self)
                self.lineEdit_2.setGeometry(QtCore.QRect(70, 170, 530, 50))
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_2.setPlaceholderText('Phương pháp điều trị')
                self.lineEdit_2.setFont(font)

                self.completer_2 = QCompleter()
                self.lineEdit_2.setCompleter(self.completer_2)
                self.model_2 = QStringListModel()
                self.completer_2.setModel(self.model_2)

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(70, 270, 530, 50))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)
                #  self.pushButton.move(275,420)
                self.pushButton.clicked.connect(self.create_pdf2)  # self.create_pdf2)
                # self.pushButton1.clicked.connect(self.window3)
                self.pushButton2.clicked.connect(self.winc)
                # self.listWidget.itemChanged.connect(self.call)
                self.listWidget.itemSelectionChanged.connect(self.on_change)
                # self.listWidget.itemClicked.connect(self.call)
                self.main_window()
                self.get_data()
                self.get_data1()

            def main_window(self):
                self.setWindowTitle(self.title)
                self.setGeometry(self.top, self.left, self.width, self.height)
                self.show()

            def get_data(self):
                conn = sqlite3.connect("db_member.db")
                c = conn.cursor()
                c.execute(" SELECT name_pk22 FROM print_dt22")
                results = c.fetchall()
                new_list = [i[0] for i in results]
                # print(new_list)  # Test print
                self.model.setStringList(new_list)  # From here up I was able to get the
                # code to work but there's no auto completion in the QLineEdit.

            def get_data1(self):
                conn = sqlite3.connect("db_member.db")
                cur2 = conn.cursor()
                cur2.execute("SELECT name_j22 FROM print_jb22")

                # print("%s" % (row2["name_j22(1)"]))
                # completer = QCompleter(row2["name_j22"])
                results = cur2.fetchall()
                new_list = [i[0] for i in results]
                # print(new_list)  # Test print
                self.model_2.setStringList(new_list)  # From here up I was able to get the
                # code to work but there's no auto completion in the QLineEdit.

            def on_change(self):
                self.cou = self.cou + 1

                inn = str([item.text() for item in self.listWidget.selectedItems()])
                # print(inn)
                k = inn[2:4]
                self.kk = int(k)
                # print(self.kk)
                # self.kk = int(k)
                if self.cou == 1:
                    self.anh1 = self.kk
                if self.cou == 2:
                    self.anh2 = self.kk
                if self.cou == 3:
                    self.anh3 = self.kk
                if self.cou == 4:
                    self.anh4 = self.kk
                if self.cou == 5:
                    self.anh5 = self.kk
                if self.cou == 6:
                    self.anh6 = self.kk
                self.TEXT.setText('%s.png' % (str(self.anh1) + ":" + str(self.anh2) + ":" + str(self.anh3) + ":" + str(
                    self.anh4) + ":" + str(self.anh5) + ":" + str(self.anh6)))

                if self.cou > 6:
                    self.cou = 0

                #     print(self.kk)
                # if self.kk==1:
                #     self.item.setCheckState(1)
                #     self.anh1=16

            # def call(self, qList):
            #     print(str(qList))
            #     index = self.listWidget.indexFromItem(qList)

            def winc(self):
                self.hide()

            # def call(self, qList):
            #     checkedItem = 0
            #     for index in range(self.listWidget.count()):
            #         if self.listWidget.item(index).checkState() == Qt.Checked:
            #             checkedItem += 1
            #     print(str(checkedItem))
            #
            #     imn = [str(item.text()) for item in self.listWidget.selectedItems()]
            #     print(imn)
            #     print(imn[5])
            #     #self.on_change()
            #     #self.on_change()

            def create_pdf2(self):
                # Set up a logo
                shost = self.lineEdit.text()
                shost2 = self.lineEdit_2.text()
                shost3 = self.lineEdit_3.text()

                conn = sqlite3.connect("db_member.db")
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT max(id) FROM member")
                rows = cur.fetchall()
                for row in rows:
                    row["max(id)"]

                cur2 = conn.cursor()
                cur2.execute("SELECT name_pk FROM print_dt")
                cur3 = conn.cursor()
                cur3.execute("SELECT address FROM print_dt")
                cur4 = conn.cursor()
                cur4.execute("SELECT dt_name FROM print_dt")
                cur5 = conn.cursor()
                cur5.execute("SELECT * FROM `member`")
                cur6 = conn.cursor()
                cur6.execute("SELECT name_pkadd FROM print_dtadd")

                rows6 = cur6.fetchall()
                rows5 = cur5.fetchall()
                rows4 = cur4.fetchall()
                rows3 = cur3.fetchall()
                rows2 = cur2.fetchall()

                for row5 in rows5:
                    row5[6]
                for row2 in rows2:
                    row2["name_pk"]

                for row3 in rows3:
                    row3["address"]

                for row4 in rows4:
                    row4["dt_name"]

                for row6 in rows6:
                    row6["name_pkadd"]

                t = row2["name_pk"]
                t1 = row3["address"]
                t2 = "BS: " + row4["dt_name"]
                t3 = row6["name_pkadd"]

                pdf = FPDF()
                pdf.set_font("Arial", size=12)
                pdf.add_page()

                pdf.image(t3, 8, 6, 25)
                pdf.add_font('DejaVu', '', 'DejaVuSerif-Italic.ttf', uni=True)
                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(35)
                pdf.cell(0, 5, t, ln=1)
                pdf.set_font('DejaVu', '', 14)

                pdf.cell(70)
                pdf.cell(0, 10, t2, ln=1)
                pdf.set_font('DejaVu', '', 14)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(30)

                pdf.cell(0, 0, "ĐC:", ln=1)
                pdf.set_font('DejaVu', '', 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(40)
                pdf.cell(0, 0, t1, ln=1)
                pdf.set_draw_color(0, 0, 0)
                pdf.set_line_width(1)
                pdf.line(30, 30, 180, 30)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(255, 0, 40)
                pdf.cell(35)
                pdf.cell(0, 5, ' ', ln=1)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(255, 0, 40)
                pdf.cell(35)
                pdf.cell(0, 15, 'PHIẾU KHÁM NỘI SOI TAI-MŨI-HỌNG', ln=1)

                pdf.set_font('DejaVu', '', 12)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(75)
                pdf.cell(0, 0, 'Số Phiếu : ' + str(row5[0]), ln=1)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.cell(5)
                pdf.cell(0, 0, 'Tên bệnh nhân : ' + str(row5[1]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Tuổi : ' + str(row5[4]), ln=1)
                pdf.cell(135)
                pdf.cell(0, 0, 'Giới tính : ' + str(row5[6]), ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)
                pdf.cell(5)
                pdf.cell(0, 0, 'Địa chỉ : ' + str(row5[3]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Số bảo hiểm : ' + str(row5[7]), ln=1)
                pdf.cell(135)
                pdf.cell(0, 0, 'Nghề nghiệp : ' + str(row5[2]), ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)
                pdf.cell(5)
                pdf.cell(0, 0, 'Triệu chứng : ' + str(row5[5]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Điện thoại: ' + str(row5[8]), ln=1)

                pdf.set_font('DejaVu', '', 14)
                pdf.cell(0, 15, ' ', ln=1)
                pdf.cell(70)
                pdf.cell(0, 0, 'HÌNH ẢNH NỘI SOI ', ln=1)
                #
                file_name = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh1)))
                file_name1 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh2)))
                file_name2 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh3)))
                file_name3 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh4)))
                file_name4 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh5)))
                file_name5 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh6)))
                #

                pdf.set_font('DejaVu', '', 16)
                pdf.cell(0, 130, ' ', ln=1)
                pdf.cell(60)
                pdf.cell(0, 0, 'MÔ TẢ KẾT QUẢ NỘI SOI ', ln=1)
                pdf.set_font('DejaVu', '', 12)
                pdf.cell(0, 5, ' ', ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Chẩn đoán : %s' % (shost), ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Điều trị : %s' % (shost2), ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Chỉ định bác sĩ : %s' % (shost3), ln=1)

                pdf.set_x(120)
                pdf.cell(0, 14, " Ngày " + str(today.day) + " Tháng " + str(today.month) + " Năm " + str(today.year),
                         ln=1)
                pdf.set_x(145)
                pdf.cell(0, 6, 'Bác sĩ : ', ln=1)
                pdf.cell(0, 15, ' ', ln=1)
                pdf.set_x(126)
                pdf.cell(0, 0, t2, ln=1)
                # if file_name == '' or file_name1 == True or file_name2 == True or file_name3 == True or file_name4 == True or file_name5 == True :
                if os.path.exists(file_name) and os.path.exists(file_name1) and os.path.exists(
                        file_name2) and os.path.exists(file_name3) and os.path.exists(file_name4) and os.path.exists(
                    file_name5):
                    pdf.image(file_name, 12, 90, 60)
                    pdf.image(file_name1, 12, 150, 60)
                    pdf.image(file_name2, 74, 90, 60)
                    pdf.image(file_name3, 74, 150, 60)
                    pdf.image(file_name4, 136, 90, 60)
                    pdf.image(file_name5, 136, 150, 60)
                # pdf.image(file_name, 12, 90, 60)
                # pdf.image(file_name1, 12, 150, 60)
                # pdf.image(file_name2, 74, 90, 60)
                # pdf.image(file_name3, 74, 150, 60)
                # pdf.image(file_name4, 136, 90, 60)
                # pdf.image(file_name5, 136, 150, 60)

                directory1 = "doccument/"
                if not os.path.exists(directory1):
                    os.makedirs(directory1)
                pdf.output('doccument/%s.pdf' % ("a" + str(row["max(id)"])))
                webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["max(id)"])))
                #                 pdf.output('doccument/%s.pdf' % ("a" + str(row["max(id)"])))
                #                 webbrowser.open_new(r'doccument\%s.pdf' % ("a" + str(row["max(id)"])))
                conn.commit()
                cur.close()

                # self.winc()

        class video(QtWidgets.QDialog, Ui_Form):

            def __init__(self):
                #                 root.overrideredirect(False)
                root.withdraw()
                super().__init__()
                self.value = 0  # ---
                self.value1 = 0
                self.value2 = 0
                self.valueh = 5
                self.valuem = 11
                self.valuea = 1
                self.setupUi(self)  # ++
                self.CAPTURE.clicked.connect(self.capture_image)
                self.NEXT_3.clicked.connect(self.window2)

                # # adding items to the combo box
                # self.available_cameras = QCameraInfo.availableCameras()
                self.camera_selector.addItem("  CAMERA USB3.0")
                # self.camera_selector.add Items([camera.description()
                #                                for camera in self.available_cameras])
                # self.camera_selector1.addItem("  Chụp Thủ Công ")
                # self.camera_selector1.addItem("  Chụp Tự Động")
                # self.camera_selector.currentIndexChanged.connect(self.select_camera)
                # self.camera_selector.stateChanged.connect(self.select_camera)

                self.NEXT_7.clicked.connect(self.w1)
                self.NEXT_3c.clicked.connect(self.cw1)
                self.imgLabel.setScaledContents(True)
                self.cap = None  # -capture <-> +cap
                self.timer = QtCore.QTimer(self, interval=5)
                self.timer.timeout.connect(self.update_frame)
                self._image_counter = 0
                self.start_webcam()
                self.saveTimer = QTimer()

                # self.listWidget.itemChanged.connect(self.call)
                # self.listWidget.itemSelectionChanged.connect(self.on_change)
                # self.item.clicked.connect(self.w1)
                # self.item.setCheckState(True)
                # self.TEXT.setText.setText("True" if self.item1.setCheckState() else "False")

            @QtCore.pyqtSlot()
            def start_webcam(self):
                if self.cap is None:
                    self.cap = cv2.VideoCapture(0)
                    # self.imgLabel.setText("No Single")
                self.timer.start()
                font = QFont('Times', 42)
                self.imgLabel.setFont(font)
                self.imgLabel.setText("No Single : Kiểm Tra Tín Hiệu !")

                # else:
                # self.imgLabel.setText("No Single")

            @QtCore.pyqtSlot()
            def update_frame(self):
                ret, image = self.cap.read()
                # Define the codec and create VideoWriter object
                # image = imutils.resize(image, width=320, height=256)
                # time.sleep(2.0)

                if ret == True:
                    # image =cv2.resize(image, (320, 256))
                    image = cv2.resize(image, (960, 540))
                    # image = cv2.flip(image, 1)
                    # frame1 = cv2.resize(image, (416, 416))
                    frame2 = cv2.resize(image, (200, 150))
                    # frame1 = imutils.resize(image, width=640, height=480)
                    # (H, W) = frame1.shape[:2]

                    if self.valuea == 2:
                        height, width, channels = image.shape
                        # Detecting objects
                        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
                        #  blob = cv2.dnn.blobFromImage(image, 0.00392, (320,224), (0, 0, 0), True, crop=False)
                        net.setInput(blob)
                        outs = net.forward(output_layers)
                        # Showing informations on the screen
                        class_ids = []
                        confidences = []
                        boxes = []
                        for out in outs:
                            for detection in out:
                                scores = detection[5:]
                                class_id = np.argmax(scores)
                                confidence = scores[class_id]
                                if confidence > 0.78:
                                    # Object detected
                                    center_x = int(detection[0] * width)
                                    center_y = int(detection[1] * height)
                                    w = int(detection[2] * width)
                                    h = int(detection[3] * height)
                                    # Rectangle coordinates
                                    x = int(center_x - w / 2)
                                    y = int(center_y - h / 2)
                                    boxes.append([x, y, w, h])
                                    confidences.append(float(confidence))
                                    class_ids.append(class_id)
                        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
                        for i in range(len(boxes)):
                            if i in indexes:
                                label = str(classes[class_ids[i]])
                                # cv2.putText(image, label , (20,20), font, 2,(255, 255, 255), 2)
                                # print(label)
                                # print(class_ids[i])
                                confidence = confidences[i]
                                # color = colors[class_ids[i]]
                                cv2.putText(image, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3,
                                            (255, 255, 255), 3)
                                # elapsed_time = time.time() - starting_time
                                # fps = frame_id / elapsed_time
                                # cv2.putText(image, "FPS: " + str(round(fps, 2)), (10, 50), font, 3, (0, 0, 255), 3)

                                if self.value < 6 and class_ids[i] == 0:
                                    self.value = self.value + 1
                                    conn = sqlite3.connect("db_member.db")
                                    conn.row_factory = sqlite3.Row
                                    cur = conn.cursor()
                                    cur.execute("SELECT max(id) FROM member")
                                    rows = cur.fetchall()
                                    directory = "anh/"
                                    if not os.path.exists(directory):
                                        os.makedirs(directory)
                                    for row in rows:
                                        row["max(id)"]
                                    cv2.imwrite('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value)),
                                                frame2)
                                    # self.TEXT.setText('your Image have been Saved')
                                    self.label = QLabel(self)

                                    self.it.setIcon(
                                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value))))
                                    self.it1.setIcon(
                                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value))))
                                    self.it2.setIcon(
                                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value))))
                                    self.it3.setIcon(
                                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value))))
                                    self.it4.setIcon(
                                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value))))
                                    self.it5.setIcon(
                                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value))))

                                    self.TEXT.setText('anh/%s.png' % (label) + str(self.value))

                                if self.valueh < 12 and class_ids[i] == 1:
                                    self.valueh = self.valueh + 1
                                    conn = sqlite3.connect("db_member.db")
                                    conn.row_factory = sqlite3.Row
                                    cur = conn.cursor()
                                    cur.execute("SELECT max(id) FROM member")
                                    rows = cur.fetchall()
                                    directory = "anh/"
                                    if not os.path.exists(directory):
                                        os.makedirs(directory)
                                    for row in rows:
                                        row["max(id)"]
                                    cv2.imwrite('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valueh)),
                                                frame2)
                                    # self.TEXT.setText('your Image have been Saved')
                                    self.label = QLabel(self)

                                    self.it6.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valueh))))
                                    self.it7.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valueh))))
                                    self.it8.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valueh))))
                                    self.it9.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valueh))))
                                    self.it10.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valueh))))
                                    self.it11.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valueh))))

                                    self.TEXT.setText('anh/%s.png' % (label) + str(str(self.valueh)))

                                if self.valuem < 18 and class_ids[i] == 2:
                                    self.valuem = self.valuem + 1
                                    conn = sqlite3.connect("db_member.db")
                                    conn.row_factory = sqlite3.Row
                                    cur = conn.cursor()
                                    cur.execute("SELECT max(id) FROM member")
                                    rows = cur.fetchall()
                                    directory = "anh/"
                                    if not os.path.exists(directory):
                                        os.makedirs(directory)
                                    for row in rows:
                                        row["max(id)"]
                                    cv2.imwrite('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valuem)),
                                                frame2)
                                    # self.TEXT.setText('your Image have been Saved')
                                    self.label = QLabel(self)

                                    self.it12.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valuem))))
                                    self.it13.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valuem))))
                                    self.it14.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valuem))))
                                    self.it15.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valuem))))
                                    self.it16.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valuem))))
                                    self.it17.setIcon(
                                        QtGui.QIcon(
                                            'anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.valuem))))

                                    self.TEXT.setText('anh/%s.png' % (label) + str(self.valuem))

                    self.displayImage(image, True)
                else:
                    self.cap.release()

            @QtCore.pyqtSlot()
            def capture_image(self):

                flag, frame = self.cap.read()

                if flag == True and self.value1 < 18:
                    frame = imutils.resize(frame, width=240, height=170)
                    self.value1 = self.value1 + 1
                    conn = sqlite3.connect("db_member.db")
                    conn.row_factory = sqlite3.Row
                    cur = conn.cursor()
                    cur.execute("SELECT max(id) FROM member")
                    rows = cur.fetchall()
                    directory = "anh/"
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    for row in rows:
                        row["max(id)"]
                    cv2.imwrite('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value1)), frame)
                    # self.TEXT.setText('your Image have been Saved')
                    self.label = QLabel(self)

                    self.it.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(1))))
                    self.it1.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(2))))
                    self.it2.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(3))))
                    self.it3.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(4))))
                    self.it4.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(5))))
                    self.it5.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(6))))
                    self.it6.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(7))))

                    self.it7.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(8))))
                    self.it8.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(9))))
                    self.it9.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(10))))
                    self.it10.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(11))))
                    self.it11.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(12))))
                    self.it12.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(13))))
                    self.it13.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(14))))
                    self.it14.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(15))))
                    self.it15.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(16))))
                    self.it16.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(17))))
                    self.it17.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(18))))
                    # self.TEXT.setText(str(row["max(id)"]) + label+ str(self.value))
                    self.TEXT.setText('anh/%s.png' % (self.value1))

                if flag == False:
                    font = QFont('Times', 42)
                    self.imgLabel.setFont(font)
                    self.imgLabel.setText("No Single : Kiểm Tra Tín Hiệu !")

                # else:
                # font = QFont('Times', 42)
                # self.imgLabel.setFont(font)
                # self.imgLabel.setText("No Single : Kiểm Tra Tín Hiệu !")

            def window2(self):  # <===
                self.w = Window2()
                self.w.show()
                # self.w1()

            def displayImage(self, img, window=True):
                qformat = QtGui.QImage.Format_Indexed8
                if len(img.shape) == 3:
                    if img.shape[2] == 4:
                        qformat = QtGui.QImage.Format_RGBA8888
                    else:
                        qformat = QtGui.QImage.Format_RGB888
                outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
                outImage = outImage.rgbSwapped()
                if window:
                    self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))

            def w1(self):
                window.close()
                self.cap.release()
                root.update()
                root.deiconify()

            def cw1(self):
                if self.valuea == 1:
                    self.NEXT_3c.setText("Chụp ảnh tự động")
                    self.valuea = 2
                else:
                    self.NEXT_3c.setText("Chụp ảnh thủ công")
                    self.valuea = 1

        window = video()
        window.setGeometry(0, 0, 1024, 570)
        #         window.overrideredirect(True)
        window.show()

        try:
            sys.exit(app.exec_())
        except:
            logic1 = 1


app = QApplication(sys.argv)
# # root.overrideredirect(True)root.overrideredirect(True)
# root.geometry("1024x600+0+0")
b = Application(root)
root.mainloop()


