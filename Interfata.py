from time import sleep
import Functii as func
import tkinter as tk
import os
import re

def openlog():
    '''decshide fisierul log'''
    try:
        os.startfile('log.txt')
    except FileNotFoundError:
        return 0


def getprocent(string):
    '''caut in string  caractere intre : si %,le convertesc la float si  returneaza val max'''
    lista=re.findall(':[0-9\.-]+%',string)
    i=0
    for e in lista:
        e=float(e.strip(":%"))
        lista[i]=e
        i+=1
    return max(lista)

def labelcolor(prc):
    '''schimb culoarea textului daca depasesc un procent'''
    if(prc>80):
        return "red"
    if(prc>50):
        return "orange"
    else:
        return "black"


window=tk.Tk()
window.title("Proiect LP 2")
canvas=tk.Canvas(window,height=800,width=800,bg="white")
canvas.grid()

frame1=tk.Frame(canvas,bg="white",height=800,width=800,padx=10,pady=10,borderwidth = 2)
frame1.grid(row=0,column=0)
lt1=tk.Label(frame1,text="Specificatii statie",bg="white", anchor="e",justify="center")
lt1.grid(row=0,column=0,sticky='N')
lcpu=tk.Label(frame1,text=func.cpu(),bg="white", anchor="e",justify="left")
lcpu.grid(row=1,column=0,sticky='W')
lcores=tk.Label(frame1,text=func.cores(),bg="white", anchor="e",justify="left")
lcores.grid(row=2,column=0,sticky='W')
lmemory=tk.Label(frame1,text=func.memory(),bg="white", anchor="e",justify="left")
lmemory.grid(row=3,column=0,sticky='W')
ldisk=tk.Label(frame1,text=func.disk(),bg="white", anchor="e",justify="left")
ldisk.grid(row=4,column=0,sticky='W')
lgpu=tk.Label(frame1,text=func.gpu(),bg="white", anchor="e",justify="left")
lgpu.grid(row=5,column=0,sticky='W')

frame2=tk.Frame(canvas,bg="white",height=800,width=800,padx=10,pady=10,borderwidth = 2)
frame2.grid(row=0,column=1)
#frame2.columnconfigure(0, weight=1)
#frame2.columnconfigure(0, weight=3)
lt2=tk.Label(frame2,text="Monitor resurse",bg="white", anchor="e",justify="center")
lt2.grid(row=0,column=0,sticky='N')

'''cpuldbar=ttk.Progressbar(frame2,orient="vertical",length=100)
cpuldbar.grid(row=1,column=0,sticky='W')

gpuldbar=ttk.Progressbar(frame2,orient="vertical",length=100)
gpuldbar.grid(row=1,column=1,sticky='W')

memldbar=ttk.Progressbar(frame2,orient="vertical",length=100)
memldbar.grid(row=1,column=2,sticky='W')
'''

cpuldval=tk.StringVar()
cpuldval.set(func.cpuld())
memldval=tk.StringVar()
memldval.set(func.memoryld())
gpuldval=tk.StringVar()
gpuldval.set(func.gpuld())
gputempval=tk.StringVar()
gputempval.set(func.gputemp())

lcpuld=tk.Label(frame2,textvariable=cpuldval,bg="white", anchor="e",justify="left")
lcpuld.grid(row=1,column=0,sticky='W')

lmemld=tk.Label(frame2,textvariable=memldval,bg="white", anchor="e",justify="left")
lmemld.grid(row=2,column=0,sticky='W')

lgpuld=tk.Label(frame2,textvariable=gpuldval,bg="white", anchor="e",justify="left")
lgpuld.grid(row=3,column=0,sticky='W')
tk.Label()
lgputemp=tk.Label(frame2,textvariable=gputempval,bg="white", anchor="e",justify="left")
lgputemp.grid(row=4,column=0,sticky='W')

b1=tk.Button(frame2,text="Deschide fisier log",command=lambda:openlog())
b1.grid(row=5,column=0)

def update():
    while(True):
        cpuldval.set(func.cpuld())
        lcpuld.config(fg=labelcolor(getprocent(func.cpuld())))
        memldval.set(func.memoryld())
        lmemld.config(fg=labelcolor(getprocent(func.memoryld())))
        gpuldval.set(func.gpuld())
        lgpuld.config(fg=labelcolor(getprocent(func.gpuld())))
        gputempval.set(func.gputemp())
        window.update()

window.after(5000, update())

window.mainloop()