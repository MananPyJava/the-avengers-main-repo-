from tkinter import *
import wikipedia
import pandas as pd

a=0
d=0
entry1=''


def wikisearch():
    global a,entry1
    a+=1

    if a==1:
        l2=Label(text="Enter Term You Want To Search and press button below: ",bg='black',fg='white')
        l2.pack()
        print('Bio')
        entry1 = Entry(root,width=200,bg='black',fg='white')
        entry1.pack()
        b=Button(text='Search', command=search, bg='black',fg='white')
        b.pack(anchor='center')

def search():
    global entry1
    query=entry1.get()
    results = wikipedia.summary(query+" according to", sentences=5)
    l3=Label(root,text=results,wraplength=500,bg='black',fg='white')
    l3.pack()
    print(results)

def Eng():
    global a
    a+=1
    if a==1:
        l4=Label(text="Enter Sentence It will show your grammatical mistakes : ",bg='black',fg='white')
        l4.pack()
        entry2=Entry(root,width=200,bg='black',fg='white')
        entry2.pack()
        c = Button(text='Search', command=search, bg='black', fg='white')
        c.pack(anchor='center')
def Chem():
    data=pd.read_csv('chem_data.csv')
    print(data)

def about():
    pass

root = Tk()
root.title("Student Assistant")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='pink')
#   photo=PhotoImage(file='photo.png')
l1=Label()#image=photo)
l1.place(x=0, y=0, relwidth=1, relheight=1)
MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="Wikipedia search", command=wikisearch)
FileMenu.add_command(label="English", command = Eng)
FileMenu.add_command(label = "Chemistry", command = Chem)
MenuBar.add_cascade(label = "Subjects", menu=FileMenu)
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label = "About Our Teacher-'Tech With Tim'", command=about)
MenuBar.add_cascade(label="Our Inspiration", menu=HelpMenu)
setup=Menu(MenuBar,tearoff=0)
root.config(menu=MenuBar)


def start():
    root.mainloop()


if __name__ == '__main__':
    start()