import os
import pandas as pd  #pandas to read excel files
from pydub import AudioSegment # for slicing and trimming audio files
from gtts import gTTS #for converting text to speech (in hindi)


# Converting Text to Speech
def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

# Merging all the audio files
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

# Generating n slicing audio files from railway.mp3
def generateSkeleton():
    audio = AudioSegment.from_mp3("C:\\Users\\jaymi\\Desktop\\Python Projects\\Indian Railway Announcement System\\railway.mp3")

#Generating "yatri kripya dhyaan de"
    start = 88000
    finish =  90200
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_hindi.mp3', format='mp3')

#Generating "se chal kar"
    start = 91000
    finish =  92200
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_hindi.mp3', format='mp3')

#Generating "ke raaste"
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_hindi.mp3', format='mp3')

#Generating "par jaane wali gaadi sankhya"
    start = 96000
    finish =  98900
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3', format='mp3')

#Generating "kuch hi samay mai platform par"
    start = 105500
    finish =  108200
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_hindi.mp3', format='mp3')

#Generating "par aa rahi hai"
    start = 109000
    finish =  112250
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_hindi.mp3', format='mp3')


#Generating Annoucements from text to speech
def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        textToSpeech(item['from'], '2_hindi.mp3')
        textToSpeech(item['via'], '4_hindi.mp3')
        textToSpeech(item['to'], '6_hindi.mp3')
        textToSpeech(item['train_no']+" "+item['train_name'],'8_hindi.mp3')
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}{index+1}.mp3", format = "mp3")



if __name__  == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Generating Announcement...")
    generateAnnouncement("C:\\Users\\jaymi\\Desktop\\Python Projects\\Indian Railway Announcement System\\announce_hindi.xlsx")
    print("Done!")
