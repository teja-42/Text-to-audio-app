from gtts import gTTS
import os
from tkinter import *


root=Tk()

c=Canvas(root,width=400,height=300)
c.pack()

def textToSpeech():
    text=e.get()
    language="en"
    output=gTTS(text=text,lang=language,slow=False)
    output.save("o.mp3")
    os.system("start o.mp3")

e=Entry(root)
c.create_window(200,180,window=e)

b=Button(root,text="Start",command=textToSpeech)
c.create_window(200,230,window=b)

root.mainloop()

