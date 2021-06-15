#!/usr/bin/env python
# coding: utf-8

# In[ ]:


--教材10--海龜繪圖--

Homework #1 
請使用海龜繪圖繪製六角星星。


# In[92]:


import turtle

turtle.clearscreen()
t = turtle.Pen()

for x in range(1, 7): #六邊形
    t.forward(100)      # 繪線移動100
    t.left(60)          # 左轉60度 六邊形內角60度
    for x in range(1,4): #三角形
        t.forward(100) # 繪線移動100
        t.left(-120)  #向外轉120所以是-120


# In[ ]:


--教材10--海龜繪圖--

Homework #2 
請使用海龜繪圖設計紅綠燈動畫，三顆燈輪流亮起，各亮10秒，循環三次。


# In[2]:


import turtle
import time

turtle.clearscreen()
t = turtle.Pen()
colorsList = ['red','yellow','green']

t.circle(50) #第一個圈

t.penup()
t.forward(-100)
t.pendown()

t.circle(50)  #第二個圈

t.penup()
t.forward(-100)
t.pendown()

t.circle(50)  #第三個圈  

for i in range(0,3):
    for i in range(0,3):
        t.fillcolor(colorsList[i%3])    
        t.begin_fill() 
        
        t.circle(50)  
        t.penup()
        t.forward(100)
        t.pendown()
        
        t.end_fill()
        time.sleep(10) 
    for i in range(0,3):
        t.fillcolor('white')
        t.begin_fill()
    
        t.penup()
        t.forward(-100)
        t.pendown()
        t.circle(50)
        t.end_fill()


# --教材11--
# Homework #1 請設計一個 BMI 計算程式。

# In[11]:


from tkinter import * #導入模組


def count(): 
    tall = round((m.get()**2), 2)
    bmii=kg.get()/tall
    bmiii=round(bmii,2)
    bmi.set(bmiii)
    
    if bmi.get()< 18.5:
        str1.set("你的bmi值為:%.5s,太瘦囉!" % bmi.get())
    elif bmi.get()>=18.5 and bmi.get()<24 :
        str1.set("你的bmi值為:%.5s,正常範圍!" % bmi.get())
    else:
        str1.set("你的bmi值為:%.5s,異常範圍!" % bmi.get())
      
    



window = Tk() #自行定義TK物件名稱
window.title("BMI計算器")   #視窗標題                  
window.geometry("400x300") #視窗大小



m = DoubleVar()   #小數
kg = DoubleVar()  #小數
bmi = DoubleVar() #小數
str1 = StringVar() #字串

lab1 = Label(window,text="BMI計算器",font='8')  #標籤BMI計算器

lab2 = Label(window,text="身高(m)") #身高標籤
e1 = Entry(window,width=8,textvariable=m) #文字方塊1#身高輸入格

lab3 = Label(window,text="體重(kg)") #體重標籤
e2 = Entry(window,width=8,textvariable=kg)   #文字方塊2#體重輸入格

btn1 = Button(window,text="開始計算",command=count) #開始計算按鈕 command連結到count()
lab4 = Label(window,text="BMI值為") #BMI值標籤
e3 = Entry(window,textvariable=bmi)  #文字方塊3 #BMI值顯示格
e4 = Entry(window,width=30,textvariable=str1)  #文字方塊4 #文字內容顯示格
              
btn2 = Button(window,text="Exit",width=10,command=window.destroy) #離開按鈕


#定位按鈕
lab1.grid(row=0,column=1) 
lab2.grid(row=2,column=0)
e1.grid(row=2,column=1)           

lab3.grid(row=3,column=0)
e2.grid(row=3,column=1)   
btn1.grid(row=4,column=1)
lab4.grid(row=5,column=0)
e3.grid(row=5,column=1)                     
e4.grid(row=8,column=1)
btn2.grid(row=9,column=4)

#column直的｜ # row衡的 — 

window.mainloop()


# --教材11--
# Homework #2 請設計一個計算機程式。

# In[23]:


from tkinter import *
    
window = Tk() 
window.title("計算機")

def updateDisplay(buttonString): #更新display函式
    content = display.get() 
    if content == "0":  #開始輸入時如果是0則不顯示
        content = "" 
    display.set(content+buttonString) #buttonString加入新按鈕字串
def calculate(): #計算函式
    result = eval(display.get()) 
    display.set(display.get() + '=' + str(result)) 
    
def pa(): #轉成百分率函式
    result=eval(display.get())/100
    print(result)
    display.set(float(result))

def clear(): #清除歸零函式
    display.set('0') 
    
def backspace(): #清除後一位函式
    display.set(str(display.get()[:-1])) #取到-1前一位
    


display = StringVar() #設定顯示變數
display.set('0') #設定一開始為0

textLabel = Label(window)  #建立計算機顯示欄位
textLabel.config(bg='white', width=28, height=2,fg='black') 
#底色白色 高度28 寬度2,字體顏色黑色
textLabel['textvariable']= display  #display指定到textLabel['textvariable']文字變數


