import webbrowser
import tkinter #only need these two modules


#these are the button commands so to speak, just a simple open webbrowser command to openthe link
def vault():
    webbrowser.open("http://vaultbrewing.com/beer/")
def crookedeye():
    webbrowser.open("http://www.crookedeyebrewery.com/for-what-ales-you/")
def naked():
    webbrowser.open("http://www.nakedbrewingcompany.com/beers/")
def prism():
    webbrowser.open("http://prismbeer.com/beer_type/all-beers/")
def roundguys():
    webbrowser.open("http://pub.roundguysbrewery.com/")
def yards():
    webbrowser.open("http://yardsbrewing.com/ales/")
def towerhill():
    webbrowser.open(r'http://www.towerhillbrewery.com/#brews-section')
def freewill():
    webbrowser.open("https://www.freewillbrewing.com/year-round")
def slyfox():
    webbrowser.open("http://www.slyfoxbeer.com/beers")
def doylestown():
    webbrowser.open("https://www.doylestownbrewingcompany.com/whats-on-tap")
def twosp():
    webbrowser.open(r'http://www.2spbrewing.com/our-beers/')
def victory():
    webbrowser.open("https://www.victorybeer.com/beers/")
def brokeng():
    webbrowser.open(r'http://brokengoblet.com/index.html#beers')

window = tkinter.Tk()
window.configure(background='#ffa31a')
window.title("Whats on tap?")
window.wm_iconbitmap('favicon.ico')
vault1 =tkinter.Button(window, text='Vault Brewing, Yardley PA', command=vault,background='khaki1')
crookedeye1 =tkinter.Button(window, text='Crooked Eye Brewing, Hatboro PA', command=crookedeye,background='khaki1')
naked1 =tkinter.Button(window, text='Naked Brewing, Huntingdon Valley PA',command=naked,background='khaki1')
prism1 =tkinter.Button(window, text='Prism Brewing, Lansdale PA',command = prism,background='khaki1')
roundguys1 =tkinter.Button(window,text ='Round Guys Brewing, Lansdale PA', command=roundguys,background='khaki1')
yards1 =tkinter.Button(window, text = 'Yards Brewing, Philadelphia PA',command = yards,background='khaki1')
towerhill1 = tkinter.Button(window, text = 'Towerhill Brewing, Chalfont, PA',command= towerhill,background='khaki1')
freewill1 = tkinter.Button(window, text = 'Free Will Brewing, Perkasie, PA',command = freewill,background='khaki1')
slyfox1 = tkinter.Button(window, text = 'SlyFox Brewing, Phoenixville, PA', command = slyfox,background='khaki1')
doylestown1 = tkinter.Button(window, text = 'Doylestown Brewing, Doylestown PA',command = doylestown,background='khaki1')
twosp1 = tkinter.Button(window, text = '2sp Brewing, Aston PA',command = twosp,background='khaki1')
victory1 = tkinter.Button(window, text = 'Victory Brewing, Downingtown PA', command = victory,background='khaki1')
brokeng1 = tkinter.Button(window, text = 'Broken Goblet, Bristol, PA', command = brokeng,background='khaki1')

vault1.grid(row=2, column=0)
crookedeye1.grid(row=3, column=0)
naked1.grid(row=4, column=0)
prism1.grid(row=5, column=0)
roundguys1.grid(row=6, column=0)
yards1.grid(row=7, column=0)
towerhill1.grid(row=8, column=0)
freewill1.grid(row=2, column=1)
slyfox1.grid(row=3, column=1)
doylestown1.grid(row=4, column=1)
twosp1.grid(row=5, column=1)
victory1.grid(row=6, column=1)
brokeng1.grid(row=7, column=1)






window.mainloop()