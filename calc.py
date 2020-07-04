from tkinter import *
window = Tk()
window.config(bg="#bfbdbb")
window.title("make math")
operator=""
text_Input=StringVar()

text_disp=Entry(window,font=('arial',20,"bold"),textvariable=text_Input,bd=30,insertwidth=4,
                bg="#bfbdbb",justify="right").grid(columnspan=4)
"""buttons adding """

btn7=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="7",bg="#3a69b5").grid(row=1,column=0)
btn8=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="8",bg="#3a69b5").grid(row=1,column=1)
btn9=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="9",bg="#3a69b5").grid(row=1,column=2)
clr=Button(window,padx=18,bd=8,fg="black",font=('arial',20,"bold"),
           text="c",bg="#3a69b5").grid(row=1,column=3)


btn4=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="4",bg="#3a69b5").grid(row=2,column=0)
btn5=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="5",bg="#3a69b5").grid(row=2,column=1)
btn6=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="6",bg="#3a69b5").grid(row=2,column=2)
mul=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="*",bg="#3a69b5").grid(row=2,column=3)


btn1=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="1",bg="#3a69b5").grid(row=3,column=0)
btn2=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="2",bg="#3a69b5").grid(row=3,column=1)
btn3=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="3",bg="#3a69b5").grid(row=3,column=2)
sub=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="-",bg="#3a69b5").grid(row=3,column=3)


btn0=Button(window,padx=20,bd=8,fg="black",font=('arial',20,"bold"),
           text="0",bg="#3a69b5").grid(row=4,column=0)
point=Button(window,padx=24,bd=8,fg="black",font=('arial',20,"bold"),
           text=".",bg="#3a69b5").grid(row=4,column=1)
div=Button(window,padx=24,bd=8,fg="black",font=('arial',20,"bold"),
           text="/",bg="#3a69b5").grid(row=4,column=2)
eql=Button(window,padx=17,bd=8,fg="#fcfbfa",font=('arial',20,"bold"),
           text="=",bg="#3a69b5").grid(row=4,column=3)


window.mainloop()