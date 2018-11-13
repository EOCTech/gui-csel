#!/usr/bin/env python

from Tkinter import *

#First try at a class. In the future I want to add two more things: type and stringvalue
#This should allow us to score goodUser, badProgram, etc
class Vuln:
    def __init__(self,name,points,enabled,keywords,hit,miss):
        self.name = name        #What is the vulnerability called?
        self.points = points    #How many points is it worth?
        self.enabled = enabled  #Is the item being scored?
        self.kw = keywords      #Keywords to look for when scoring
        self.hm = hit           #Message to display on a hit
        self.mm = miss          #Message to display on a miss

v1 = Vuln("disableGuest","0","0","","","")
v2 = Vuln("disableAutoLogin","0","0","","","")
v3 = Vuln("disableUserGreeter","0","0","","","")
v4 = Vuln("disableSshRootLogin","0","0","","","")
v5 = Vuln("checkFirewall","0","0","","","")
v6 = Vuln("checkKernel","0","0","","","")
v7 = Vuln("avUpdated","0","0","","","")
v8 = Vuln("disableAutoLogin","0","0","","","")
v50 = Vuln("goodUser","0","0","","","")
v51 = Vuln("badUser","0","0","","","")
vulns = [v1,v2,v3,v4,v5,v6,v7,v8,v50,v51]

def writeToConfig(name,points,enabled,keywords):
        if enabled == 1:
          f = open('csel.cfg','a')
          line1 = name+'=(y)\n'
          line2 = name+'Value=('+str(points)+')\n'
          #If there are some keywords, sub them in for the 'y'
          if keywords != '0':
              line1 = name+'=('+str(keywords)+')\n' 
          f.write(line1)
          f.write(line2)
          

#What happens when you click Submit?
def callback():
    #We wanna use those fancy variable lists 
    global checkBoxes
    global vulns
    global pointVal
    global listVulns
    global keyWords
    f = open('csel.cfg','w+')
    for vuln,checkEn,score,key in zip(vulns,checkBoxes,pointVal,keyWords):
        vuln.enabled = checkEn.get()
        vuln.points = score.get()
        vuln.kw = key.get()
        writeToConfig(vuln.name,vuln.points,vuln.enabled,vuln.kw)
    f.close()

#######Tkinter Time!!!###############
root = Tk()
#Initialize a crap-ton of TK vars. Can you find a more elegant way?
#Checkboxes to enable or disable an item
cb01 = IntVar()
cb02 = IntVar()
cb03 = IntVar()
cb04 = IntVar()
cb05 = IntVar()
cb06 = IntVar()
cb07 = IntVar()
cb08 = IntVar()
cb09 = IntVar()
cb10 = IntVar()
cb50 = IntVar()
cb51 = IntVar()
checkBoxes = [cb01,cb02,cb03,cb04,cb05,cb06,cb07,cb08,cb50,cb51]

#Point values for each item
pts01 = IntVar()
pts02 = IntVar()
pts03 = IntVar()
pts04 = IntVar()
pts05 = IntVar()
pts06 = IntVar()
pts07 = IntVar()
pts08 = IntVar()
pts50 = IntVar()
pts51 = IntVar()
pointVal = [pts01,pts02,pts03,pts04,pts05,pts06,pts07,pts08,pts50,pts51]

#These are for the keywords that some of the items take (goodUser, badProgram, etc)
kw01 = StringVar()
kw02 = StringVar()
kw03 = StringVar()
kw04 = StringVar()
kw05 = StringVar()
kw06 = StringVar()
kw07 = StringVar()
kw08 = StringVar()
kw50 = StringVar()
kw51 = StringVar()
keyWords = [kw01,kw02,kw03,kw04,kw05,kw06,kw07,kw08,kw50,kw51]

root.title('CSEL Setup Tool')

#Making some boxes
checkbox01 = Checkbutton(root,text=v1.name,variable=cb01)
points01 = Entry(root,textvariable=pts01)
checkbox02 = Checkbutton(root,text=v2.name,variable=cb02)
points02 = Entry(root,textvariable=pts02)
checkbox03 = Checkbutton(root,text=v3.name,variable=cb03)
points03 = Entry(root,textvariable=pts03)
checkbox04 = Checkbutton(root,text=v4.name,variable=cb04)
points04 = Entry(root,textvariable=pts04)
checkbox05 = Checkbutton(root,text=v5.name,variable=cb05)
points05 = Entry(root,textvariable=pts05)
checkbox06 = Checkbutton(root,text=v6.name,variable=cb06)
points06 = Entry(root,textvariable=pts06)
checkbox07 = Checkbutton(root,text=v7.name,variable=cb07)
points07 = Entry(root,textvariable=pts07)
checkbox08 = Checkbutton(root,text=v8.name,variable=cb08)
points08 = Entry(root,textvariable=pts08)
#Gettting into the fancier vulnerabilities now
checkbox50 = Checkbutton(root,text=v50.name,variable=cb50)
points50 = Entry(root,textvariable=pts50)
keywords50 = Entry(root,textvariable=kw50)
checkbox51 = Checkbutton(root,text=v51.name,variable=cb51)
points51 = Entry(root,textvariable=pts51)
keywords51 = Entry(root,textvariable=kw51)
submit = Button(root,text='Submit',command=callback)

#Let's make a table!
head1 = Label(root,text="Score Vulnerability?")
head2 = Label(root,text="Point Value")
head3 = Label(root,text="Vulnerability Keywords")
head1.grid(row=0,column=1)
head2.grid(row=0,column=2)
head3.grid(row=0,column=3)
checkbox01.grid(row=1,column=1,sticky=W)
points01.grid(row=1,column=2)
checkbox02.grid(row=2,column=1,sticky=W)
points02.grid(row=2,column=2)
checkbox03.grid(row=3,column=1,sticky=W)
points03.grid(row=3,column=2)
checkbox04.grid(row=4,column=1,sticky=W)
points04.grid(row=4,column=2)
checkbox05.grid(row=5,column=1,sticky=W)
points05.grid(row=5,column=2)
checkbox06.grid(row=6,column=1,sticky=W)
points06.grid(row=6,column=2)
checkbox07.grid(row=7,column=1,sticky=W)
points07.grid(row=7,column=2)
checkbox08.grid(row=8,column=1,sticky=W)
points08.grid(row=8,column=2)
checkbox50.grid(row=50,column=1,sticky=W)
points50.grid(row=50,column=2)
keywords50.grid(row=50,column=3)
checkbox51.grid(row=51,column=1,sticky=W)
points51.grid(row=51,column=2)
keywords51.grid(row=51,column=3)
submit.grid(row=99,column=2)

root.mainloop()