from tkinter import *#module for the gui
from gtts import gTTS#import the gTTS module
from playsound import playsound#import thid module to play converted audio

#we create the main window
mainWindow = Tk()
mainWindow.geometry('450x450')
mainWindow.title('Ferrari TTS')
mainWindow.resizable(0,0)


#define the text to speech file
def generate_tts():
    try:text_fil=f"{e1.get('1.0',END)}"
    except: text_fil='Enter something to be converted to speech'
    language = 'en'
    obj = gTTS(
        text=text_fil,
        lang=language,
        slow=False
    )
    #save the file
    obj.save('file.mp3')
    #play the file
    playsound('file.mp3')

#Label
name=Label(mainWindow,text="Enter a text.")
name.pack()
name.place(height=50,width=410,y=20,x=20)

#text input area
e1 = Text(mainWindow,wrap='word')
e1.pack()
e1.place(height=300,width=410,y=50,x=20)

#scrollbar
#scrollb=Scrollbar(mainWindow,orient='vertical',command=e1.yview)
#e1['yscrollcommand']=scrollb.set

#submit button
submit =Button(mainWindow,text='Generate Speech',command=generate_tts)
submit.pack()
submit.place(height=50,width=410,y=350,x=20)


#main loop would be run constantly as  a listener
mainWindow.mainloop()

'''source tutorialspoint
button,
canvas,
checkbutton,
entry,
frame,
label,
listbox,
menubutton,
menu
message
raiobutton
scale
scrollbar
TExt
toplevel
spinbox
paned window
label frame
tkMessage box
'''
