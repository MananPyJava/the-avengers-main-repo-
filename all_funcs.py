from tkinter import *
import wikipedia
import pandas as pd

a=0
d=0
root=''
entry1=''
l1=''
b=''
l2=''
searched=''

def wikisearch():
    global a,entry1, l1, b
    a+=1
    if a==1:
        l1['text']="Enter Term You Want To Search and press button below: "
        entry1 = Entry(root,width=20)
        entry1.pack(anchor='center')
        b=Button(text='Search', command=search)
        b.pack(anchor='center')

def search():
    global entry1, l2, b, searched, root
    query=entry1.get()
    results = wikipedia.summary(query+' according to', sentences=2)
    l2=Label(root, wraplength=600)
    l2['text']=results
    l2.place(x=root.winfo_screenwidth()/2, y=75, anchor='center')

def Physics():
    global a, l1, b
    a=0
    l1['text']="""Some of the most used Formulae in Physics are:
                  1)Speed=Distance/Time
                  2)Acceleration=(Final Velocity-Initial Velocity)/Time
                  3)Density=Mass/Volume
                  4)Force=Mass x Acceleration
                  5)Power=Work Done/Time
                  6)Weight=Mass x Gravity
                  7)Pressure=Force/Area
                  8)Kinetic Energy=0.5 x Mass x Velocity x Velocity
                  9)Voltage(in volts)=Electric current flowing through the conductor in amperes x The resistance of the material in ohms
                  10)Frequency of a wave=Velocity or wave speed x The wavelength of the wave
               """
    try:
        entry1.destroy()
    except:
        pass
    try:
        b.destroy()
    except:
        pass
def Chem():
    global a, b, l1, entry1, l2
    a=1 #change to 1 when making label
    data=pd.read_csv('chem_data.csv')
    

def main():
    global a, l1, entry1, b, root
    a=0
    root = Tk()
    root.title("Student Assistant")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure()
    #photo=PhotoImage(file='photo.png')
    l1=Label(root)
    l1.place(x=root.winfo_screenwidth()/5, y=0)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="Search Wikipedia", command=wikisearch)
    FileMenu.add_command(label="Physics", command = Physics)
    FileMenu.add_command(label = "Chemistry", command = Chem)
    MenuBar.add_cascade(label = "Subjects", menu=FileMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Our Teacher-'Tech With Tim'", command=lambda: print())
    MenuBar.add_cascade(label="Our Inspiration", menu=HelpMenu)
    setup=Menu(MenuBar,tearoff=0)
    root.config(menu=MenuBar)
    root.mainloop()

if __name__=="__main__":
    main()