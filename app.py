import pyttsx3

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("sample.pdf", "rb"))

# print how many pages input1 has:
print ("document1.pdf has %d pages." % input1.getNumPages())

page4 = input1.getPage(0)
print(type(page4))
page4content = page4.extractText()
print(page4content)
engine = pyttsx3.init()

# engine.say("I will speak this text")
# engine.runAndWait()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

engine.say(page4content)

engine.runAndWait()
engine.stop()