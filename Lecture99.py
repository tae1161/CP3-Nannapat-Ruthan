from tkinter import *
import math


def leftClickButton(event):
    height = int(textBoxHeight.get())
    weight = int(textBoxWeight.get())
    BMI = round((weight / (math.pow(height / 100, 2))), 2)

    labelResult.configure(text=BMI)

    if BMI < 18.55:
        labelBMI.configure(text="อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม")
    elif BMI < 23:
        labelBMI.configure(text="อยู่ในเกณฑ์ปกติ")
    elif BMI < 25:
        labelBMI.configure(text="น้ำหนักเกิน")
    elif BMI < 30:
        labelBMI.configure(text="โรคอ้วนระดับที่ 1")
    else:
        labelBMI.configure(text="โรคอ้วนระดับที่ 2")


Mainwindow = Tk()
labelHeight = Label(Mainwindow, text="ส่วนสูง (Cm.)")
labelHeight.grid(row=0, column=0)

textBoxHeight = Entry(Mainwindow)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(Mainwindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)

textBoxWeight = Entry(Mainwindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(Mainwindow, text="คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)

labelResult = Label(Mainwindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)

labelBMI = Label(Mainwindow, text="เกณ")
labelBMI.grid(row=3, column=1)

Mainwindow.mainloop()