#!/usr/bin/env python

from Tkinter import *

#First try at a class. In the future I want to add two more things: type and stringvalue
#This should allow us to score goodUser, badProgram, etc
class Vuln:
    def __init__(self,name,points,enabled):
        self.name = name
        self.points = points
        self.enabled = enabled

v1 = Vuln("disableGuest","0","0")
v2 = Vuln("disableAutoLogin","0","0")
v3 = Vuln("disableUserGreeter","0","0")
v4 = Vuln("disableSshRootLogin","0","0")
v5 = Vuln("checkFirewall","0","0")
v6 = Vuln("checkKernel","0","0")
v7 = Vuln("avUpdated","0","0")
v8 = Vuln("disableAutoLogin","0","0")
v9 = Vuln("notImplementedYet","0","0")
v10 = Vuln("notImplementedYet","0","0")
vulns = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]

#######NOT QUITE READY FOR THIS YET##############
# class ListVuln:
#     def __init__(self,name,strValue,points,enabled):
#         self.name = name
#         self.strValue = strValue
#         self.points = points
#         self.enabled = enabled

# lv1 = ListVuln("goodUser","","0","0")
# lv2 = ListVuln("goodProgram","","0","0")
# lv3 = ListVuln("badUser","","0","0")
# lv4 = ListVuln("badProgram","","0","0")
# listVulns = [lv1,lv2,lv3,lv4]

def writeToConfig(name,points,enabled):
        if enabled == 1:
          f = open('csel.cfg','a')
          line1 = name+'=(y)\n'
          line2 = name+'Value=('+str(points)+')\n'
          f.write(line1)
          f.write(line2)

#What happens when you click Submit?
def callback():
    #We wanna use those fancy variable lists 
    global checkBoxes
    global vulns
    global pointVal
    global listVulns
    f = open('csel.cfg','w+')
    for vuln,checkEn,score in zip(vulns,checkBoxes,pointVal):
        vuln.enabled = checkEn.get()
        vuln.points = score.get()
        #This is just a stand in. Next up, call a function to write to a file.   
        #print vuln.name,vuln.points,vuln.enabled
        writeToConfig(vuln.name,vuln.points,vuln.enabled)
    f.close()
root = Tk()
#Initialize a crap-ton of TK vars. Can you find a more elegant way?
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
checkBoxes = [cb01,cb02,cb03,cb04,cb05,cb06,cb07,cb08,cb09,cb10]

pts01 = IntVar()
pts02 = IntVar()
pts03 = IntVar()
pts04 = IntVar()
pts05 = IntVar()
pts06 = IntVar()
pts07 = IntVar()
pts08 = IntVar()
pts09 = IntVar()
pts10 = IntVar()
pointVal = [pts01,pts02,pts03,pts04,pts05,pts06,pts07,pts08,pts09,pts10]

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
checkbox09 = Checkbutton(root,text=v9.name,variable=cb09)
points09 = Entry(root,textvariable=pts09)
checkbox10 = Checkbutton(root,text=v10.name,variable=cb10)
points10 = Entry(root,textvariable=pts10)
submit = Button(root,text='Submit',command=callback)

#Let's make a table!
head1 = Label(root,text="Enabled?")
head2 = Label(root,text="Point Value")
head1.grid(row=0,column=1)
head2.grid(row=0,column=2)
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
checkbox09.grid(row=9,column=1,sticky=W)
points09.grid(row=9,column=2)
checkbox10.grid(row=10,column=1,sticky=W)
points10.grid(row=10,column=2)
submit.grid(row=99,column=2)

root.mainloop()