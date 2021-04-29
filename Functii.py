import psutil as pu
import cpuinfo
import GPUtil as gu
import numpy as np
import simpleaudio as sa
import platform
#import os
#import cpuutilization
#print(platform.processor())
#pu.sensors_temperatures(False)
#print("d:{d}".format(d=pu.disk_usage("D:")[3]))
#print(pu.sensors_fans())
#print(pu.virtual_memory())
#while(True):
 #   print("cpu:{cpu}".format(cpu=pu.cpu_percent(interval=1)))


def warn():
    '''functie de averizare sonora'''
    f = 660  #nota
    fs = 44100  #samples
    s = 1  #secunde
    t = np.linspace(0, s, s * fs, False)
    note = np.sin(f * t * 2 * np.pi)
    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    for i in range(0,3):#3 semnale
        play_obj = sa.play_buffer(audio, 1, 2, fs)
        sa.sleep(2)
    play_obj.wait_done()


def get_size(bytes, suffix="B"):
    '''modifica valorile de la bytes la multiplii'''
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def cpu():
    '''returneaza brand procesor'''
    return cpuinfo.get_cpu_info()['brand_raw']

def cpuld():
    '''returneaza utilizare cpu'''
    list=pu.cpu_percent(interval=1,percpu=True)
    string=''
    i=0
    for e in list:
        if(e>75):
            warn()
            return ("S-a depasit limita de utilizare a nucleului "+ str(i))
        i = i + 1
        string=string+"Nucleul "+str(i)+":"+ str(e)+"% "
    return string

def cores():
    '''returneza nr nuclee +nr threads'''
    cores='Nuclee fizice: '+ str(pu.cpu_count(False))+" Nuclee logice: "+str(pu.cpu_count(True))
    return cores

def memory():
    '''retuneaza memoria ram instalata'''
    mem=pu.virtual_memory()
    memory="Memorie totala:"+get_size(mem.total)+" Memorie disponibila: "+get_size(mem.available)+" Memorie utilizata: "+get_size(mem.used)
    return memory

def disk():
    '''returneaza spatiile de stocare'''
    part=pu.disk_partitions()
    try:
        for e in part:
            total=get_size(pu.disk_usage(str(e.device).replace("\\",'')).total)
            used=get_size(pu.disk_usage(str(e.device).replace("\\",'')).used)
            prc=pu.disk_usage(str(e.device).replace("\\",'')).percent
            print(str(e.device).replace("\\",'')+str(total)+str(used)+str(prc))
    except PermissionError:
        print("Eroare de permisiune pentru diskul: "+str(e.device).replace("\\",'') )

def gpu():
    for e in gu.getGPUs():
        print(e.name)
        print(e.temperature)
        print(e.memoryTotal)
        print(e.memoryUsed)
        print(e.load*100)

def gpuld():
    string =''
    i=0
    for e in gu.getGPUs():
        if(e.load*100>75):
            warn()
            return ("S-a depasit limita de utilizare a GPU!")
    string=string+"GPU "+str(i)+':'+str(e.load*100)+'% '
    return string




print(cpu())
print(cores())
print(cpuld())
print(memory())
disk()
gpu()
print(gpuld())