#利用lambda函式計算
btn1 = Button(window,width=5,text='1',command = lambda:updateDisplay('1'))   # 按鈕1#連結到lambda函式
btn2 = Button(window,width=5,text='2',command = lambda:updateDisplay('2'))   # 按鈕2#連結到lambda函式
btn3 = Button(window,width=5,text='3',command = lambda:updateDisplay('3'))   # 按鈕3#連結到lambda函式
btn4 = Button(window,width=5,text='4',command = lambda:updateDisplay('4'))   # 按鈕4#連結到lambda函式
btn5 = Button(window,width=5,text='5',command = lambda:updateDisplay('5'))   # 按鈕5#連結到lambda函式
btn6 = Button(window,width=5,text='6',command = lambda:updateDisplay('6'))   # 按鈕6#連結到lambda函式
btn7 = Button(window,width=5,text='7',command = lambda:updateDisplay('7'))   # 按鈕7#連結到lambda函式
btn8 = Button(window,width=5,text='8',command = lambda:updateDisplay('8'))   # 按鈕8#連結到lambda函式
btn9 = Button(window,width=5,text='9',command = lambda:updateDisplay('9'))   # 按鈕9#連結到lambda函式


btnc = Button(window,width=5,text='C',command =clear) #連結到清除函式 clear()
btndel = Button(window,width=5,text='DEL',command =backspace) #連結到 backspace()函式
btnper = Button(window,width=5,text='%',command = pa)  # 按鈕 % #連結到pa函式 #換成取百分比值
 btndiv = Button(window,width=5,text='/',command = lambda:updateDisplay('/'))  # 按鈕 / #連結到lambda函式
btnmul = Button(window,width=5,text='*',command = lambda:updateDisplay('*'))  # 按鈕 * #連結到lambda函式
btnsub = Button(window,width=5,text='-',command = lambda:updateDisplay('-'))  # 按鈕 - #連結到lambda函式
btnadd = Button(window,width=5,text='+',command = lambda:updateDisplay('+'))  # 按鈕 + #連結到lambda函式
btnequ = Button(window,width=5,text='=',bg='orange',command = calculate)      # 按鈕 = #連結到lambda函式
btnzero = Button(window,width=12,text='0',command = lambda:updateDisplay('0'))# 按鈕 0 #連結到lambda函式
btndot = Button(window,width=5,text='.',command = lambda:updateDisplay('.'))  # 按鈕 . #連結到lambda函式

#定位
textLabel.grid(row=0,column=0,columnspan=4)
btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnadd.grid(row=4,column=3)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btnsub.grid(row=3,column=3)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btnmul.grid(row=2,column=3)

btnc.grid(row=1,column=0)
btndel.grid(row=1,column=1)
btnper.grid(row=1,column=2)
btndiv.grid(row=1,column=3)

btnzero.grid(row=5,columnspan=2)
btndot.grid(row=5,column=2)
btnequ.grid(row=5,column=3)

window.mainloop()


# --教材11--
# Homework #3 請設計一個貸款計算程式，請使用 tkinter 設計此程式。
# 這個程式的每月支付金額與總支付金額使用淺黃色為背景，
# 我們可以輸入利率、貸款年數、貸款金額然後計算每月支付金額與總支付金額，更多細節可以參考下列執行結果。

# In[16]:


from tkinter import *
 
    

def totall():
    rate.set((rate.get()/100)/12) #年利率 /100 變小數在/12
    rate.set(round(rate.get(),4)) #小數進位取前4位

    
    year.set(year.get()*12) #年分*12變月份
    year.set(year.get())

    
    #以下開始房貸計算
    monthly.set((1+rate.get()))
    monthly.set(round(monthly.get(),4))

    monthly.set( (monthly.get()) **(year.get()))

    monthly.set((monthly.get()*rate.get())/(monthly.get()-1))
    monthly.set(round(monthly.get(),4))

    monthly.set(monthly.get()*money.get())
    monthly.set(int(monthly.get()))
    
    total.set(monthly.get()*year.get())
    total.set(int(total.get()))

    
window = Tk() 
window.title("房貸利率計算器")
window.geometry("400x200")

rate=DoubleVar() #利率
year=IntVar() #貸款年數
money=IntVar() #總額
monthly=DoubleVar() #每個月支付
total=DoubleVar() #總支付金額

lab1 = Label(window,text="房貸利率計算器") 

lab2 = Label(window,text="利率") 
e1 = Entry(window,width=15,textvariable=rate)

lab3 = Label(window,text="貸款總年數")
e2 = Entry(window,width=15,textvariable=year)

lab4=Label(window,text="貸款金額")
e3 = Entry(window,width=15,textvariable=money)

lab5=Label(window,text="每月支付金額")
e4 = Entry(window,width=15,textvariable=monthly,bg='#FFFFCD')
lab6=Label(window,text="總支付金額")
e5 = Entry(window,width=15,textvariable=total,bg='#FFFFCD')
btn1 = Button(window,width=10,text='計算',command=totall)


lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
e1.grid(row=1,column=1)
lab3.grid(row=2,column=0)
e2.grid(row=2,column=1)
lab4.grid(row=3,column=0)
e3.grid(row=3,column=1)
lab5.grid(row=4,column=0)
e4.grid(row=4,column=1)
lab6.grid(row=5,column=0)
e5.grid(row=5,column=1)
btn1.grid(row=9,column=1,rowspan=3)


window.mainloop()

