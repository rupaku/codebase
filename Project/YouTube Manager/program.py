from pytube import YouTube
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
import threading


class Application:
    def __init__(self, root):
        self.root = root
        self.root.grid__rowconfigure(0, weight=2)
        self.root.grid__columnconfigure(0, weight=1)
        self.root.configure(bg="#ffdddd")
        self.top_label = Label(self.root, text="YOUTUBE DOWNLOAD MANAGER", fg="orange", font=('Aerial', 70))
        # put this label on window using grid
        self.top_label.grid(pady=(0, 10))
        self.link_label = Label(self.root, text="Paste the youtube link below", fg="orange", font=('Aerial', 30))
        self.link_label.grid(pady=(0, 20))
        self.youtubeEntryVar = StringVar()
        self.youtubeEntry = Entry(self.root, width=70, textvariable=self.youtubeEntryVar, font=('Aerial', 25),
                                  fg='green')
        self.youtubeEntry.grid(pady=(0, 15), ipady=2)
        self.youtubeEntryError = Label(self.root, text="", fg="orange", font=('Aerial', 20))
        self.youtubeEntryError.grid(pady=(0, 8))
        self.youtubeFileSaveLabel = Label(self.root, text="choose directory", fg="orange", font=('Aerial', 30))
        self.youtubeFileSaveLabel.grid()
        self.youtubeFileDirectoryButton = Button(self.root, text="directory", fg="orange",
                                                 font=('Aerial', 30), command=self.openDirectory)
        self.youtubeFileDirectoryButton.grid(pady=(10, 3))
        self.FileLocationLabel = Label(self.root, text="", font=('Aerial', 30))
        self.FileLocationLabel.grid(pady=())
        self.youtubeChooseLabel = Label(self.root, text="Choose the download type", font=('Aerial', 30))
        self.youtubeChooseLabel.grid(pady=())

        downloadChoices = [("Audio mp3", 1), ("video mp4", 2)]
        self.choicesVar = StringVar()
        self.choicesVar.set(1)

        for text, mode in downloadChoices:
            self.youtubeChoices = Radiobutton(self.root, text=text, font=("Arial", 15), variable=self.choicesVar)
            self.youtubeChoices.grid()
        self.youtubeDownloadButton = Button(self.root, text="download", width=10,
                                            font=('Aerial', 30), command=self.checkyoutubelink)
        self.youtubeDownloadButton.grid(pady=(30, 5))

    def checkyoutubelink(self):
        self.matchyoutubelink = re.match("^https://www.youtube.com/.*", self.youtubeEntryVar.get())

        if not self.matchyoutubelink:
            self.youtubeEntryError.config(text="Invalid youtube link", fg="red")
        elif not self.openDirectory():
            self.youtubeFileSaveLabel.config(text="Please choose the folder", fg="red")
        elif self.matchyoutubelink and self.openDirectory():
            self.downloadwindow()

    def downloadwindow(self):
        self.newWindow = Toplevel(self.root)
        self.root.withdraw()
        self.app = SecondPage(self.newWindow, self.youtubeEntryVar.get(), self.FolderName.get(), self.choicesVar.get())

    def openDirectory(self):
        self.FolderName = filedialog.askdirectory()
        if (len(self.FolderName) > 0):
            self.fileLocationLabel.config(text=self.FolderName, fg="green", font=("Arial", 25))
            return True
        else:
            self.fileLocationLabel.config(text="Please choose folder name, fg="
            red
            ", font=("
            Arial
            ", 25))


class SecondPage:
    def __init__(self, downloadwindow, youtubeEntry, FolderName, Choices):
        self.downloadwindow = downloadwindow
        downloadwindow.state("zoomed")
        self.downloadwindow.grid__rowconfigure(0, weight=2)
        self.downloadwindow.grid__columnconfigure(0, weight=1)
        self.youtubeEntry = youtubeEntry
        self.FolderName = FolderName
        self.Choices = Choices

        self.yt = YouTube(self.youtubeEntry)

        if self.choices == "1":
            self.video_type = self.yt.streams.filter(only_audio=True).first()
            self.MaxFileSize = self.video_type.file_size

        if self.choices == "2":
            self.video_type = self.yt.streams.first()
            self.MaxFileSize = self.video_type.file_size

        self.loadingLabel = Label(self.downloadwindow, text="downloading in progress", font=("Arial", 25))
        self.loadingLabel.grid(pady=(100, 0)

        self.loadingpercent = Label(self.downloadwindow, text="0", fg="green", font=("Arial", 40))
        self.loadingpercent.grid(pady=(50, 0)

        self.progressbar = ttk.Progressbar(self.downloadwindow,length=500,orient='horizontal',mode=)
        self.loadingpercent.grid(pady=(50, 0)



        if __name__ == '__main__':
            window = tk.Tk()
        window.state("zoomed")
        app = Application(window)
        window.mainloop()
