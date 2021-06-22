import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
import kivy.utils as utils
from kivy.uix.dropdown import DropDown
import pandas as pd

class Grammar:
    def __init__(self,cari):
        self.cari = cari

    def Verb1(self):
        vocab = pd.read_csv('C:/Users/affaa/downloads/verbs.csv')
        verb1 = vocab['verb1'].values
        verb1 = list(verb1)
        return verb1

    def verb2(self):
        vocab = pd.read_csv('C:/Users/affaa/downloads/verbs.csv')
        verb2 = vocab['verb2'].values
        verb2 = list(verb2)
        return verb2
    
    def verb3(self):
        vocab = pd.read_csv('C:/Users/affaa/downloads/verbs.csv')
        verb3 = vocab['verb3'].values
        verb3 = list(verb3)
        return verb3
    
    def verbs(self):
        vocab = pd.read_csv('C:/Users/affaa/downloads/verbs.csv')
        verbs = vocab['verbs'].values
        verbs = list(verbs)
        return verbs

    def verbing(self):
        vocab = pd.read_csv('C:/Users/affaa/downloads/verbs.csv')
        verbing = vocab['verbing'].values
        verbing = list(verbing)
        return verbing

    def indeks(self):
        vocab = pd.read_csv('C:/Users/affaa/downloads/verbs.csv')
        cari1 = self.cari.lower()
        verb1 = vocab['verb1'].values
        verb1 = list(verb1)
        indeks = verb1.index(cari1)
        return int(indeks)

class MyGrid(Screen):
    subjek = ObjectProperty(None)
    verb = ObjectProperty(None)
    objek = ObjectProperty(None)
    def btn_pilih(self):
        lay2 = SecLay()
        lay2
        global subj
        global obj
        global veb
        global inds
        subj = self.subjek.text
        obj = self.objek.text
        veb = self.verb.text

class SecLay(Screen):
    def btn_simpres(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        simpres = gram.Verb1()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} {simpres[inds]} {obj}"
        sentence = str(sentence)
        print(sentence)
        return sentence
    
    def btn_prescon(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        prescon = gram.verbing()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} {prescon[inds]} {obj}"
        sentence = str(sentence)
        print(sentence)
        return sentence
    
    def btn_presperf(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        presperf = gram.verb3()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} have {presperf[inds]} {obj}"
        sentence = str(sentence)
        print(sentence)
        return sentence

    def btn_presperfcon(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        presperfcon = gram.verbing()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} have been {presperfcon[inds]} {obj}"
        sentence = str(sentence)
        print(sentence)
        return sentence

    def btn_simpast(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        simpast = gram.verb2()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} {simpast[inds]} {obj}"
        sentence = str(sentence)
        print(sentence)
        return sentence

    def btn_pastcon(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        gender = ["you", "it", "we", "they"]
        pastcon = gram.verbing()
        inds = gram.indeks()
        global sentence
        if subj.lower() in gender:
            sentence = f"{subj} were {pastcon[inds]} {obj}"
        else:
            sentence = f"{subj} was {pastcon[inds]} {obj}"
        sentence = str(sentence)
        print(sentence)
        return sentence

    def btn_pastperf(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        verb3 = gram.verb3()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} {verb3} {obj}"
        print(sentence)
        return sentence

    def btn_pastperfcon(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        verbing = gram.verbing()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} had been {verbing} {obj}"
        print(sentence)
        return sentence
    
    def btn_simpfut(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        verb3 = gram.verb3()
        global sentence
        sentence = f"{subj} {verb3} {obj}"
        print(sentence)
        return sentence
    
    def btn_futcon(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        verbing = gram.verbing()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} {verbing} {obj}"
        print(sentence)
        return sentence
    
    def btn_futper(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        verbed = gram.verb3()
        inds = gram.indeks()
        global sentence
        sentence = f"{subj} will have {verb3} {obj}"
        print(sentence)
        return sentence
    
    def btn_futpercon(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        verbing = gram.verbing()
        inds = gram.inds()
        global sentence
        sentence = f"{subj} will have been {verbing} {obj}"
        print(sentence)
        return sentence

    '''
    def btn_pastfut(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        inds = gram.indeks()

    
    def btn_pastfutcon(self):
        lay3 = ThirdLay()
        lay3
        gram = Grammar(veb)
        inds = gram.indeks()
        sentence = f"{subj} {} {veb}"
        print(sentence)
        return sentence
    #lay3 = ThirdLay()
    '''

class ThirdLay(Screen):
    kalimat = StringProperty()
    verb1 = StringProperty()
    verb2 = StringProperty()
    verb3 = StringProperty()
    #hasil = ObjectProperty()
    def outhasil(self):
        gram = Grammar(veb)
        inds = gram.indeks()
        self.kalimat = sentence
        verb1list = gram.Verb1()
        verb2list = gram.verb2()
        verb3list = gram.verb3()
        self.verb1 = verb1list[inds]
        self.verb2 = verb2list[inds]
        self.verb3 = verb3list[inds]

    def btn_back(self):
        lay1 = MyGrid()
        lay1
class WindowManager(ScreenManager):
    MyGrid = ObjectProperty()
    SecLay= ObjectProperty()
    ThirdLay= ObjectProperty()

kv = Builder.load_file('inglish.kv')

class InglishApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    InglishApp().run()