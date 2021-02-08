from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

# File Location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text = Folder_Name, fg = "green")

    else:
        locationError.config(text = "Please Choose Folder!", fg = "red")

# Download Video
def DownloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if (len(url) > 1):
        ytdError.config(text = "")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text = "Paste your Link again!", fg = "red")


    # Download Function
    select.download(Folder_Name)
    ytdError.config(text = "Download Completed!")
    

root = Tk()
root.title("Youtube Downloader")
root.geometry("350x400") # set window
root.columnconfigure(0,weight=1) # set all content in center

# YouTube Link Label
ytdLabel = Label(root, text="Video Link", font=("jost",15))
ytdLabel.grid()

# Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

# Error Message
ytdError = Label(root, text="Error Message", fg="red", font=("jost",10))
ytdError.grid()

# Save Label
saveLabel = Label(root, text="Save the Video", font=("jost", 15, "bold"))
saveLabel.grid()

# Button for saving file
saveEntry = Button(root, width = 10, bg = "red", fg = "white", text = "Choose Path", command = openLocation)
saveEntry.grid()

# Error Message Location
locationError = Label(root, text = "Error Message of Path", fg = "red", font = ("jost", 10))
ytdError.grid()

# Download Quality
ytdQuality = Label(root, text = "Select Quality", font = ("jost", 15))
ytdQuality.grid()

# Combo Box
choices = ["720p", "144p", "Only Audio"]
ytdChoices = ttk.Combobox(root, values = choices)
ytdChoices.grid()

# Download Button
downloadButton = Button(root, text = "Download", width = 10, bg = "red", fg = "white", command = DownloadVideo)
downloadButton.grid()

# Developer Label
developerLabel = Label(root, text = "Made By ENS", font = ("jost", 15))
developerLabel.grid()


root.mainloop()