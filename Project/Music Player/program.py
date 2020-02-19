import tkinter
from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

window = Tk()
mixer.init()
# dimension of window
window.geometry('500x500')
window.title('Python music player')


def help_me():
    tkinter.messagebox.showinfo("")


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar = Menu(window)
# start count of element in menu with zero
submenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=window.destroy)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu)
menubar.add_cascade(label="Help", command=help_me)

textLabel = Label(window, text="This is a play button")
textLabel.pack()


def play_music():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Music is playing"
        except:
            tkinter.messagebox.showerror('File not found')
            print("FIle not found")
    else:
        mixer.music.unpause()
        statusbar['text'] = "Music is resumed"


def stop_music():
    mixer.music.stop()
    statusbar['text']="Music is stopped"


def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)

def pause_music():
    global paused
    paused=True
    mixer.music.pause()
    statusbar['text'] = "Music is paused"


def rewind_music():
    play_music()
    statusbar['text'] = "Music is rewinded"

frame=Frame(window)
frame.pack(padx=10,pady=10)

photo = PhotoImage(file='play.png')
photoButton = Button(frame, image=photo, command=play_music)
photoButton.grid(row=0,column=0,padx=10)

stopphoto = PhotoImage(file='stop.png')
stopButton = Button(frame, image=stopphoto, command=stop_music)
stopButton.grid(row=0,column=0,padx=10)

pausephoto = PhotoImage(file='pause.png')
pauseButton = Button(frame, image=pausephoto, command=pause_music)
pauseButton.grid(row=0,column=0,padx=10)

bottomframe=Frame(window)
bottomframe.pack()

rewindphoto = PhotoImage(file='rewind.png')
rewindButton = Button(bottomframe, image=rewindphoto, command=rewind_music)
rewindButton.grid(row=0,column=0)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.grid(row=0,column=1)

statusbar=Label(window,text="keep enjoying the music",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)
window.mainloop()
