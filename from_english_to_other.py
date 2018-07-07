#Author: PRANAB SARKAR
#Address:JALPAIGURI,WEST BENGAL,INDIA.
#Contact No:+91-7001029414
#Email address: sarkarpranab66@gmail.com



import speech_recognition as sr
from googletrans import Translator
from gtts import  gTTS
import os
import pandas as pd

class tt:
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'zh-tw': 'chinese',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ku': 'kurdish',
        'ku': 'kurmanji',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'my': 'burmese',
        'ne': 'nepali',
        'no': 'norwegian',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
        'fil': 'Filipino',
        'he': 'Hebrew'
    }

    def __init__(self,lang):
        self.lang=lang
        df = pd.DataFrame()
        df['code'] = self.LANGUAGES.keys()
        df['language'] = self.LANGUAGES.values()

        find_lang1 = df[df.language == self.lang]
        find_lang2 = find_lang1.code.values.tolist()

        self.str1 = ''.join(find_lang2)




    def solution_firstlayer(self):
        try:
            print("\n Thank you for choosing this language hope you will find it intresting :)")
            sen = input("Enter the sentence : ")
            translator = Translator()
            x = translator.translate(sen, dest=self.str1)  # bn for bengali and hi for hindi en for enflish
            print("\nTranslated text = {}".format(x.text))
            qui()
        except:
            print("\n\n---------------The language you have entered is not available----------------------\n                PLEASE ENTER ANY AVIALABLE LANGUAGE FROM THE LIST")
            main()

    def solution_secondlayer(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak:")
                audio = r.listen(source)

            try:

                print("You said : " + r.recognize_google(audio))
                translator = Translator()
                x = translator.translate(r.recognize_google(audio),
                                         dest=self.str1)  
                print("Translated text = {}".format(x.text))

                speak = gTTS(x.text, self.str1)
                speak.save("1.mp3")
                os.system("1.mp3")
                qui()
            except sr.UnknownValueError:
                print("Can you please repeat again :) ...")
                self.solution_secondlayer()

            except sr.RequestError as e:
                print("Please check your internet connection..")
                self.solution_secondlayer()

        except:
            print(
                "\n\n---------------The language you have entered is not available----------------------\n                PLEASE ENTER ANY AVIALABLE LANGUAGE FROM THE LIST")
            main()




    def about_me(self):
        print("Author : Pranab Sarkar \nContact Number : +91-7001029414\nEmail : sarkarpranab66@gmail.com\nBuild Ver:1.0")
    def ex(self): 
        qui()





def qui():
    global take_ch5
    try:
        take_ch5=input("\nDo you want to Quit (Y/N) :")
    except:
        print("Please enter correct values")
        qui()
    take_ch112 = take_ch5.lower()
    if(take_ch112=="y"):
        try:
            print("\nThank You Visit again !!")
        except:
            print("\nThank You Visit again !!")
    elif(take_ch112=="n"):
        print("\nWelcome again master")
        main()

    else:
        print("\nPlease fill up the options properly.")
        main()

def main():
    global take_ch2, take_ch2
    take_ch1=0
    print("\n_________________Welcome to the converter  V1.0_________________")
    print("\n\n                     1. Text to Text")
    print("\n                     2. Speech to speech")
    print("\n                     3. About")
    print("\n                     4. Exit\n\n")
    try:
        take_ch1 = int(input("Enter your choice :"))
    except:
        print("Please fill up the options properly")
        main()
    if(take_ch1==1):
        print("\n This is a translator which can translate a sentence from english to other. \n  ")
        try:
            ink=input("Please enter the language in which you want to translate :")
        except:
            print("\nPlease enter correct input.")
            ink = input("Please enter the language in which you want to translate :")

        p1=tt(ink.lower())
        p1.solution_firstlayer()

    elif(take_ch1==2):
        print("\n This is a translator which can translate your spoken sentence from english to other and the converted sentence will be played in a music player. \n  ")
        try:
            ink = input("Please enter the language in which you want to translate :")
        except:
            print("\nPlease enter correct input.")
            ink = input("Please enter the language in which you want to translate :")
        p2=tt(ink.lower())
        p2.solution_secondlayer()
    elif(take_ch1==3):
        p3=tt("hindi")
        p3.about_me()
    elif(take_ch1==4):
        p4=tt("hindi")
        p4.ex()

    else:

        print("Wrong Choice ... Do you want to continue of quit (Y/N) :")
        p8=tt("hindi")
        p8.ex()


main()
