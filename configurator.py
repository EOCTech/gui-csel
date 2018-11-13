#!/usr/bin/env python

from Tkinter import *

#First try at a class. In the future I want to add two more things: type and stringvalue
#This should allow us to score goodUser, badProgram, etc
class Vuln:
    def __init__(self,name,points,enabled,keywords,hit,miss,tip):
        self.name = name        #What is the vulnerability called?
        self.points = points    #How many points is it worth?
        self.enabled = enabled  #Is the item being scored?
        self.kw = keywords      #Keywords to look for when scoring
        self.hm = hit           #Message to display on a hit
        self.mm = miss          #Message to display on a miss
        self.tip = tip          #Explanation of the item

v01 = Vuln("disableGuest","0","0","","","","Is the guest disabled in lightdm?")
v02 = Vuln("disableAutoLogin","0","0","","","","Is there an auto logged in user in lightdm?")
v03 = Vuln("disableUserGreeter","0","0","","","","Disable the user greeter in lightdm")
v04 = Vuln("disableSshRootLogin","0","0","","","","'PermitRootLogin no' exists in sshd_config")
v05 = Vuln("checkFirewall","0","0","","","","Is ufw enabled?")
v06 = Vuln("checkKernel","0","0","","","","Has kernel been updated?")
v07 = Vuln("avUpdated","0","0","","","","Has clamav freshclam been run?")
v08 = Vuln("NotImplementedYet","0","0","","","","No tip to give...yet")
v50 = Vuln("goodUser","0","0","","","","Lose points for removing this user (use negative number)")
v51 = Vuln("badUser","0","0","","","","Remove these users to score")
v52 = Vuln("goodProgram","0","0","","","","Score points by installing these programs")
v53 = Vuln("badProgram","0","0","","","","Score points by removing these programs")
v54 = Vuln("checkStartup","0","0","","","","Check rc.local for a specific string (type string in 'keywords')")
v55 = Vuln("checkHosts","0","0","","","","Check /etc/hosts for a specific string (type string in 'keywords')")
v56 = Vuln("badCron","0","0","","","","Check the root cron for a specific string (type string in 'keywords')")
v57 = Vuln("badFile","0","0","","","","Score points for deleting this file")
vulns = [v01,v02,v03,v04,v05,v06,v07,v08,v50,v51,v52,v53,v54,v55,v56,v57]

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
cb52 = IntVar()
cb53 = IntVar()
cb54 = IntVar()
cb55 = IntVar()
cb56 = IntVar()
cb57 = IntVar()
checkBoxes = [cb01,cb02,cb03,cb04,cb05,cb06,cb07,cb08,cb50,cb51,cb52,cb53,cb54,cb55,cb56,cb57]

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
pts52 = IntVar()
pts53 = IntVar()
pts54 = IntVar()
pts55 = IntVar()
pts56 = IntVar()
pts57 = IntVar()
pointVal = [pts01,pts02,pts03,pts04,pts05,pts06,pts07,pts08,pts50,pts51,pts52,pts53,pts54,pts55,pts56,pts57]

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
kw52 = StringVar()
kw53 = StringVar()
kw54 = StringVar()
kw55 = StringVar()
kw56 = StringVar()
kw57 = StringVar()
keyWords = [kw01,kw02,kw03,kw04,kw05,kw06,kw07,kw08,kw50,kw51,kw52,kw53,kw54,kw55,kw56,kw57]

root.title('CSEL Setup Tool')

#Making some boxes
checkbox01 = Checkbutton(root,text=v01.name,variable=cb01)
points01 = Entry(root,textvariable=pts01)
label01 = Label(root,text=v01.tip)
checkbox02 = Checkbutton(root,text=v02.name,variable=cb02)
points02 = Entry(root,textvariable=pts02)
label02 = Label(root,text=v02.tip)
checkbox03 = Checkbutton(root,text=v03.name,variable=cb03)
points03 = Entry(root,textvariable=pts03)
label03 = Label(root,text=v03.tip)
checkbox04 = Checkbutton(root,text=v04.name,variable=cb04)
points04 = Entry(root,textvariable=pts04)
label04 = Label(root,text=v04.tip)
checkbox05 = Checkbutton(root,text=v05.name,variable=cb05)
points05 = Entry(root,textvariable=pts05)
label05 = Label(root,text=v05.tip)
checkbox06 = Checkbutton(root,text=v06.name,variable=cb06)
points06 = Entry(root,textvariable=pts06)
label06 = Label(root,text=v06.tip)
checkbox07 = Checkbutton(root,text=v07.name,variable=cb07)
points07 = Entry(root,textvariable=pts07)
label07 = Label(root,text=v07.tip)
checkbox08 = Checkbutton(root,text=v08.name,variable=cb08)
points08 = Entry(root,textvariable=pts08)
label08 = Label(root,text=v08.tip)
#Gettting into the fancier vulnerabilities now
checkbox50 = Checkbutton(root,text=v50.name,variable=cb50)
points50 = Entry(root,textvariable=pts50)
keywords50 = Entry(root,textvariable=kw50)
label50 = Label(root,text=v50.tip)
checkbox51 = Checkbutton(root,text=v51.name,variable=cb51)
points51 = Entry(root,textvariable=pts51)
keywords51 = Entry(root,textvariable=kw51)
label51 = Label(root,text=v51.tip)
checkbox52 = Checkbutton(root,text=v52.name,variable=cb52)
points52 = Entry(root,textvariable=pts52)
keywords52 = Entry(root,textvariable=kw52)
label52 = Label(root,text=v52.tip)
checkbox53 = Checkbutton(root,text=v53.name,variable=cb53)
points53 = Entry(root,textvariable=pts53)
keywords53 = Entry(root,textvariable=kw53)
label53 = Label(root,text=v53.tip)
checkbox54 = Checkbutton(root,text=v54.name,variable=cb54)
points54 = Entry(root,textvariable=pts54)
keywords54 = Entry(root,textvariable=kw54)
label54 = Label(root,text=v54.tip)
checkbox55 = Checkbutton(root,text=v55.name,variable=cb55)
points55 = Entry(root,textvariable=pts55)
keywords55 = Entry(root,textvariable=kw55)
label55 = Label(root,text=v55.tip)
checkbox56 = Checkbutton(root,text=v56.name,variable=cb56)
points56 = Entry(root,textvariable=pts56)
keywords56 = Entry(root,textvariable=kw56)
label56 = Label(root,text=v56.tip)
checkbox57 = Checkbutton(root,text=v57.name,variable=cb57)
points57 = Entry(root,textvariable=pts57)
keywords57 = Entry(root,textvariable=kw57)
label57 = Label(root,text=v57.tip)
submit = Button(root,text='Submit',command=callback)


