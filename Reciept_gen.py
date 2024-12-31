from ttkbootstrap import ttk,Window
from random import randint
from datetime import datetime

win = Window(themename="darkly")
win.geometry("1200x700")
win.title("Gestion Restaurant")

style = ttk.Style()
style.configure('Custom.frame',bg="white")

def show():
    frame2.grid(row=0, column=1, padx=100)
    t = 50 * int(coo.get() or 0) + 70 * int(tag.get() or 0) + 80 * int(pas.get() or 0) + 40 * int(bri.get() or 0) + 25 * int(har.get() or 0) + 20 * int(caf.get() or 0)

    num.delete(0, "end")
    num.insert(0, randint(3000, 4000))

    date.delete(0, "end")
    date.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    cout.delete(0, "end")
    cout.insert(0, f"{t:.2f} DH")

    frais_value = t * 0.03
    frais.delete(0, "end")
    frais.insert(0, f"{frais_value:.2f} DH")

    tax_value = t * 0.3
    tax.delete(0, "end")
    tax.insert(0, f"{tax_value:.2f} DH")

    total_value = t + frais_value + tax_value
    total.delete(0, "end")
    total.insert(0, f"{total_value:.2f} DH")




def clear():
    frame2.grid_remove()
    coo.delete(0,'end')
    tag.delete(0,'end')
    pas.delete(0,'end')
    bri.delete(0,'end')
    har.delete(0,'end')
    caf.delete(0,'end')

frame1 = ttk.Frame()

ttk.Label(frame1,text="Couscous: 50DH",font=("Roboto",20)).grid(row=0,column=0,padx=5,pady=5,sticky='w')
coo = ttk.Entry(frame1,font=("Roboto",20),width=7)
coo.grid(row=0,column=1,padx=5,pady=5)

ttk.Label(frame1,text="Tajine: 70DH",font=("Roboto",20)).grid(row=1,column=0,padx=5,pady=5,sticky='w')
tag = ttk.Entry(frame1,font=("Roboto",20),width=7)
tag.grid(row=1,column=1,padx=5,pady=5)

ttk.Label(frame1,text="Pastilla: 80DH",font=("Roboto",20)).grid(row=2,padx=5,pady=5,sticky='w')
pas = ttk.Entry(frame1,font=("Roboto",20),width=7)
pas.grid(row=2,column=1,padx=5,pady=5)

ttk.Label(frame1,text="Briouates: 40DH",font=("Roboto",20)).grid(row=3,padx=5,pady=5,sticky='w')
bri = ttk.Entry(frame1,font=("Roboto",20),width=7)
bri.grid(row=3,column=1,padx=5,pady=5)

ttk.Label(frame1,text="Harira: 25DH",font=("Roboto",20)).grid(row=4,padx=5,pady=5,sticky='w')
har = ttk.Entry(frame1,font=("Roboto",20),width=7)
har.grid(row=4,column=1,padx=5,pady=5)

ttk.Label(frame1,text="Cafe: 20DH",font=("Roboto",20)).grid(row=5,padx=5,pady=5,sticky='w')
caf = ttk.Entry(frame1,font=("Roboto",20),width=7)
caf.grid(row=5,column=1,padx=5,pady=5)

ttk.Button(frame1,text="Generate Reciept",command=show).grid(row=6,sticky='e',padx=10,pady=10)
ttk.Button(frame1,text="Clear",command=clear).grid(row=6,column=1,sticky='w',padx=10,pady=10)

frame1.grid(row=0)

frame2 = ttk.Frame()

ttk.Label(frame2,text="Num de Factur: ",font=("Roboto",20)).grid(row=0,column=0,padx=5,pady=5)
num = ttk.Entry(frame2,font=("Roboto",20),width=20)
num.grid(row=0,column=1,padx=5,pady=5)

ttk.Label(frame2,text="Date: ",font=("Roboto",20)).grid(row=1,column=0,padx=5,pady=5)
date = ttk.Entry(frame2,font=("Roboto",20),width=20)
date.grid(row=1,column=1,padx=5,pady=5)

ttk.Label(frame2,text="Cout: ",font=("Roboto",20)).grid(row=2,padx=5,pady=5)
cout = ttk.Entry(frame2,font=("Roboto",20),width=20)
cout.grid(row=2,column=1,padx=5,pady=5)

ttk.Label(frame2,text="Frais de Service: ",font=("Roboto",20)).grid(row=3,padx=5,pady=5)
frais = ttk.Entry(frame2,font=("Roboto",20),width=20)
frais.grid(row=3,column=1,padx=5,pady=5)

ttk.Label(frame2,text="Taxe: ",font=("Roboto",20)).grid(row=4,padx=5,pady=5)
tax = ttk.Entry(frame2,font=("Roboto",20),width=20)
tax.grid(row=4,column=1,padx=5,pady=5)

ttk.Label(frame2,text="Total: ",font=("Roboto",20)).grid(row=5,padx=5,pady=5)
total = ttk.Entry(frame2,font=("Roboto",20),width=20)
total.grid(row=5,column=1,padx=5,pady=5)






win.mainloop()