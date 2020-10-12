import language_check
import wikipedia
from tkinter import *
import pyttsx3
from spellchecker import SpellChecker
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
spell=SpellChecker()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
a=0
d=0


def Bio():
    global a,entry1
    a+=1

    if a==1:
        l2=Label(text="Enter Term You Want To Search and press button below: ",bg='black',fg='white')
        l2.pack()
        print('Bio')
        entry1 = Entry(root,width=200,bg='black',fg='white')
        entry1.pack()
        b=Button(text='Search', command=biosearch, bg='black',fg='white')
        b.pack(anchor='center')

def biosearch():
    global entry1
    query=entry1.get()
    results = wikipedia.summary(query+" according to", sentences=2)
    l3=Label(root,text=results,wraplength=500,bg='black',fg='white')
    l3.pack()
    print(results)
    speak(results)

def Eng():
    global d
    d+=1
    if d==1:
        l4=Label(text="Enter Sentence It will show your grammatical mistakes : ",bg='black',fg='white')
        l4.pack()
        entry2=Entry(root,width=200,bg='black',fg='white')
        entry2.pack()
        c = Button(text='Search', command=biosearch, bg='black', fg='white')
        c.pack(anchor='center')
def Chem():
    pass
def about():
    pass

if _name_ == '_main_':
    root = Tk()
    root.title("Student Assistant")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure(background='pink')
    photo=PhotoImage(file='photo.png')
    l1=Label(image=photo)
    l1.place(x=0, y=0, relwidth=1, relheight=1)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="Biology", command=Bio)
    FileMenu.add_command(label="English", command = Eng)
    FileMenu.add_command(label = "Chemistry", command = Chem)
    MenuBar.add_cascade(label = "Subjects", menu=FileMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Our Teacher-'Tech With Tim'", command=about)
    MenuBar.add_cascade(label="Our Inspiration", menu=HelpMenu)
    setup=Menu(MenuBar,tearoff=0)
    root.config(menu=MenuBar)
    root.mainloop()
