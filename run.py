from tkinter import *

root = Tk()
dieshu = ""
dieshu2 = ""
root.title("计算器")

root.resizable(width=False, height=False)
lbl = Label(root, text="")
lbl.place(x=0, y=0, anchor=NW)
fuhao = ""
dian1=""

# 数字函数
def one():
    global dieshu
    global fuhao
    dieshu += "1"
    lbl.configure(text=dieshu)


def two():
    global dieshu
    global fuhao
    dieshu += "2"
    lbl.configure(text=dieshu)


def there():
    global dieshu
    global fuhao
    dieshu += "3"
    lbl.configure(text=dieshu)


def four():
    global dieshu
    global fuhao
    dieshu += "4"
    lbl.configure(text=dieshu)


def five():
    global dieshu
    global fuhao
    dieshu += "5"
    lbl.configure(text=dieshu)


def six():
    global dieshu
    global fuhao
    dieshu += "6"
    lbl.configure(text=dieshu)


def seven():
    global dieshu
    global fuhao
    dieshu += "7"
    lbl.configure(text=dieshu)


def eight():
    global dieshu
    global fuhao
    dieshu += "8"
    lbl.configure(text=dieshu)


def nine():
    global dieshu
    global fuhao
    dieshu += "9"
    lbl.configure(text=dieshu)
def lin():
    global dieshu
    global fuhao
    dieshu += "0"
    lbl.configure(text=dieshu)
# 符号函数
def jia():
    global fuhao
    global dieshu
    global dieshu2
    fuhao = "+"
    dieshu2 = dieshu
    dieshu = ""
    lbl.configure(text="")




def jian():
    global fuhao
    global dieshu
    global dieshu2
    fuhao = "-"
    lbl.configure(text="")
    dieshu2 = dieshu
    dieshu = ""


def chu():
    global fuhao
    global dieshu
    global dieshu2
    fuhao = "/"
    lbl.configure(text="")
    dieshu2 = dieshu
    dieshu = ""

def cheng():
    global fuhao
    global dieshu
    global dieshu2
    fuhao = "*"
    lbl.configure(text="")
    dieshu2 = dieshu
    dieshu = ""

def AC():
    global fuhao
    global dieshu
    global dieshu2
    fuhao=""
    dieshu=""
    dieshu2=""
    lbl.configure(text="")
def dian():
    global dieshu
    global fuhao
    global dian1
    dieshu += "."
    dian1=1
    lbl.configure(text=dieshu)
def deng():
    global fuhao
    global dieshu
    global dieshu2
    global dian1
    if dian1 == 1:
        dieshu=float(dieshu)
        dieshu2=float(dieshu2)
    if fuhao == "+":
        dieshu = str(dieshu2 + dieshu)
        lbl.configure(text=dieshu)


    if fuhao == "-":
        dieshu = str(dieshu2 - dieshu)
        lbl.configure(text=dieshu)


    if fuhao == "*":
        dieshu = str(dieshu2 * dieshu)
        lbl.configure(text=dieshu)


    if fuhao == "/":
        dieshu = str(dieshu2 / dieshu)
        lbl.configure(text=dieshu)


    if fuhao == "":
        dieshu = dieshu2
        lbl.configure(text=dieshu)


    fuhao = ""


one = Button(root, text='1', command=one)
one.place(x=0, y=50, anchor=NW)
two = Button(root, text='2', command=two)
two.place(x=20, y=50, anchor=NW)
there = Button(root, text='3', command=there)
there.place(x=40, y=50, anchor=NW)
four = Button(root, text='4', command=four)
four.place(x=0, y=80, anchor=NW)
five = Button(root, text='5', command=five)
five.place(x=20, y=80, anchor=NW)
six = Button(root, text='6', command=six)
six.place(x=40, y=80, anchor=NW)
seven = Button(root, text='7', command=seven)
seven.place(x=0, y=110, anchor=NW)
eight = Button(root, text='8', command=eight)
eight.place(x=20, y=110, anchor=NW)
nine = Button(root, text='9', command=nine)
nine.place(x=40, y=110, anchor=NW)
lin = Button(root, text='0', command=lin)
lin.place(x=20, y=140, anchor=NW)
cheng = Button(root, text='X', command=cheng)
cheng.place(x=90, y=80, anchor=NW)
jia = Button(root, text='+', command=jia)
jia.place(x=90, y=110, anchor=NW)
jian = Button(root, text='-', command=jian)
jian.place(x=90, y=50, anchor=NW)
chu = Button(root, text='/', command=chu)
chu.place(x=110, y=50, anchor=NW)
deng = Button(root, text='=', command=deng)
deng.place(x=110, y=80, anchor=NW)
dian = Button(root, text='.', command=dian)
dian.place(x=40, y=140, anchor=NW)
AC = Button(root, text='AC', command=AC)
AC.place(x=110, y=110, anchor=NW)

root.mainloop()