#Let's make a table!
head1 = Label(root,text="Score?",font=('Verdana',10,'bold'))
head2 = Label(root,text="Point Value",font=('Verdana',10,'bold'))
head3 = Label(root,text="Explanation",font=('Verdana',10,'bold'))
head4 = Label(root,text="Score?",font=('Verdana',10,'bold'))
head5 = Label(root,text="Point Value",font=('Verdana',10,'bold'))
head6 = Label(root,text="Keywords",font=('Verdana',10,'bold'))
head7 = Label(root,text="Explanation",font=('Verdana',10,'bold'))

head1.grid(row=0,column=1)
head2.grid(row=0,column=2)
head3.grid(row=0,column=3)
head4.grid(row=49,column=1)
head5.grid(row=49,column=2)
head6.grid(row=49,column=3)
head7.grid(row=49,column=4)
checkbox01.grid(row=1,column=1,sticky=W)
points01.grid(row=1,column=2)
label01.grid(row=1,column=3,sticky=W)
checkbox02.grid(row=2,column=1,sticky=W)
points02.grid(row=2,column=2)
label02.grid(row=2,column=3,sticky=W)
checkbox03.grid(row=3,column=1,sticky=W)
points03.grid(row=3,column=2)
label03.grid(row=3,column=3,sticky=W)
checkbox04.grid(row=4,column=1,sticky=W)
points04.grid(row=4,column=2)
label04.grid(row=4,column=3,sticky=W)
checkbox05.grid(row=5,column=1,sticky=W)
points05.grid(row=5,column=2)
label05.grid(row=5,column=3,sticky=W)
checkbox06.grid(row=6,column=1,sticky=W)
points06.grid(row=6,column=2)
label06.grid(row=6,column=3,sticky=W)
checkbox07.grid(row=7,column=1,sticky=W)
points07.grid(row=7,column=2)
label07.grid(row=7,column=3,sticky=W)
checkbox08.grid(row=8,column=1,sticky=W)
points08.grid(row=8,column=2)
label08.grid(row=8,column=3,sticky=W)
checkbox50.grid(row=50,column=1,sticky=W)
points50.grid(row=50,column=2)
keywords50.grid(row=50,column=3)
label50.grid(row=50,column=4,sticky=W)
checkbox51.grid(row=51,column=1,sticky=W)
points51.grid(row=51,column=2)
keywords51.grid(row=51,column=3)
label51.grid(row=51,column=4,sticky=W)
checkbox52.grid(row=52,column=1,sticky=W)
points52.grid(row=52,column=2)
keywords52.grid(row=52,column=3)
label52.grid(row=52,column=4,sticky=W)
checkbox53.grid(row=53,column=1,sticky=W)
points53.grid(row=53,column=2)
keywords53.grid(row=53,column=3)
label53.grid(row=53,column=4,sticky=W)
checkbox54.grid(row=54,column=1,sticky=W)
points54.grid(row=54,column=2)
keywords54.grid(row=54,column=3)
label54.grid(row=54,column=4,sticky=W)
checkbox55.grid(row=55,column=1,sticky=W)
points55.grid(row=55,column=2)
keywords55.grid(row=55,column=3)
label55.grid(row=55,column=4,sticky=W)
checkbox56.grid(row=56,column=1,sticky=W)
points56.grid(row=56,column=2)
keywords56.grid(row=56,column=3)
label56.grid(row=56,column=4,sticky=W)
checkbox57.grid(row=57,column=1,sticky=W)
points57.grid(row=57,column=2)
keywords57.grid(row=57,column=3)
label57.grid(row=57,column=4,sticky=W)
submit.grid(row=99,column=3)

root.mainloop()