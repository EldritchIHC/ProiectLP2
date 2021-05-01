import psutil as pu
import cpuinfo
import GPUtil as gu
import numpy as np
import simpleaudio as sa
from datetime import datetime
'''
pentru requirments ,in terminal:
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt
'''
def warn():
    '''functie de avertizare sonora
    sursa
    https://realpython.com/playing-and-recording-sound-python/
    '''
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

def log(f):
    ''' scrie intr-un fisier cand apare o depasire a limitelor resurselor'''
    with open('log.txt','a',encoding='utf-8') as log:
        log.write("La data: "+str(datetime.today()) + '\n')
        log.write("Eroare:"+f+' \n'+' \n')

def get_size(bytes, suffix="B"):
    '''modifica valorile de la bytes la multiplii
    sursa:
    https://www.thepythoncode.com/article/get-hardware-system-information-python?fbclid=IwAR2nU2AbBgcl18qB4ak2XByfBMnlcuHEweU84uTHG0pW5dquQQnNJBP-wvM
    '''
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
        if(e>80):
            warn()
            log("S-a depasit limita de utilizare a nucleului "+ str(i))
            #string=string+ ("S-a depasit limita de utilizare a nucleului "+ str(i)+'\n')
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
    string = "Memorie totala: " + get_size(mem.total) + "\n" + "Memorie disponibila: " + get_size(mem.available) + "\n" + "Memorie utilizata: " + get_size(mem.used) + ' ' + str(mem.percent) + '%'
    if(mem.percent>90):
        warn()
        log("S-a depasit limita de utilizare a memoriei RAM!")
        string=string+"\nS-a depasit limita de utilizare a memoriei RAM!"
    return string

def disk():
    '''returneaza spatiile de stocare'''
    part=pu.disk_partitions()
    string=''
    try:
        for e in part:
            total=get_size(pu.disk_usage(str(e.device).replace("\\",'')).total)
            used=get_size(pu.disk_usage(str(e.device).replace("\\",'')).used)
            prc=pu.disk_usage(str(e.device).replace("\\",'')).percent
            if(prc>90):
                warn()
                log("Diskul:"+str(e.device).replace("\\",'')+' are spatiul ocupat:'+ str(prc)+'%')
            string=string+str(e.device).replace("\\",'')+' '+str(total)+' '+str(used)+' '+str(prc)+'% \n'
    except PermissionError:
        string=string+"Eroare de permisiune pentru diskul: "+str(e.device).replace("\\",'')
    return string

def gpu():
    '''returneaza brand gpu'''
    string=''
    i=0
    for e in gu.getGPUs():
        string = string + "GPU " + str(i) + ':' + str(e.name) + ' Memorie totala: '+str(get_size(int(e.memoryTotal)*(1024**2)))+' Memorie utilizata: '+str(get_size(int(e.memoryUsed)*(1024**2)))
    return string

def gpuld():
    '''returneaza utilizare gpu'''
    string =''
    i=0
    for e in gu.getGPUs():
        string = string + "GPU " + str(i) + ':' + str(e.load * 100) + '% '
        if(e.load*100>75):
            warn()
            log("S-a depasit limita de utilizare a GPU!")
            string=string+ "S-a depasit limita de utilizare a GPU!"
    return string

def gputemp():
    '''returneaza temp gpu'''
    string = ''
    i = 0
    for e in gu.getGPUs():
        if(e.temperature>80):
            warn()
            log("GPU"+str(i)+" s-a supraincalzit!")
        string=string+"Temperatura GPU "+str(i)+':'+str(e.temperature)+'C'
    return string


#print(cpu())
#print(cores())
#print(cpuld())
#print(memory())
#print(disk())
#print(gpu())
#print(gpuld())
#print(gputemp())

