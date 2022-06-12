from typing import Text
import pdfminer.high_level as pd
import pyttsx3
import datetime
from playsound import playsound
from gtts import gTTS
import os

class PdfToText:
    # as argument takes a path of Pdf file 

    def __init__(self, path) -> None:
    
        self.__path = path
        self.__text = pd.extract_text(self.__path)
        self.__senteces = []
        self.getSentences()
    
    # Getting sentences as List 
    
    def getSentences(self):
        if not self.__senteces:
            if not type(self.__text) is list:
                self.__text = self.__text.split('.')
            for idx, sentence in enumerate(self.__text):
                    # removing new lines from sentence
                    sentence = sentence.split('\n')
                    # joining all the sentences part of sentence  
                    sentence = ' '.join(sentence)
                    # removing leading and trailing spaces 
                    sentence = sentence.strip()
                    # adding . to the end of each sentence
                    sentence +='.'
                    self.__senteces.append(sentence)
        
        return self.__senteces

    # Getting Text as a string 
    
    def getText(self)->str:

        return ''.join(self.__senteces)
    
    # Saving Text to txt file as Name or default first 3 word of sentence 
    
    def SaveAsText(self, name = None):
        
        # Creating folder      
        
        if not name:
            name = (self.__senteces[0])
        with open(name + '.txt' , 'a') as file:
            for i in self.__senteces:
                file.writelines(i + '\n')

# pyttx3

class PlaySoundOffline:
    
    # creating an engine to read Text
    
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
    
    # Reading text as argument takes a Text: str
    
    def play(self, text):
        
        self.engine.setProperty('rate' , 175)
        
        for sentence in text:
            self.engine.say(sentence)
            self.engine.runAndWait()

# gTTS

class PlaySoundOnline:

    # As argument takes text, lang of text as str and creates gTTS onject to read Text  

    def __init__(self, text ,lang) -> None:
        
        self.gtts = gTTS(text, lang=lang)
        self.save()
    
    # Saves audio as todaysdate.mp3

    def save(self):
        
        date = datetime.date.today() 

        self.gtts.save(str(date) + '.mp3')






 

def main():
    #PDF = PdfToText('za_textom.pdf')
    
    #PDF.SaveAsText('Second')
    with open('Second.txt', '+r' ,encoding='utf8') as file:
        k = file.readline()

    PDF =PlaySoundOnline(k , 'ru')

    print (k)













if __name__ == '__main__':
    main()


# Create a folder audio/txt if it does not exist and store all audios and texts in that folder
# Create a another folder for PDFS 
# Split all Classes 
 