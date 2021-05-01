import Functii as func
import tkinter as tk
from tkinter import ttk

import os

'''
os.startfile('log.txt')
'''
window=tk.Tk()
window.title("Proiect LP 2")
canvas=tk.Canvas(window,height=800,width=800,bg="black")
canvas.grid()

frame1=tk.Frame(canvas,bg="red",height=800,width=800,padx=10,pady=10,borderwidth = 2)
frame1.grid(row=0,column=0)
lcpu=tk.Label(frame1,text=func.cpu(),bg="red", anchor="e",justify="left")
lcpu.grid(row=0,column=0,sticky='W')
lcores=tk.Label(frame1,text=func.cores(),bg="red", anchor="e",justify="left")
lcores.grid(row=1,column=0,sticky='W')
lmemory=tk.Label(frame1,text=func.memory(),bg="red", anchor="e",justify="left")
lmemory.grid(row=2,column=0,sticky='W')
ldisk=tk.Label(frame1,text=func.disk(),bg="red", anchor="e",justify="left")
ldisk.grid(row=3,column=0,sticky='W')
lgpu=tk.Label(frame1,text=func.gpu(),bg="red", anchor="e",justify="left")
lgpu.grid(row=4,column=0,sticky='W')

frame2=tk.Frame(canvas,bg="red",height=800,width=800,padx=10,pady=10,borderwidth = 2)
frame2.grid(row=0,column=1)
#frame2.columnconfigure(0, weight=1)
#frame2.columnconfigure(0, weight=3)
l=tk.Label(frame2,text="Monitor resurse",bg="red", anchor="e",justify="center")
l.grid(row=0,column=0)

'''cpuldbar=ttk.Progressbar(frame2,orient="vertical",length=100)
cpuldbar.grid(row=1,column=0,sticky='W')

gpuldbar=ttk.Progressbar(frame2,orient="vertical",length=100)
gpuldbar.grid(row=1,column=1,sticky='W')

memldbar=ttk.Progressbar(frame2,orient="vertical",length=100)
memldbar.grid(row=1,column=2,sticky='W')
'''

lcpuld=tk.Label(frame2,text=func.cpuld(),bg="red", anchor="e",justify="left")
lcpuld.grid(row=1,column=0,sticky='W')

lgpuld=tk.Label(frame2,text=func.gpuld(),bg="red", anchor="e",justify="left")
lgpuld.grid(row=2,column=0,sticky='W')

lgputemp=tk.Label(frame2,text=func.gputemp(),bg="red", anchor="e",justify="left")
lgputemp.grid(row=3,column=0,sticky='W')

b1=tk.Button(frame2,text="Deschide fisier log")
b1.grid(row=4,column=0)

window.mainloop()