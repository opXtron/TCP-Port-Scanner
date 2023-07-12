import socket,sys,threading,time
from tkinter import *
ip_s=1
ip_f=1024
ports=[]
log=[]
target='localhost'

def scanport(target,port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
        s.settimeout(4)
        c=s.connect_ex((target,port))  
        if c==0:  
            m="Port %d \t[open]"%(port,)  
            ports.append(port)
            listbox.insert("end",str(m))  
            updateResult()   
        s.close() 

    except OSError:
        print('>too many open sockets port'+str(port))
    except:
        c.close()
        s.close() 
        sys.exit() 
    sys.exit()

def  updateResult(): 
    rtext="["+str(len(ports))+'/'+str(ip_f)+"] ~"+str(target)
    L27.configure(text=rtext)

def startscan():
    global ports,log,target,ip_f
    clearscan()
    ports=[]
    ip_s=int(L24.get())
    ip_f=int(L25.get())
    log.append('>port Scanner')
    log.append('='*14+'\n')
    log.append('Target:\t'+str(target))

    try:
        target=socket.gethostbyname(str(L22.get()))
        log.append("Ip Adr:\t"+str(target))
        log.append('ports:\t['+ str(ip_s)+'/'+str(ip_f)+']')
        log.append('\n')
        while ip_s<=ip_f:
            try:
                scan=threading.Thread(target=scanport,args=(target,ip_s))
                scan.setDaemon(True)
                scan.start()
            except:time.sleep(0.01)
            ip_s+=1

    except:
        m='>Target'+str(L22.get())+'not found'
        log.append(m)
        listbox.insert(0,str(m))
    for i in range(len(log)):
        print(log[i])
        print()

def clearscan():
    listbox.delete(0,'end')



gui=Tk()
gui.title('port scanner')
gui.geometry('400x600+20+20')

gui.tk_setPalette(background='black',foreground='red',activeBackgrounk='#111111',activeForeground='#222222',highlightColor='#00ee00',highlightBackground='#00ee00')

L11=Label(gui,text="Port Scanner",font=("Helvetica",16,'underline'))
L11.place(x=16,y=10)

L21=Label(gui,text="Target")
L21.place(x=16,y=90)

L22=Entry(gui,text="Localhost")
L22.place(x=180,y=90)
L22.insert(0,"Localhost")

L23=Label(gui,text='Ports')
L23.place(x=16,y=158)

L24=Entry(gui,text='1')
L24.place(x=180,y=158,width=95)
L24.insert(0,'1')

L25=Entry(gui,text='1024')
L25.place(x=290,y=158,width=95)
L25.insert(0,"1024")

L26=Label(gui,text="Results")
L26.place(x=16,y=220)

L27=Label(gui,text="[...]")
L27.place(x=180,y=220)

frame=Frame(gui)
frame.place(x=16,y=275,width=370,height=215)
listbox=Listbox(frame,width=59,height=13)
listbox.place(x=0,y=0)
listbox.bind('<<listbox select')
scrollbar=Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

B11=Button(gui,text="start Scan",command=startscan)
B11.place(x=16,y=500,width=170)
gui.mainloop()